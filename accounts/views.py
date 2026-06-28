from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.http import url_has_allowed_host_and_scheme

from .forms import UserRegistrationForm, UserLoginForm, UserProfileUpdateForm, UserReportForm
from .models import User


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()

            if user.role in ['RESCUER', 'SHELTER']:
                messages.success(
                    request,
                    'Registration successful. Your account is pending administrator approval.'
                )
            else:
                messages.success(
                    request,
                    'Registration successful. You can now login to PAWS CONNECT.'
                )

            return redirect('home')
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()

            if not user.is_superuser and user.account_status != 'APPROVED':
                messages.error(
                    request,
                    'Your account is not approved yet. Please wait for administrator approval.'
                )
                return redirect('login')

            login(request, user)
            return redirect('dashboard')
    else:
        form = UserLoginForm()

    return render(request, 'accounts/login.html', {'form': form})


@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have been logged out successfully.')
        return redirect('home')

    return render(request, 'accounts/logout_confirm.html')


@login_required
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('profile')
    else:
        form = UserProfileUpdateForm(instance=request.user)

    return render(request, 'accounts/profile.html', {'form': form})

@login_required
def report_user_view(request, user_id):
    reported_user = get_object_or_404(User, id=user_id)

    if reported_user == request.user:
        messages.error(request, 'You cannot report your own account.')
        return redirect('dashboard')

    if reported_user.role == 'ADMIN':
        messages.error(request, 'Administrator accounts cannot be reported through this form.')
        return redirect('dashboard')

    next_url = request.GET.get('next') or request.POST.get('next') or 'dashboard'

    if not url_has_allowed_host_and_scheme(
        url=next_url,
        allowed_hosts={request.get_host()}
    ):
        next_url = 'dashboard'

    if request.method == 'POST':
        form = UserReportForm(request.POST)

        if form.is_valid():
            user_report = form.save(commit=False)
            user_report.reported_by = request.user
            user_report.reported_user = reported_user
            user_report.related_page = next_url
            user_report.save()

            messages.success(
                request,
                'Your report has been submitted to the administrator for review.'
            )

            return redirect(next_url)
    else:
        form = UserReportForm()

    return render(request, 'accounts/report_user.html', {
        'form': form,
        'reported_user': reported_user,
        'next_url': next_url,
    })