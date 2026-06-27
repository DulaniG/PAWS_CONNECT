from django.contrib import admin
from .models import Report, RescueUpdate, Animal, AdoptionRequest


class RescueUpdateInline(admin.TabularInline):
    model = RescueUpdate
    extra = 0
    readonly_fields = ('created_at',)


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'animal_type',
        'condition',
        'suggested_priority',
        'priority',
        'verification_status',
        'report_status',
        'current_rescue_status',
        'reporter',
        'assigned_shelter',
        'assigned_rescuer',
        'reported_at',
    )

    list_filter = (
        'animal_type',
        'condition',
        'suggested_priority',
        'priority',
        'verification_status',
        'report_status',
        'current_rescue_status',
        'reported_at',
    )

    search_fields = (
        'description',
        'location_description',
        'reporter__username',
        'reporter__full_name',
        'assigned_rescuer__username',
        'assigned_rescuer__full_name',
    )

    readonly_fields = (
        'suggested_priority',
        'reported_at',
        'updated_at',
        'verified_at',
        'assigned_at',
    )

    ordering = ('-reported_at',)

    inlines = [RescueUpdateInline]


@admin.register(RescueUpdate)
class RescueUpdateAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'report',
        'rescuer',
        'status',
        'created_at',
    )

    list_filter = (
        'status',
        'created_at',
    )

    search_fields = (
        'update_text',
        'rescuer__username',
        'rescuer__full_name',
    )

    readonly_fields = ('created_at',)

    ordering = ('-created_at',)


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'display_animal',
        'shelter',
        'assigned_rescuer',
        'treatment_status',
        'arrival_date',
        'adoption_ready_date',
        'outcome_date',
        'created_at',
    )

    list_filter = (
        'treatment_status',
        'gender',
        'arrival_date',
        'adoption_ready_date',
        'outcome_date',
        'created_at',
    )

    search_fields = (
        'name',
        'age',
        'health_status',
        'treatment_notes',
        'vet_info',
        'report__description',
        'report__location_description',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
        'adoption_ready_date',
        'outcome_date',
    )

    ordering = ('-created_at',)

    def display_animal(self, obj):
        if obj.name:
            return obj.name

        return obj.report.get_animal_type_display()

    display_animal.short_description = 'Animal'


@admin.register(AdoptionRequest)
class AdoptionRequestAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'animal',
        'requester',
        'status',
        'processed_by',
        'created_at',
        'processed_at',
    )

    list_filter = (
        'status',
        'created_at',
        'processed_at',
    )

    search_fields = (
        'message',
        'decision_notes',
        'requester__username',
        'requester__full_name',
        'animal__name',
        'animal__report__description',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
        'processed_at',
    )

    ordering = ('-created_at',)