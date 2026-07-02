from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils import timezone

from .models import User, UserReport, Notification


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        'id',
        'username',
        'full_name',
        'email',
        'role',
        'account_status',
        'linked_shelter',
        'is_active',
        'is_staff',
        'date_joined',
    )

    list_filter = (
        'role',
        'account_status',
        'is_active',
        'is_staff',
        'is_superuser',
        'date_joined',
    )

    search_fields = (
        'username',
        'full_name',
        'email',
        'phone_number',
        'service_area',
        'shelter_address',
    )

    ordering = ('-date_joined',)

    fieldsets = UserAdmin.fieldsets + (
        (
            'PAWS CONNECT Account Details',
            {
                'fields': (
                    'full_name',
                    'phone_number',
                    'role',
                    'account_status',
                    'service_area',
                    'shelter_address',
                    'shelter_map_link',
                    'linked_shelter',
                )
            }
        ),
    )

    actions = [
        'approve_accounts',
        'reject_accounts',
        'suspend_accounts',
    ]

    def approve_accounts(self, request, queryset):
        updated_count = 0

        for user in queryset:
            user.account_status = 'APPROVED'
            user.is_active = True
            user.save()
            user.send_account_status_email()
            updated_count += 1

        self.message_user(
            request,
            f'{updated_count} account(s) approved successfully.'
        )

    approve_accounts.short_description = 'Approve selected accounts'

    def reject_accounts(self, request, queryset):
        updated_count = 0

        for user in queryset:
            user.account_status = 'REJECTED'
            user.is_active = False
            user.save()
            user.send_account_status_email()
            updated_count += 1

        self.message_user(
            request,
            f'{updated_count} account(s) rejected successfully.'
        )

    reject_accounts.short_description = 'Reject selected accounts'

    def suspend_accounts(self, request, queryset):
        updated_count = 0

        for user in queryset:
            user.account_status = 'SUSPENDED'
            user.is_active = False
            user.save()
            user.send_account_status_email()
            updated_count += 1

        self.message_user(
            request,
            f'{updated_count} account(s) suspended successfully.'
        )

    suspend_accounts.short_description = 'Suspend selected accounts'


@admin.register(UserReport)
class UserReportAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'reported_user',
        'reported_user_role',
        'reported_by',
        'reported_by_role',
        'reason',
        'status',
        'created_at',
        'reviewed_by',
        'reviewed_at',
    )

    list_filter = (
        'status',
        'reason',
        'reported_user__role',
        'reported_by__role',
        'created_at',
        'reviewed_at',
    )

    search_fields = (
        'reported_user__username',
        'reported_user__full_name',
        'reported_user__email',
        'reported_by__username',
        'reported_by__full_name',
        'description',
        'admin_notes',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
        'reviewed_at',
    )

    fieldsets = (
        (
            'Report Information',
            {
                'fields': (
                    'reported_by',
                    'reported_user',
                    'reason',
                    'description',
                    'related_page',
                    'created_at',
                    'updated_at',
                )
            }
        ),
        (
            'Admin Review',
            {
                'fields': (
                    'status',
                    'admin_notes',
                    'reviewed_by',
                    'reviewed_at',
                )
            }
        ),
    )

    ordering = ('-created_at',)

    actions = [
        'mark_as_reviewed',
        'mark_as_action_taken',
        'mark_as_dismissed',
        'suspend_reported_users',
    ]

    def reported_user_role(self, obj):
        return obj.reported_user.get_role_display()

    reported_user_role.short_description = 'Reported User Role'

    def reported_by_role(self, obj):
        return obj.reported_by.get_role_display()

    reported_by_role.short_description = 'Reported By Role'

    def mark_as_reviewed(self, request, queryset):
        updated_count = queryset.update(
            status='REVIEWED',
            reviewed_by=request.user,
            reviewed_at=timezone.now()
        )

        self.message_user(
            request,
            f'{updated_count} report(s) marked as reviewed.'
        )

    mark_as_reviewed.short_description = 'Mark selected reports as reviewed'

    def mark_as_action_taken(self, request, queryset):
        updated_count = queryset.update(
            status='ACTION_TAKEN',
            reviewed_by=request.user,
            reviewed_at=timezone.now()
        )

        self.message_user(
            request,
            f'{updated_count} report(s) marked as action taken.'
        )

    mark_as_action_taken.short_description = 'Mark selected reports as action taken'

    def mark_as_dismissed(self, request, queryset):
        updated_count = queryset.update(
            status='DISMISSED',
            reviewed_by=request.user,
            reviewed_at=timezone.now()
        )

        self.message_user(
            request,
            f'{updated_count} report(s) dismissed.'
        )

    mark_as_dismissed.short_description = 'Dismiss selected reports'

    def suspend_reported_users(self, request, queryset):
        suspended_count = 0

        for user_report in queryset:
            reported_user = user_report.reported_user
            reported_user.account_status = 'SUSPENDED'
            reported_user.is_active = False
            reported_user.save()
            reported_user.send_account_status_email()

            user_report.status = 'ACTION_TAKEN'
            user_report.reviewed_by = request.user
            user_report.reviewed_at = timezone.now()

            if not user_report.admin_notes:
                user_report.admin_notes = 'Reported account suspended by administrator.'

            user_report.save()
            suspended_count += 1

        self.message_user(
            request,
            f'{suspended_count} reported user account(s) suspended successfully.'
        )

    suspend_reported_users.short_description = 'Suspend reported users'

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'notification_type',
        'title',
        'is_read',
        'created_at',
    )

    list_filter = (
        'notification_type',
        'is_read',
        'created_at',
    )

    search_fields = (
        'user__username',
        'user__full_name',
        'title',
        'message',
    )

    readonly_fields = (
        'created_at',
    )

    ordering = ('-created_at',)
