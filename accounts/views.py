from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.http import url_has_allowed_host_and_scheme
from .forms import UserRegistrationForm, UserLoginForm, UserProfileUpdateForm, UserReportForm
from .models import Notification, User
from .utils import create_admin_notification


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

            if not user.is_superuser:
                if user.account_status == 'PENDING':
                    messages.error(
                        request,
                        'Your account is pending administrator approval. Please wait until your account has been reviewed.'
                    )
                    return redirect('login')
                
                if user.account_status == 'SUSPENDED':
                    messages.error(
                        request,
                        'Your account has been suspended. Please contact the PAWS CONNECT administrator for further assistance.'
                    )
                    return redirect('login')
                
                if user.account_status == 'REJECTED':
                    messages.error(
                        request,
                        'Your account registration was rejected. Please contact the PAWS CONNECT administrator for further information.'
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

            create_admin_notification(
                notification_type='ACCOUNT_SAFETY_REPORT',
                title='New Account Safety Report',
                message=(
                    f'{request.user.username} reported {reported_user.username}. '
                    f'Reason: {user_report.get_reason_display()}.'
                ),
                target_url='/admin/accounts/userreport/'
            )

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

@login_required
def notifications_list_view(request):
    notifications = Notification.objects.filter(
        user=request.user
    ).order_by('-created_at')

    unread_count = notifications.filter(is_read=False).count()

    return render(request, 'accounts/notifications.html', {
        'notifications': notifications,
        'unread_count': unread_count,
    })


@login_required
def mark_notification_read_view(request, notification_id):
    notification = get_object_or_404(
        Notification,
        id=notification_id,
        user=request.user
    )

    notification.is_read = True
    notification.save()

    if notification.target_url:
        return redirect(notification.target_url)

    return redirect('notifications')


@login_required
def mark_all_notifications_read_view(request):
    Notification.objects.filter(
        user=request.user,
        is_read=False
    ).update(is_read=True)

    messages.success(request, 'All notifications marked as read.')

    return redirect('notifications')