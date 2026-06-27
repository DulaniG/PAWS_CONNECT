from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .forms import (
    ReportForm,
    ReportReviewForm,
    RescueAssignmentForm,
    RescueUpdateForm,
    AnimalTreatmentForm,
    AdoptionRequestForm,
    AdoptionDecisionForm,
)
from .models import Report, Animal, AdoptionRequest


@login_required
def report_animal_view(request):
    if request.user.role == 'ADMIN':
        messages.error(request, 'Administrators do not submit animal reports from this page.')
        return redirect('dashboard')

    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)

        if form.is_valid():
            report = form.save(commit=False)
            report.reporter = request.user
            report.save()

            messages.success(
                request,
                f'Animal report submitted successfully. Suggested priority: {report.get_suggested_priority_display()}. A shelter will review the report and set the final priority.'
            )

            return redirect('my_reports')
    else:
        initial_data = {}

        if request.user.phone_number:
            initial_data['reporter_contact_phone'] = request.user.phone_number

        form = ReportForm(initial=initial_data)

    return render(request, 'rescue/report_animal.html', {'form': form})


@login_required
def my_reports_view(request):
    reports = Report.objects.filter(reporter=request.user).order_by('-reported_at')

    return render(request, 'rescue/my_reports.html', {
        'reports': reports
    })


@login_required
def my_report_detail_view(request, report_id):
    report = get_object_or_404(
        Report,
        id=report_id,
        reporter=request.user
    )

    rescue_updates = report.rescue_updates.all().order_by('-created_at')

    animal = None
    try:
        animal = report.animal
    except Animal.DoesNotExist:
        animal = None

    return render(request, 'rescue/my_report_detail.html', {
        'report': report,
        'rescue_updates': rescue_updates,
        'animal': animal,
    })


@login_required
def shelter_report_list_view(request):
    if request.user.role != 'SHELTER':
        messages.error(request, 'Only shelter users can review animal reports.')
        return redirect('dashboard')

    reports = Report.objects.all().order_by('-reported_at')

    return render(request, 'rescue/shelter_report_list.html', {
        'reports': reports
    })


@login_required
def shelter_report_detail_view(request, report_id):
    if request.user.role != 'SHELTER':
        messages.error(request, 'Only shelter users can review animal reports.')
        return redirect('dashboard')

    report = get_object_or_404(Report, id=report_id)

    if request.method == 'POST':
        form = ReportReviewForm(request.POST, instance=report)

        if form.is_valid():
            reviewed_report = form.save(commit=False)
            reviewed_report.assigned_shelter = request.user
            reviewed_report.verified_at = timezone.now()

            if reviewed_report.verification_status in ['ANIMAL_NOT_FOUND', 'ALREADY_RESCUED']:
                reviewed_report.report_status = 'CLOSED'
            else:
                reviewed_report.report_status = 'REVIEWED'

            reviewed_report.save()

            messages.success(
                request,
                'Report reviewed successfully. Final priority and verification status have been saved.'
            )

            return redirect('shelter_report_list')
    else:
        form = ReportReviewForm(instance=report)

    assignment_form = RescueAssignmentForm(
        instance=report,
        shelter_user=request.user
    )

    rescue_updates = report.rescue_updates.all().order_by('-created_at')

    animal = None
    try:
        animal = report.animal
    except Animal.DoesNotExist:
        animal = None

    return render(request, 'rescue/shelter_report_detail.html', {
        'report': report,
        'form': form,
        'assignment_form': assignment_form,
        'rescue_updates': rescue_updates,
        'animal': animal,
    })


@login_required
def assign_rescuer_view(request, report_id):
    if request.user.role != 'SHELTER':
        messages.error(request, 'Only shelter users can assign rescuers.')
        return redirect('dashboard')

    report = get_object_or_404(Report, id=report_id)

    if not report.priority:
        messages.error(request, 'Final priority must be set before assigning a rescuer.')
        return redirect('shelter_report_detail', report_id=report.id)

    if report.verification_status != 'CONFIRMED_STILL_THERE':
        messages.error(
            request,
            'Animal must be verified as Confirmed Still There before assigning a rescuer.'
        )
        return redirect('shelter_report_detail', report_id=report.id)

    if request.method == 'POST':
        assignment_form = RescueAssignmentForm(
            request.POST,
            instance=report,
            shelter_user=request.user
        )

        if assignment_form.is_valid():
            assigned_report = assignment_form.save(commit=False)
            assigned_report.assigned_shelter = request.user
            assigned_report.report_status = 'ASSIGNED'
            assigned_report.assigned_at = timezone.now()
            assigned_report.save()

            messages.success(
                request,
                f'Report assigned successfully to {assigned_report.assigned_rescuer.full_name or assigned_report.assigned_rescuer.username}.'
            )

            return redirect('shelter_report_list')

    return redirect('shelter_report_detail', report_id=report.id)


@login_required
def rescuer_assigned_cases_view(request):
    if request.user.role != 'RESCUER':
        messages.error(request, 'Only rescuers can view assigned rescue cases.')
        return redirect('dashboard')

    reports = Report.objects.filter(
        assigned_rescuer=request.user
    ).exclude(
        current_rescue_status__in=[
            'HANDED_OVER_TO_SHELTER',
            'UNABLE_TO_LOCATE',
        ]
    ).select_related(
        'reporter',
        'assigned_shelter'
    ).order_by('-assigned_at', '-reported_at')

    return render(request, 'rescue/rescuer_assigned_cases.html', {
        'reports': reports
    })


@login_required
def rescuer_completed_cases_view(request):
    if request.user.role != 'RESCUER':
        messages.error(request, 'Only rescuers can view completed rescue cases.')
        return redirect('dashboard')

    reports = Report.objects.filter(
        assigned_rescuer=request.user,
        current_rescue_status__in=[
            'HANDED_OVER_TO_SHELTER',
            'UNABLE_TO_LOCATE',
        ]
    ).select_related(
        'reporter',
        'assigned_shelter'
    ).order_by('-updated_at', '-assigned_at', '-reported_at')

    return render(request, 'rescue/rescuer_completed_cases.html', {
        'reports': reports
    })


@login_required
def rescuer_case_detail_view(request, report_id):
    if request.user.role != 'RESCUER':
        messages.error(request, 'Only rescuers can update assigned rescue cases.')
        return redirect('dashboard')

    report = get_object_or_404(
        Report,
        id=report_id,
        assigned_rescuer=request.user
    )

    is_completed_case = report.current_rescue_status in [
        'HANDED_OVER_TO_SHELTER',
        'UNABLE_TO_LOCATE',
    ]

    animal = None
    try:
        animal = report.animal
    except Animal.DoesNotExist:
        animal = None

    if request.method == 'POST':
        if is_completed_case:
            messages.error(
                request,
                'This rescue case has already ended, so new rescue updates cannot be added.'
            )
            return redirect('rescuer_case_detail', report_id=report.id)

        form = RescueUpdateForm(request.POST, request.FILES)

        if form.is_valid():
            rescue_update = form.save(commit=False)
            rescue_update.report = report
            rescue_update.rescuer = request.user
            rescue_update.save()

            messages.success(
                request,
                f'Rescue status updated successfully to {rescue_update.get_status_display()}.'
            )

            return redirect('rescuer_case_detail', report_id=report.id)
    else:
        form = RescueUpdateForm()

    rescue_updates = report.rescue_updates.all().order_by('-created_at')

    return render(request, 'rescue/rescuer_case_detail.html', {
        'report': report,
        'form': form,
        'rescue_updates': rescue_updates,
        'animal': animal,
        'is_completed_case': is_completed_case,
    })


@login_required
def shelter_treatment_list_view(request):
    if request.user.role != 'SHELTER':
        messages.error(request, 'Only shelter users can access treatment tracking.')
        return redirect('dashboard')

    reports = Report.objects.filter(
        assigned_shelter=request.user,
        current_rescue_status='HANDED_OVER_TO_SHELTER'
    ).order_by('-updated_at')

    return render(request, 'rescue/shelter_treatment_list.html', {
        'reports': reports
    })


@login_required
def animal_treatment_detail_view(request, report_id):
    if request.user.role != 'SHELTER':
        messages.error(request, 'Only shelter users can manage treatment records.')
        return redirect('dashboard')

    report = get_object_or_404(
        Report,
        id=report_id,
        assigned_shelter=request.user
    )

    if report.current_rescue_status != 'HANDED_OVER_TO_SHELTER':
        messages.error(
            request,
            'Treatment tracking can start only after the rescue status is Handed Over to Shelter.'
        )
        return redirect('shelter_treatment_list')

    animal, created = Animal.objects.get_or_create(
        report=report,
        defaults={
            'shelter': request.user,
            'assigned_rescuer': report.assigned_rescuer,
            'arrival_date': timezone.localdate(),
            'treatment_status': 'UNDER_TREATMENT',
        }
    )

    if not animal.shelter:
        animal.shelter = request.user

    if not animal.assigned_rescuer:
        animal.assigned_rescuer = report.assigned_rescuer

    if not animal.arrival_date:
        animal.arrival_date = timezone.localdate()

    animal.save()

    if request.method == 'POST':
        form = AnimalTreatmentForm(request.POST, request.FILES, instance=animal)

        if form.is_valid():
            updated_animal = form.save(commit=False)
            updated_animal.shelter = request.user
            updated_animal.assigned_rescuer = report.assigned_rescuer
            updated_animal.save()

            messages.success(
                request,
                f'Treatment record saved successfully. Current status: {updated_animal.get_treatment_status_display()}.'
            )

            return redirect('animal_treatment_detail', report_id=report.id)
    else:
        form = AnimalTreatmentForm(instance=animal)

    rescue_updates = report.rescue_updates.all().order_by('-created_at')

    return render(request, 'rescue/animal_treatment_detail.html', {
        'report': report,
        'animal': animal,
        'form': form,
        'rescue_updates': rescue_updates,
        'created': created,
    })


@login_required
def adoption_home_view(request):
    if request.user.role == 'ADMIN':
        messages.error(request, 'Administrators do not submit adoption requests from this page.')
        return redirect('dashboard')

    return render(request, 'rescue/adoption_home.html')


@login_required
def available_animals_view(request):
    if request.user.role == 'ADMIN':
        messages.error(request, 'Administrators do not submit adoption requests from this page.')
        return redirect('dashboard')

    animals = Animal.objects.filter(
        treatment_status='READY_FOR_ADOPTION'
    ).select_related(
        'report',
        'shelter'
    ).order_by('-adoption_ready_date', '-updated_at')

    return render(request, 'rescue/available_animals.html', {
        'animals': animals
    })


@login_required
def animal_adoption_detail_view(request, animal_id):
    if request.user.role == 'ADMIN':
        messages.error(request, 'Administrators do not submit adoption requests from this page.')
        return redirect('dashboard')

    animal = get_object_or_404(
        Animal,
        id=animal_id,
        treatment_status='READY_FOR_ADOPTION'
    )

    existing_active_request = AdoptionRequest.objects.filter(
        animal=animal,
        requester=request.user,
        status__in=['PENDING', 'APPROVED']
    ).order_by('-created_at').first()

    if request.method == 'POST':
        if existing_active_request:
            messages.error(
                request,
                'You already have an active adoption request for this animal.'
            )
            return redirect('animal_adoption_detail', animal_id=animal.id)

        form = AdoptionRequestForm(request.POST)

        if form.is_valid():
            adoption_request = form.save(commit=False)
            adoption_request.animal = animal
            adoption_request.requester = request.user
            adoption_request.save()

            messages.success(
                request,
                'Adoption request submitted successfully. The shelter will review your request.'
            )

            return redirect('my_adoption_requests')
    else:
        form = AdoptionRequestForm()

    previous_requests = AdoptionRequest.objects.filter(
        animal=animal,
        requester=request.user
    ).order_by('-created_at')

    return render(request, 'rescue/animal_adoption_detail.html', {
        'animal': animal,
        'form': form,
        'existing_active_request': existing_active_request,
        'previous_requests': previous_requests,
    })


@login_required
def my_adoption_requests_view(request):
    if request.user.role == 'ADMIN':
        messages.error(request, 'Administrators do not submit adoption requests.')
        return redirect('dashboard')

    adoption_requests = AdoptionRequest.objects.filter(
        requester=request.user
    ).select_related(
        'animal',
        'animal__report',
        'animal__shelter'
    ).order_by('-created_at')

    return render(request, 'rescue/my_adoption_requests.html', {
        'adoption_requests': adoption_requests
    })


@login_required
def my_adoption_request_detail_view(request, request_id):
    if request.user.role == 'ADMIN':
        messages.error(request, 'Administrators do not submit adoption requests.')
        return redirect('dashboard')

    adoption_request = get_object_or_404(
        AdoptionRequest.objects.select_related(
            'animal',
            'animal__report',
            'animal__shelter',
            'requester',
            'processed_by'
        ),
        id=request_id,
        requester=request.user
    )

    return render(request, 'rescue/my_adoption_request_detail.html', {
        'adoption_request': adoption_request
    })


@login_required
def shelter_adoption_requests_view(request):
    if request.user.role != 'SHELTER':
        messages.error(request, 'Only shelter users can review adoption requests.')
        return redirect('dashboard')

    adoption_requests = AdoptionRequest.objects.filter(
        animal__shelter=request.user
    ).select_related(
        'animal',
        'animal__report',
        'requester'
    ).order_by('-created_at')

    return render(request, 'rescue/shelter_adoption_requests.html', {
        'adoption_requests': adoption_requests
    })


@login_required
def shelter_adoption_request_detail_view(request, request_id):
    if request.user.role != 'SHELTER':
        messages.error(request, 'Only shelter users can review adoption requests.')
        return redirect('dashboard')

    adoption_request = get_object_or_404(
        AdoptionRequest,
        id=request_id,
        animal__shelter=request.user
    )

    if request.method == 'POST':
        if adoption_request.status != 'PENDING':
            messages.error(request, 'This adoption request has already been processed.')
            return redirect('shelter_adoption_request_detail', request_id=adoption_request.id)

        form = AdoptionDecisionForm(request.POST, instance=adoption_request)

        if form.is_valid():
            updated_request = form.save(commit=False)
            updated_request.processed_by = request.user
            updated_request.processed_at = timezone.now()
            updated_request.save()

            animal = updated_request.animal

            if updated_request.status == 'APPROVED':
                if animal.treatment_status != 'READY_FOR_ADOPTION':
                    messages.error(
                        request,
                        'This animal is no longer ready for adoption.'
                    )
                    return redirect('shelter_adoption_request_detail', request_id=adoption_request.id)

                animal.treatment_status = 'ADOPTED'

                if updated_request.decision_notes:
                    animal.outcome_notes = updated_request.decision_notes
                else:
                    animal.outcome_notes = (
                        f'Adoption approved for {updated_request.requester.full_name or updated_request.requester.username}.'
                    )

                animal.save()

                AdoptionRequest.objects.filter(
                    animal=animal,
                    status='PENDING'
                ).exclude(
                    id=updated_request.id
                ).update(
                    status='REJECTED',
                    processed_by=request.user,
                    processed_at=timezone.now(),
                    decision_notes='Another adoption request was approved for this animal.'
                )

                messages.success(
                    request,
                    'Adoption request approved successfully. Animal status changed to Adopted.'
                )

            elif updated_request.status == 'REJECTED':
                messages.success(
                    request,
                    'Adoption request rejected successfully.'
                )

            return redirect('shelter_adoption_requests')
    else:
        form = AdoptionDecisionForm(instance=adoption_request)

    return render(request, 'rescue/shelter_adoption_request_detail.html', {
        'adoption_request': adoption_request,
        'form': form,
    })