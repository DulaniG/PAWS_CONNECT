from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.action(description='Approve selected accounts')
def approve_accounts(modeladmin, request, queryset):
    updated_count = 0

    for user in queryset:
        user.account_status = 'APPROVED'
        user.save()
        updated_count += 1

    modeladmin.message_user(
        request,
        f'{updated_count} account(s) approved successfully.',
        messages.SUCCESS
    )


@admin.action(description='Reject selected accounts')
def reject_accounts(modeladmin, request, queryset):
    updated_count = 0

    for user in queryset:
        user.account_status = 'REJECTED'
        user.save()
        updated_count += 1

    modeladmin.message_user(
        request,
        f'{updated_count} account(s) rejected successfully.',
        messages.WARNING
    )


@admin.action(description='Suspend selected accounts')
def suspend_accounts(modeladmin, request, queryset):
    updated_count = 0

    for user in queryset:
        user.account_status = 'SUSPENDED'
        user.save()
        updated_count += 1

    modeladmin.message_user(
        request,
        f'{updated_count} account(s) suspended successfully.',
        messages.WARNING
    )


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User

    list_display = (
        'username',
        'email',
        'full_name',
        'role',
        'account_status',
        'service_area',
        'linked_shelter',
        'is_staff',
        'is_active',
    )

    list_filter = (
        'role',
        'account_status',
        'is_staff',
        'is_active',
    )

    search_fields = (
        'username',
        'email',
        'full_name',
        'phone_number',
        'service_area',
        'shelter_address',
    )

    ordering = ('username',)

    list_editable = (
        'role',
        'account_status',
    )

    actions = [
        approve_accounts,
        reject_accounts,
        suspend_accounts,
    ]

    fieldsets = UserAdmin.fieldsets + (
        ('PAWS CONNECT User Details', {
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
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('PAWS CONNECT User Details', {
            'fields': (
                'full_name',
                'email',
                'phone_number',
                'role',
                'account_status',
                'service_area',
                'shelter_address',
                'shelter_map_link',
                'linked_shelter',
            )
        }),
    )