from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import UserRegistrationForm, UserLoginForm


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