from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.urls import reverse
from django.db.models import Q

from accounts.utils import create_notification, create_shelter_notifications

from .forms import (
    ReportForm,
    ReportReviewForm,
    RescueAssignmentForm,
    RescueUpdateForm,
    AnimalTreatmentForm,
    AdoptionRequestForm,
    AdoptionDecisionForm,
)
from .models import Report, RescueUpdate, Animal, AdoptionRequest


@login_required
def report_animal_view(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)

        if form.is_valid():
            report = form.save(commit=False)
            report.reporter = request.user

            if not report.reporter_contact_phone and request.user.phone_number:
                report.reporter_contact_phone = request.user.phone_number

            report.save()

            create_shelter_notifications(
                notification_type='REPORT_REVIEWED',
                title='New Animal Report Submitted',
                message=(
                    f'A new animal report has been submitted by '
                    f'{request.user.full_name or request.user.username}. '
                    f'Suggested priority: {report.get_suggested_priority_display()}.'
                ),
                target_url='/rescue/shelter/reports/'
            )

            messages.success(
                request,
                'Animal report submitted successfully. A shelter will review it soon.'
            )

            return redirect('my_reports')
    else:
        form = ReportForm()

    return render(request, 'rescue/report_animal.html', {
        'form': form,
    })


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

    rescue_updates = report.rescue_updates.all().order_by('created_at')

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
        messages.error(request, 'Only shelter users can view shelter reports.')
        return redirect('dashboard')

    completed_report_ids = Animal.objects.filter(
        treatment_status__in=['ADOPTED', 'PASSED_AWAY']
    ).values_list('report_id', flat=True)

    new_reports = Report.objects.filter(
        report_status='SUBMITTED'
    ).exclude(
        id__in=completed_report_ids
    ).order_by('-reported_at')

    reviewed_count = Report.objects.filter(
        assigned_shelter=request.user,
        report_status='REVIEWED'
    ).exclude(
        id__in=completed_report_ids
    ).count()

    assigned_count = Report.objects.filter(
        assigned_shelter=request.user,
        report_status='ASSIGNED'
    ).exclude(
        current_rescue_status__in=['HANDED_OVER_TO_SHELTER', 'UNABLE_TO_LOCATE']
    ).exclude(
        id__in=completed_report_ids
    ).count()

    handover_count = Report.objects.filter(
        assigned_shelter=request.user,
        current_rescue_status='HANDED_OVER_TO_SHELTER'
    ).exclude(
        id__in=completed_report_ids
    ).count()

    completed_count = Report.objects.filter(
        Q(assigned_shelter=request.user),
        Q(current_rescue_status='UNABLE_TO_LOCATE') |
        Q(animal__treatment_status__in=['ADOPTED', 'PASSED_AWAY'])
    ).count()

    return render(request, 'rescue/shelter_report_list.html', {
        'new_reports': new_reports,
        'reviewed_count': reviewed_count,
        'assigned_count': assigned_count,
        'handover_count': handover_count,
        'completed_count': completed_count,
    })


@login_required
def shelter_reviewed_reports_view(request):
    if request.user.role != 'SHELTER':
        messages.error(request, 'Only shelter users can view reviewed reports.')
        return redirect('dashboard')

    completed_report_ids = Animal.objects.filter(
        treatment_status__in=['ADOPTED', 'PASSED_AWAY']
    ).values_list('report_id', flat=True)

    reports = Report.objects.filter(
        assigned_shelter=request.user,
        report_status='REVIEWED'
    ).exclude(
        id__in=completed_report_ids
    ).select_related(
        'reporter',
        'assigned_rescuer'
    ).order_by('-updated_at')

    return render(request, 'rescue/shelter_stage_reports.html', {
        'reports': reports,
        'stage_title': 'Reviewed Reports Waiting for Assignment',
        'stage_description': 'Reports that have been reviewed by the shelter but have not yet been assigned to a rescuer.',
        'stage_badge': 'Reviewed',
        'stage_key': 'reviewed',
        'empty_message': 'No reviewed reports are waiting for assignment.',
    })


@login_required
def shelter_assigned_reports_view(request):
    if request.user.role != 'SHELTER':
        messages.error(request, 'Only shelter users can view assigned rescue cases.')
        return redirect('dashboard')

    completed_report_ids = Animal.objects.filter(
        treatment_status__in=['ADOPTED', 'PASSED_AWAY']
    ).values_list('report_id', flat=True)

    reports = Report.objects.filter(
        assigned_shelter=request.user,
        report_status='ASSIGNED'
    ).exclude(
        current_rescue_status__in=['HANDED_OVER_TO_SHELTER', 'UNABLE_TO_LOCATE']
    ).exclude(
        id__in=completed_report_ids
    ).select_related(
        'reporter',
        'assigned_rescuer'
    ).order_by('-assigned_at')

    return render(request, 'rescue/shelter_stage_reports.html', {
        'reports': reports,
        'stage_title': 'Assigned Rescue Cases In Progress',
        'stage_description': 'Rescue cases that have already been assigned to a rescuer and are still active.',
        'stage_badge': 'Assigned',
        'stage_key': 'assigned',
        'empty_message': 'No assigned rescue cases are currently in progress.',
    })


@login_required
def shelter_handover_reports_view(request):
    if request.user.role != 'SHELTER':
        messages.error(request, 'Only shelter users can view handover and treatment cases.')
        return redirect('dashboard')

    completed_report_ids = Animal.objects.filter(
        treatment_status__in=['ADOPTED', 'PASSED_AWAY']
    ).values_list('report_id', flat=True)

    reports = Report.objects.filter(
        assigned_shelter=request.user,
        current_rescue_status='HANDED_OVER_TO_SHELTER'
    ).exclude(
        id__in=completed_report_ids
    ).select_related(
        'reporter',
        'assigned_rescuer',
        'animal'
    ).order_by('-updated_at')

    return render(request, 'rescue/shelter_stage_reports.html', {
        'reports': reports,
        'stage_title': 'Handed Over / Treatment Stage',
        'stage_description': 'Cases where the animal has been handed over to the shelter and treatment/adoption preparation may continue.',
        'stage_badge': 'Handed Over',
        'stage_key': 'handover',
        'empty_message': 'No handed-over cases are currently waiting in treatment stage.',
    })


@login_required
def shelter_report_detail_view(request, report_id):
    if request.user.role != 'SHELTER':
        messages.error(request, 'Only shelter users can review reports.')
        return redirect('dashboard')

    report = get_object_or_404(Report, id=report_id)

    rescue_updates = report.rescue_updates.all().order_by('created_at')

    animal = None
    try:
        animal = report.animal
    except Animal.DoesNotExist:
        animal = None

    approved_adoption_request = None
    if animal:
        approved_adoption_request = animal.adoption_requests.filter(
            status='APPROVED'
        ).select_related(
            'requester',
            'processed_by'
        ).order_by(
            '-processed_at',
            '-updated_at'
        ).first()

    is_completed_case = (
        report.report_status == 'CLOSED'
        or report.current_rescue_status == 'UNABLE_TO_LOCATE'
        or (
            animal is not None
            and animal.treatment_status in ['ADOPTED', 'PASSED_AWAY']
        )
    )

    previous_verification_status = report.verification_status

    if request.method == 'POST':
        if is_completed_case:
            messages.warning(
                request,
                'This case is already completed, so review and assignment details can no longer be changed from this page.'
            )
            return redirect('shelter_report_detail', report_id=report.id)

        form = ReportReviewForm(request.POST, instance=report)

        if form.is_valid():
            reviewed_report = form.save(commit=False)
            reviewed_report.assigned_shelter = request.user

            if reviewed_report.report_status == 'SUBMITTED':
                reviewed_report.report_status = 'REVIEWED'

            if reviewed_report.verification_status != previous_verification_status:
                reviewed_report.verified_at = timezone.now()

            reviewed_report.save()

            create_notification(
                user=reviewed_report.reporter,
                notification_type='REPORT_REVIEWED',
                title='Animal Report Reviewed',
                message=(
                    f'Your animal report has been reviewed by '
                    f'{request.user.full_name or request.user.username}. '
                    f'Final priority: {reviewed_report.get_priority_display()}.'
                ),
                target_url=reverse('my_report_detail', args=[reviewed_report.id])
            )

            messages.success(request, 'Report reviewed successfully.')

            return redirect('shelter_report_detail', report_id=reviewed_report.id)
    else:
        form = ReportReviewForm(instance=report)

    assignment_form = RescueAssignmentForm(shelter_user=request.user)

    return render(request, 'rescue/shelter_report_detail.html', {
        'report': report,
        'form': form,
        'review_form': form,
        'assignment_form': assignment_form,
        'rescue_updates': rescue_updates,
        'animal': animal,
        'approved_adoption_request': approved_adoption_request,
        'is_completed_case': is_completed_case,
    })


@login_required
def assign_rescuer_view(request, report_id):
    if request.user.role != 'SHELTER':
        messages.error(request, 'Only shelter users can assign rescuers.')
        return redirect('dashboard')

    report = get_object_or_404(Report, id=report_id)

    if report.current_rescue_status in ['HANDED_OVER_TO_SHELTER', 'UNABLE_TO_LOCATE']:
        messages.warning(
            request,
            'This case can no longer be reassigned because the rescue case is no longer active.'
        )
        return redirect('shelter_report_detail', report_id=report.id)

    animal = None
    try:
        animal = report.animal
    except Animal.DoesNotExist:
        animal = None

    if animal and animal.treatment_status in ['ADOPTED', 'PASSED_AWAY']:
        messages.warning(
            request,
            'This case can no longer be reassigned because the animal case is already completed.'
        )
        return redirect('shelter_report_detail', report_id=report.id)

    if request.method == 'POST':
        form = RescueAssignmentForm(
            request.POST,
            shelter_user=request.user
        )

        if form.is_valid():
            assigned_rescuer = form.cleaned_data.get('assigned_rescuer')
            assignment_notes = form.cleaned_data.get('assignment_notes')

            previous_assigned_rescuer = report.assigned_rescuer

            if previous_assigned_rescuer == assigned_rescuer:
                messages.info(
                    request,
                    'This case is already assigned to this rescuer.'
                )
                return redirect('shelter_report_detail', report_id=report.id)

            is_reassignment = previous_assigned_rescuer is not None

            report.assigned_shelter = request.user
            report.assigned_rescuer = assigned_rescuer
            report.assignment_notes = assignment_notes
            report.report_status = 'ASSIGNED'
            report.current_rescue_status = 'NOT_STARTED'
            report.assigned_at = timezone.now()
            report.save()

            if is_reassignment:
                create_notification(
                    user=previous_assigned_rescuer,
                    notification_type='CASE_ASSIGNED',
                    title='Rescue Case Reassigned',
                    message=(
                        'This rescue case has been reassigned and removed from your active cases.'
                    ),
                    target_url=reverse('rescuer_assigned_cases')
                )

                create_notification(
                    user=assigned_rescuer,
                    notification_type='CASE_ASSIGNED',
                    title='Rescue Case Assigned',
                    message=(
                        f'A rescue case has been assigned to you by '
                        f'{request.user.full_name or request.user.username}. '
                        f'Priority: {report.get_priority_display()}.'
                    ),
                    target_url=reverse('rescuer_case_detail', args=[report.id])
                )

                create_notification(
                    user=report.reporter,
                    notification_type='CASE_ASSIGNED',
                    title='Rescue Case Reassigned',
                    message=(
                        'Your animal rescue case has been reassigned to another rescuer. '
                        f'Current rescue status: {report.get_current_rescue_status_display()}.'
                    ),
                    target_url=reverse('my_report_detail', args=[report.id])
                )

                messages.success(
                    request,
                    f'Rescuer changed to {assigned_rescuer.full_name or assigned_rescuer.username} successfully.'
                )

            else:
                create_notification(
                    user=assigned_rescuer,
                    notification_type='CASE_ASSIGNED',
                    title='New Rescue Case Assigned',
                    message=(
                        f'A new rescue case has been assigned to you by '
                        f'{request.user.full_name or request.user.username}. '
                        f'Priority: {report.get_priority_display()}.'
                    ),
                    target_url=reverse('rescuer_case_detail', args=[report.id])
                )

                create_notification(
                    user=report.reporter,
                    notification_type='CASE_ASSIGNED',
                    title='Rescue Case Assigned',
                    message=(
                        'Your animal report has been assigned to a rescuer. '
                        f'Current rescue status: {report.get_current_rescue_status_display()}.'
                    ),
                    target_url=reverse('my_report_detail', args=[report.id])
                )

                messages.success(
                    request,
                    f'Rescuer {assigned_rescuer.full_name or assigned_rescuer.username} assigned successfully.'
                )

            return redirect('shelter_report_detail', report_id=report.id)

        messages.error(
            request,
            'Please select a linked approved rescuer and add assignment instructions before assigning the case.'
        )

    else:
        form = RescueAssignmentForm(shelter_user=request.user)

    return render(request, 'rescue/assign_rescuer.html', {
        'report': report,
        'form': form,
    })


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

            create_notification(
                user=report.reporter,
                notification_type='RESCUE_UPDATE',
                title='Rescue Status Updated',
                message=(
                    f'The rescue status for your animal report was updated to '
                    f'{rescue_update.get_status_display()}.'
                ),
                target_url=reverse('my_report_detail', args=[report.id])
            )

            if report.assigned_shelter:
                create_notification(
                    user=report.assigned_shelter,
                    notification_type='RESCUE_UPDATE',
                    title='Rescue Case Updated',
                    message=(
                        f'{request.user.full_name or request.user.username} updated the rescue case status to '
                        f'{rescue_update.get_status_display()}.'
                    ),
                    target_url=reverse('shelter_report_detail', args=[report.id])
                )

            messages.success(
                request,
                f'Rescue status updated successfully to {rescue_update.get_status_display()}.'
            )

            return redirect('rescuer_case_detail', report_id=report.id)
    else:
        form = RescueUpdateForm()

    rescue_updates = report.rescue_updates.all().order_by('created_at')

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
        assigned_shelter=request.user,
        current_rescue_status='HANDED_OVER_TO_SHELTER'
    )

    rescue_updates = report.rescue_updates.all().order_by('created_at')

    try:
        animal = report.animal
        created = False
    except Animal.DoesNotExist:
        animal = Animal(
            report=report,
            shelter=request.user,
            assigned_rescuer=report.assigned_rescuer
        )
        created = True

    if request.method == 'POST':
        form = AnimalTreatmentForm(
            request.POST,
            request.FILES,
            instance=animal
        )

        if form.is_valid():
            treatment_record = form.save(commit=False)
            treatment_record.report = report
            treatment_record.shelter = request.user
            treatment_record.assigned_rescuer = report.assigned_rescuer
            treatment_record.save()

            create_notification(
                user=report.reporter,
                notification_type='TREATMENT_UPDATE',
                title='Treatment Status Updated',
                message=(
                    f'The treatment status for your reported animal has been updated to '
                    f'{treatment_record.get_treatment_status_display()}.'
                ),
                target_url=reverse('my_report_detail', args=[report.id])
            )

            messages.success(
                request,
                'Animal treatment record saved successfully.'
            )

            return redirect('animal_treatment_detail', report_id=report.id)
    else:
        form = AnimalTreatmentForm(instance=animal)

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
        messages.error(request, 'Administrators cannot submit adoption requests.')
        return redirect('available_animals')

    animal = get_object_or_404(
        Animal,
        id=animal_id,
        treatment_status='READY_FOR_ADOPTION'
    )

    existing_request = AdoptionRequest.objects.filter(
        animal=animal,
        requester=request.user,
        status__in=['PENDING', 'APPROVED']
    ).first()

    if request.method == 'POST':
        if existing_request:
            messages.warning(
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

            create_notification(
                user=animal.shelter,
                notification_type='ADOPTION_REQUEST',
                title='New Adoption Request',
                message=(
                    f'{request.user.full_name or request.user.username} submitted an adoption request '
                    f'for {animal.name or animal.report.get_animal_type_display()}.'
                ),
                target_url=reverse('shelter_adoption_request_detail', args=[adoption_request.id])
            )

            messages.success(
                request,
                'Your adoption request has been submitted successfully.'
            )

            return redirect('my_adoption_request_detail', request_id=adoption_request.id)
    else:
        form = AdoptionRequestForm()

    return render(request, 'rescue/animal_adoption_detail.html', {
        'animal': animal,
        'form': form,
        'existing_request': existing_request,
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
        messages.error(request, 'Only shelter users can view adoption requests.')
        return redirect('dashboard')

    adoption_requests = AdoptionRequest.objects.filter(
        animal__shelter=request.user,
        status='PENDING'
    ).select_related(
        'animal',
        'animal__report',
        'requester'
    ).order_by('-created_at')

    return render(request, 'rescue/shelter_adoption_requests.html', {
        'adoption_requests': adoption_requests,
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
        form = AdoptionDecisionForm(
            request.POST,
            instance=adoption_request
        )

        if form.is_valid():
            decision = form.save(commit=False)
            decision.processed_by = request.user
            decision.processed_at = timezone.now()
            decision.save()

            animal = decision.animal

            if decision.status == 'APPROVED':
                animal.treatment_status = 'ADOPTED'

                if decision.decision_notes:
                    animal.outcome_notes = decision.decision_notes
                else:
                    animal.outcome_notes = 'Adoption request approved by shelter.'

                animal.save()

                other_pending_requests = AdoptionRequest.objects.filter(
                    animal=animal,
                    status='PENDING'
                ).exclude(id=decision.id)

                for other_request in other_pending_requests:
                    other_request.status = 'REJECTED'
                    other_request.processed_by = request.user
                    other_request.processed_at = timezone.now()
                    other_request.decision_notes = (
                        'This request was rejected because another adoption request was approved.'
                    )
                    other_request.save()

                    create_notification(
                        user=other_request.requester,
                        notification_type='ADOPTION_DECISION',
                        title='Adoption Request Rejected',
                        message=(
                            f'Your adoption request for {animal.name or animal.report.get_animal_type_display()} '
                            'was rejected because another request was approved.'
                        ),
                        target_url=reverse('my_adoption_request_detail', args=[other_request.id])
                    )

                create_notification(
                    user=decision.requester,
                    notification_type='ADOPTION_DECISION',
                    title='Adoption Request Approved',
                    message=(
                        f'Your adoption request for {animal.name or animal.report.get_animal_type_display()} '
                        'has been approved. Please open the request details to view adoption handover information.'
                    ),
                    target_url=reverse('my_adoption_request_detail', args=[decision.id])
                )

                messages.success(
                    request,
                    'Adoption request approved successfully. The animal has been marked as adopted.'
                )

            elif decision.status == 'REJECTED':
                create_notification(
                    user=decision.requester,
                    notification_type='ADOPTION_DECISION',
                    title='Adoption Request Rejected',
                    message=(
                        f'Your adoption request for {animal.name or animal.report.get_animal_type_display()} '
                        'has been rejected by the shelter.'
                    ),
                    target_url=reverse('my_adoption_request_detail', args=[decision.id])
                )

                messages.success(
                    request,
                    'Adoption request rejected successfully.'
                )

            return redirect('shelter_adoption_request_detail', request_id=decision.id)
    else:
        form = AdoptionDecisionForm(instance=adoption_request)

    return render(request, 'rescue/shelter_adoption_request_detail.html', {
        'adoption_request': adoption_request,
        'form': form,
    })

@login_required
def shelter_completed_cases_view(request):
    if request.user.role != 'SHELTER':
        messages.error(request, 'Only shelter users can view completed shelter cases.')
        return redirect('dashboard')

    completed_reports = Report.objects.filter(
        Q(assigned_shelter=request.user),
        Q(current_rescue_status='UNABLE_TO_LOCATE') |
        Q(animal__treatment_status__in=['ADOPTED', 'PASSED_AWAY'])
    ).select_related(
        'reporter',
        'assigned_rescuer',
        'animal'
    ).order_by('-updated_at')

    return render(request, 'rescue/shelter_completed_cases.html', {
        'completed_reports': completed_reports,
    })