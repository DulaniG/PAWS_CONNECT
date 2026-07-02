from .models import Notification, User


def create_notification(user, notification_type, title, message, target_url=''):
    if not user:
        return None

    if not user.is_active:
        return None

    notification = Notification.objects.create(
        user=user,
        notification_type=notification_type,
        title=title,
        message=message,
        target_url=target_url
    )

    return notification


def create_admin_notification(notification_type, title, message, target_url=''):
    admin_users = User.objects.filter(
        role='ADMIN',
        account_status='APPROVED',
        is_active=True
    )

    created_notifications = []

    for admin_user in admin_users:
        notification = create_notification(
            user=admin_user,
            notification_type=notification_type,
            title=title,
            message=message,
            target_url=target_url
        )

        if notification:
            created_notifications.append(notification)

    return created_notifications


def create_shelter_notifications(notification_type, title, message, target_url=''):
    shelter_users = User.objects.filter(
        role='SHELTER',
        account_status='APPROVED',
        is_active=True
    )

    created_notifications = []

    for shelter_user in shelter_users:
        notification = create_notification(
            user=shelter_user,
            notification_type=notification_type,
            title=title,
            message=message,
            target_url=target_url
        )

        if notification:
            created_notifications.append(notification)

    return created_notifications