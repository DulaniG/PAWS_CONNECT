from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ('PUBLIC', 'Public User'),
        ('RESCUER', 'Rescuer'),
        ('SHELTER', 'Shelter'),
        ('ADMIN', 'Administrator'),
    ]

    ACCOUNT_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
        ('SUSPENDED', 'Suspended'),
    ]

    full_name = models.CharField(max_length=150)

    email = models.EmailField(unique=True)

    phone_number = models.CharField(max_length=20, blank=True)

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='PUBLIC'
    )

    account_status = models.CharField(
        max_length=20,
        choices=ACCOUNT_STATUS_CHOICES,
        default='APPROVED'
    )

    service_area = models.CharField(
        max_length=100,
        blank=True,
        help_text='Required for shelter accounts. Example: Colombo, Kottawa, Maharagama.'
    )

    shelter_address = models.CharField(
        max_length=255,
        blank=True,
        help_text='Required for shelter accounts. This is the default handover location for rescued animals.'
    )

    shelter_map_link = models.URLField(
        blank=True,
        help_text='Optional Google Maps or Apple Maps link for the shelter handover location.'
    )

    linked_shelter = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='linked_rescuers',
        limit_choices_to={'role': 'SHELTER'},
        verbose_name='Linked Shelter',
        help_text='For rescuer accounts only. Admin verifies and links the rescuer to a shelter.'
    )

    def send_account_status_email(self):
        if not self.email or self.is_superuser:
            return

        status_messages = {
            'APPROVED': {
                'subject': 'PAWS CONNECT Account Approved',
                'message': (
                    f'Dear {self.full_name or self.username},\n\n'
                    'Your PAWS CONNECT account has been approved by the administrator.\n\n'
                    'You can now login and access your dashboard.\n\n'
                    'Thank you,\n'
                    'PAWS CONNECT Team'
                ),
            },
            'REJECTED': {
                'subject': 'PAWS CONNECT Account Rejected',
                'message': (
                    f'Dear {self.full_name or self.username},\n\n'
                    'Your PAWS CONNECT account registration has been rejected by the administrator.\n\n'
                    'Please contact the system administrator if you need more information.\n\n'
                    'Thank you,\n'
                    'PAWS CONNECT Team'
                ),
            },
            'SUSPENDED': {
                'subject': 'PAWS CONNECT Account Suspended',
                'message': (
                    f'Dear {self.full_name or self.username},\n\n'
                    'Your PAWS CONNECT account has been suspended by the administrator.\n\n'
                    'Please contact the system administrator if you need more information.\n\n'
                    'Thank you,\n'
                    'PAWS CONNECT Team'
                ),
            },
        }

        email_content = status_messages.get(self.account_status)

        if email_content:
            send_mail(
                subject=email_content['subject'],
                message=email_content['message'],
                from_email=None,
                recipient_list=[self.email],
                fail_silently=True,
            )

    def save(self, *args, **kwargs):
        old_account_status = None

        if self.pk:
            try:
                old_user = User.objects.get(pk=self.pk)
                old_account_status = old_user.account_status
            except User.DoesNotExist:
                old_account_status = None

        if self.is_superuser:
            self.role = 'ADMIN'
            self.account_status = 'APPROVED'
            self.linked_shelter = None

        if self.role != 'RESCUER':
            self.linked_shelter = None

        super().save(*args, **kwargs)

        if old_account_status and old_account_status != self.account_status:
            self.send_account_status_email()

    def __str__(self):
        return f"{self.full_name or self.username} - {self.role}"