from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone


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

    full_name = models.CharField(
        max_length=150,
        blank=True
    )

    email = models.EmailField(
        unique=True
    )

    phone_number = models.CharField(
        max_length=20,
        blank=True
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='PUBLIC'
    )

    account_status = models.CharField(
        max_length=20,
        choices=ACCOUNT_STATUS_CHOICES,
        default='PENDING'
    )

    service_area = models.CharField(
        max_length=255,
        blank=True,
        help_text='For shelter accounts only. Example: Kottawa, Maharagama, Homagama.'
    )

    shelter_address = models.CharField(
        max_length=255,
        blank=True,
        help_text='For shelter accounts only. This is used as the shelter handover location.'
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
        help_text='For rescuer accounts only. The rescuer selects the shelter they are connected with.'
    )

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.role = 'ADMIN'
            self.account_status = 'APPROVED'
            self.linked_shelter = None

        if self.role != 'RESCUER':
            self.linked_shelter = None

        if self.role != 'SHELTER':
            self.service_area = ''
            self.shelter_address = ''
            self.shelter_map_link = ''

        super().save(*args, **kwargs)

    def send_account_status_email(self):
        if not self.email:
            return

        if self.account_status == 'APPROVED':
            subject = 'PAWS CONNECT Account Approved'
            message = (
                f'Hello {self.full_name or self.username},\n\n'
                'Your PAWS CONNECT account has been approved. '
                'You can now log in and use the system based on your assigned role.\n\n'
                'Thank you,\n'
                'PAWS CONNECT Team'
            )

        elif self.account_status == 'REJECTED':
            subject = 'PAWS CONNECT Account Rejected'
            message = (
                f'Hello {self.full_name or self.username},\n\n'
                'Your PAWS CONNECT account request has been rejected. '
                'Please contact the system administrator if you believe this is a mistake.\n\n'
                'Thank you,\n'
                'PAWS CONNECT Team'
            )

        elif self.account_status == 'SUSPENDED':
            subject = 'PAWS CONNECT Account Suspended'
            message = (
                f'Hello {self.full_name or self.username},\n\n'
                'Your PAWS CONNECT account has been suspended due to account safety or system policy concerns. '
                'Please contact the system administrator for more information.\n\n'
                'Thank you,\n'
                'PAWS CONNECT Team'
            )

        else:
            return

        send_mail(
            subject,
            message,
            None,
            [self.email],
            fail_silently=True
        )

    def __str__(self):
        if self.full_name:
            return f'{self.full_name} ({self.username})'

        return self.username


class UserReport(models.Model):
    REASON_CHOICES = [
        ('FAKE_ACCOUNT', 'Fake Account'),
        ('MISLEADING_INFORMATION', 'Misleading Information'),
        ('NOT_LINKED_TO_SHELTER', 'Not Actually Linked to Selected Shelter'),
        ('SUSPICIOUS_BEHAVIOUR', 'Suspicious Behaviour'),
        ('INAPPROPRIATE_BEHAVIOUR', 'Inappropriate Behaviour'),
        ('SCAM_OR_FRAUD', 'Scam or Fraud Concern'),
        ('OTHER', 'Other'),
    ]

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('REVIEWED', 'Reviewed'),
        ('ACTION_TAKEN', 'Action Taken'),
        ('DISMISSED', 'Dismissed'),
    ]

    reported_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='submitted_user_reports'
    )

    reported_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='received_user_reports'
    )

    reason = models.CharField(
        max_length=40,
        choices=REASON_CHOICES
    )

    description = models.TextField(
        help_text='Explain why this account is being reported.'
    )

    related_page = models.CharField(
        max_length=255,
        blank=True,
        help_text='Optional page or workflow where the suspicious activity was noticed.'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    admin_notes = models.TextField(
        blank=True,
        help_text='Admin notes after reviewing the report.'
    )

    reviewed_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='reviewed_user_reports',
        limit_choices_to={'role': 'ADMIN'}
    )

    reviewed_at = models.DateTimeField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'User Safety Report'
        verbose_name_plural = 'User Safety Reports'

    def mark_reviewed(self, admin_user=None):
        self.status = 'REVIEWED'
        self.reviewed_by = admin_user
        self.reviewed_at = timezone.now()
        self.save()

    def mark_action_taken(self, admin_user=None):
        self.status = 'ACTION_TAKEN'
        self.reviewed_by = admin_user
        self.reviewed_at = timezone.now()
        self.save()

    def mark_dismissed(self, admin_user=None):
        self.status = 'DISMISSED'
        self.reviewed_by = admin_user
        self.reviewed_at = timezone.now()
        self.save()

    def __str__(self):
        return f'Report against {self.reported_user.username} by {self.reported_by.username}'