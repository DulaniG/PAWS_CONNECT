from django.conf import settings
from django.db import models
from django.utils import timezone


class Report(models.Model):
    ANIMAL_TYPE_CHOICES = [
        ('DOG', 'Dog'),
        ('CAT', 'Cat'),
        ('BIRD', 'Bird'),
        ('OTHER', 'Other'),
    ]

    CONDITION_CHOICES = [
        ('SEVERE_INJURY', 'Severe Injury'),
        ('ROAD_ACCIDENT', 'Road Accident'),
        ('BLEEDING', 'Bleeding'),
        ('SICK', 'Sick'),
        ('MINOR_INJURY', 'Minor Injury'),
        ('ABANDONED', 'Abandoned'),
        ('LOST', 'Lost'),
        ('OTHER', 'Other'),
    ]

    PRIORITY_CHOICES = [
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    ]

    STATUS_CHOICES = [
        ('SUBMITTED', 'Submitted'),
        ('REVIEWED', 'Reviewed'),
        ('ASSIGNED', 'Assigned'),
        ('CLOSED', 'Closed'),
    ]

    VERIFICATION_STATUS_CHOICES = [
        ('PENDING_VERIFICATION', 'Pending Verification'),
        ('CONFIRMED_STILL_THERE', 'Confirmed Still There'),
        ('ANIMAL_NOT_FOUND', 'Animal Not Found'),
        ('ALREADY_RESCUED', 'Already Rescued (Confirmed by Reporter)'),
    ]

    RESCUE_STATUS_CHOICES = [
        ('NOT_STARTED', 'Not Started'),
        ('ON_THE_WAY', 'On the Way'),
        ('RESCUED', 'Rescued'),
        ('UNABLE_TO_LOCATE', 'Unable to Locate'),
        ('HANDED_OVER_TO_SHELTER', 'Handed Over to Shelter'),
    ]

    reporter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='submitted_reports'
    )

    reporter_contact_phone = models.CharField(
        max_length=20,
        blank=True,
        help_text='Required when submitting a report so the shelter can verify the animal location.'
    )

    animal_type = models.CharField(max_length=20, choices=ANIMAL_TYPE_CHOICES)

    other_animal_type = models.CharField(
        max_length=100,
        blank=True,
        help_text='Required only when animal type is Other.'
    )

    condition = models.CharField(max_length=30, choices=CONDITION_CHOICES)

    description = models.TextField(
        help_text='Describe the animal condition and situation.'
    )

    image = models.ImageField(
        upload_to='report_images/',
        blank=True,
        null=True
    )

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True
    )

    location_description = models.CharField(
        max_length=255,
        help_text='Example: Near Kottawa bus stand, beside the main road.'
    )

    map_link = models.URLField(
        blank=True,
        help_text='Optional pasted Google Maps or Apple Maps link.'
    )

    suggested_priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='LOW'
    )

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        blank=True,
        help_text='Final priority is selected manually by shelter.'
    )

    verification_status = models.CharField(
        max_length=30,
        choices=VERIFICATION_STATUS_CHOICES,
        default='PENDING_VERIFICATION'
    )

    verification_notes = models.TextField(
        blank=True,
        help_text='Notes from shelter after contacting the reporter.'
    )

    verified_at = models.DateTimeField(blank=True, null=True)

    report_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='SUBMITTED'
    )

    current_rescue_status = models.CharField(
        max_length=30,
        choices=RESCUE_STATUS_CHOICES,
        default='NOT_STARTED'
    )

    assigned_shelter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='assigned_reports',
        limit_choices_to={'role': 'SHELTER'}
    )

    assigned_rescuer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='rescuer_assigned_reports',
        limit_choices_to={'role': 'RESCUER'}
    )

    assignment_notes = models.TextField(
        blank=True,
        help_text='Rescue and handover instructions for the assigned rescuer.'
    )

    assigned_at = models.DateTimeField(blank=True, null=True)

    reported_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def calculate_suggested_priority(self):
        high_priority_conditions = [
            'SEVERE_INJURY',
            'ROAD_ACCIDENT',
            'BLEEDING',
        ]

        medium_priority_conditions = [
            'SICK',
            'MINOR_INJURY',
        ]

        if self.condition in high_priority_conditions:
            return 'HIGH'

        if self.condition in medium_priority_conditions:
            return 'MEDIUM'

        return 'LOW'

    def save(self, *args, **kwargs):
        self.suggested_priority = self.calculate_suggested_priority()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.get_animal_type_display()} report by {self.reporter.username}'


class RescueUpdate(models.Model):
    RESCUE_UPDATE_STATUS_CHOICES = [
        ('ON_THE_WAY', 'On the Way'),
        ('RESCUED', 'Rescued'),
        ('UNABLE_TO_LOCATE', 'Unable to Locate'),
        ('HANDED_OVER_TO_SHELTER', 'Handed Over to Shelter'),
    ]

    report = models.ForeignKey(
        Report,
        on_delete=models.CASCADE,
        related_name='rescue_updates'
    )

    rescuer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='rescue_updates'
    )

    status = models.CharField(
        max_length=30,
        choices=RESCUE_UPDATE_STATUS_CHOICES
    )

    update_text = models.TextField(
        help_text='Write the rescue progress update.'
    )

    photo = models.ImageField(
        upload_to='rescue_update_photos/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self.report.current_rescue_status = self.status

        if self.status in ['ON_THE_WAY', 'RESCUED']:
            self.report.report_status = 'ASSIGNED'
            
        if self.status in ['UNABLE_TO_LOCATE', 'HANDED_OVER_TO_SHELTER']:
            self.report.report_status = 'CLOSED'

        self.report.save()

    def __str__(self):
        return f'{self.get_status_display()} - {self.report}'


class Animal(models.Model):
    GENDER_CHOICES = [
        ('UNKNOWN', 'Unknown'),
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
    ]

    TREATMENT_STATUS_CHOICES = [
        ('UNDER_TREATMENT', 'Under Treatment'),
        ('RECOVERING', 'Recovering'),
        ('READY_FOR_ADOPTION', 'Ready for Adoption'),
        ('ADOPTED', 'Adopted'),
        ('PASSED_AWAY', 'Passed Away'),
    ]

    report = models.OneToOneField(
        Report,
        on_delete=models.CASCADE,
        related_name='animal'
    )

    shelter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='shelter_animals',
        limit_choices_to={'role': 'SHELTER'}
    )

    assigned_rescuer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='rescued_animals',
        limit_choices_to={'role': 'RESCUER'}
    )

    name = models.CharField(
        max_length=100,
        blank=True,
        help_text='Optional name given by the shelter.'
    )

    age = models.CharField(
        max_length=50,
        blank=True,
        help_text='Approximate age. Example: Puppy, Adult, 2 years, Unknown.'
    )

    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
        default='UNKNOWN'
    )

    animal_image = models.ImageField(
        upload_to='animal_images/',
        blank=True,
        null=True,
        help_text='Optional updated image after the animal reaches the shelter.'
    )

    health_status = models.TextField(
        blank=True,
        help_text='Current health condition of the animal.'
    )

    treatment_status = models.CharField(
        max_length=30,
        choices=TREATMENT_STATUS_CHOICES,
        default='UNDER_TREATMENT'
    )

    treatment_notes = models.TextField(
        blank=True,
        help_text='Treatment progress notes added by the shelter.'
    )

    vet_info = models.CharField(
        max_length=255,
        blank=True,
        help_text='Vet clinic or veterinarian details, if available.'
    )

    arrival_date = models.DateField(
        blank=True,
        null=True,
        help_text='Date the animal arrived at the shelter or treatment location.'
    )

    adoption_ready_date = models.DateField(
        blank=True,
        null=True,
        help_text='Date the animal became ready for adoption.'
    )

    outcome_date = models.DateField(
        blank=True,
        null=True,
        help_text='Date of final outcome, such as adoption or passing away.'
    )

    outcome_notes = models.TextField(
        blank=True,
        help_text='Optional notes about the final outcome of the case.'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.treatment_status == 'READY_FOR_ADOPTION' and not self.adoption_ready_date:
            self.adoption_ready_date = timezone.localdate()

        if self.treatment_status in ['ADOPTED', 'PASSED_AWAY'] and not self.outcome_date:
            self.outcome_date = timezone.localdate()

        super().save(*args, **kwargs)

    def __str__(self):
        if self.name:
            return f'{self.name} - {self.get_treatment_status_display()}'

        return f'{self.report.get_animal_type_display()} - {self.get_treatment_status_display()}'


class AdoptionRequest(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]

    animal = models.ForeignKey(
        Animal,
        on_delete=models.CASCADE,
        related_name='adoption_requests'
    )

    requester = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='adoption_requests'
    )

    message = models.TextField(
        help_text='Message from the adopter explaining why they want to adopt this animal.'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    processed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='processed_adoption_requests',
        limit_choices_to={'role': 'SHELTER'}
    )

    decision_notes = models.TextField(
        blank=True,
        help_text='Optional shelter notes explaining the adoption decision.'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    processed_at = models.DateTimeField(blank=True, null=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        animal_name = self.animal.name or self.animal.report.get_animal_type_display()
        return f'{animal_name} adoption request by {self.requester.username} - {self.get_status_display()}'