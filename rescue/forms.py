from django import forms
from django.contrib.auth import get_user_model

from .models import Report, RescueUpdate, Animal, AdoptionRequest


User = get_user_model()


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = [
            'reporter_contact_phone',
            'animal_type',
            'other_animal_type',
            'condition',
            'description',
            'image',
            'latitude',
            'longitude',
            'location_description',
            'map_link',
        ]

        widgets = {
            'reporter_contact_phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter contact number for shelter verification'
            }),
            'animal_type': forms.Select(attrs={'class': 'form-select'}),
            'other_animal_type': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter animal type if you selected Other'
            }),
            'condition': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Describe the animal condition and situation'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
            'latitude': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.000001',
                'placeholder': 'Example: 6.927079'
            }),
            'longitude': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.000001',
                'placeholder': 'Example: 79.861244'
            }),
            'location_description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Example: Near Kottawa bus stand, beside the main road'
            }),
            'map_link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Optional Google Maps or Apple Maps link'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['animal_type'].choices = self.fields['animal_type'].choices[1:]
        self.fields['condition'].choices = self.fields['condition'].choices[1:]

    def clean(self):
        cleaned_data = super().clean()

        reporter_contact_phone = cleaned_data.get('reporter_contact_phone')
        animal_type = cleaned_data.get('animal_type')
        other_animal_type = cleaned_data.get('other_animal_type')
        latitude = cleaned_data.get('latitude')
        longitude = cleaned_data.get('longitude')

        if not reporter_contact_phone:
            self.add_error(
                'reporter_contact_phone',
                'Contact phone number is required so the shelter can verify the report before assigning a rescuer.'
            )

        if animal_type == 'OTHER' and not other_animal_type:
            self.add_error(
                'other_animal_type',
                'Please enter the animal type when selecting Other.'
            )

        if latitude and not longitude:
            self.add_error('longitude', 'Longitude is required when latitude is provided.')

        if longitude and not latitude:
            self.add_error('latitude', 'Latitude is required when longitude is provided.')

        return cleaned_data

    def clean_image(self):
        image = self.cleaned_data.get('image')

        if image:
            max_size = 5 * 1024 * 1024

            if hasattr(image, 'size') and image.size > max_size:
                raise forms.ValidationError('Image size must be less than 5MB.')

            allowed_content_types = [
                'image/jpeg',
                'image/png',
                'image/webp',
            ]

            if hasattr(image, 'content_type'):
                if image.content_type not in allowed_content_types:
                    raise forms.ValidationError('Only JPG, PNG, or WEBP images are allowed.')

        return image


class ReportReviewForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = [
            'priority',
            'verification_status',
            'verification_notes',
        ]

        widgets = {
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'verification_status': forms.Select(attrs={'class': 'form-select'}),
            'verification_notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Example: The reporter confirmed that the animal had already been rescued before the shelter could assign a rescuer.'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['priority'].choices = self.fields['priority'].choices[1:]
        self.fields['verification_status'].choices = self.fields['verification_status'].choices[1:]

    def clean(self):
        cleaned_data = super().clean()

        priority = cleaned_data.get('priority')
        verification_status = cleaned_data.get('verification_status')

        if not priority:
            self.add_error(
                'priority',
                'Final priority is required before saving the shelter review.'
            )

        if verification_status == 'PENDING_VERIFICATION':
            self.add_error(
                'verification_status',
                'Please select a verification outcome before saving the shelter review.'
            )

        return cleaned_data
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['verification_status'].choices = [
            ('CONFIRMED_STILL_THERE', 'Confirmed Still There'),
            ('ANIMAL_NOT_FOUND', 'Animal Not Found'),
            ('ALREADY_RESCUED', 'Already Rescued'),
        ]


class RescueAssignmentForm(forms.ModelForm):
    assigned_rescuer = forms.ModelChoiceField(
        queryset=User.objects.none(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        empty_label='Select linked approved rescuer'
    )

    class Meta:
        model = Report
        fields = [
            'assigned_rescuer',
            'assignment_notes',
        ]

        labels = {
            'assigned_rescuer': 'Linked Approved Rescuer',
            'assignment_notes': 'Rescue and Handover Instructions',
        }

        widgets = {
            'assignment_notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': (
                    'Example: Animal is behind Pizza Hut near the station. '
                    'After rescue, bring the animal to our shelter handover location.'
                )
            }),
        }

    def __init__(self, *args, **kwargs):
        shelter_user = kwargs.pop('shelter_user', None)

        super().__init__(*args, **kwargs)

        rescuer_queryset = User.objects.filter(
            role='RESCUER',
            account_status='APPROVED',
            is_active=True
        )

        if shelter_user:
            rescuer_queryset = rescuer_queryset.filter(
                linked_shelter=shelter_user
            )

        self.fields['assigned_rescuer'].queryset = rescuer_queryset.order_by(
            'full_name',
            'username'
        )

    def clean_assigned_rescuer(self):
        assigned_rescuer = self.cleaned_data.get('assigned_rescuer')

        if not assigned_rescuer:
            raise forms.ValidationError('Please select a linked rescuer to assign this case.')

        return assigned_rescuer


class RescueUpdateForm(forms.ModelForm):
    class Meta:
        model = RescueUpdate
        fields = [
            'status',
            'update_text',
            'photo',
        ]

        widgets = {
            'status': forms.Select(attrs={'class': 'form-select'}),
            'update_text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Example: The animal has been handed over to the shelter.'
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['status'].choices = self.fields['status'].choices[1:]

    def clean_update_text(self):
        update_text = self.cleaned_data.get('update_text')

        if not update_text:
            raise forms.ValidationError('Please enter a rescue update note.')

        return update_text

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')

        if photo:
            max_size = 5 * 1024 * 1024

            if hasattr(photo, 'size') and photo.size > max_size:
                raise forms.ValidationError('Photo size must be less than 5MB.')

            allowed_content_types = [
                'image/jpeg',
                'image/png',
                'image/webp',
            ]

            if hasattr(photo, 'content_type'):
                if photo.content_type not in allowed_content_types:
                    raise forms.ValidationError('Only JPG, PNG, or WEBP photos are allowed.')

        return photo


class AnimalTreatmentForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = [
            'name',
            'age',
            'gender',
            'animal_image',
            'health_status',
            'treatment_status',
            'treatment_notes',
            'vet_info',
            'arrival_date',
            'outcome_notes',
        ]

        labels = {
            'name': 'Animal Name',
            'age': 'Approximate Age',
            'gender': 'Gender',
            'animal_image': 'Updated Animal Image',
            'health_status': 'Health Status',
            'treatment_status': 'Treatment Status',
            'treatment_notes': 'Treatment Notes',
            'vet_info': 'Vet / Clinic Information',
            'arrival_date': 'Arrival Date',
            'outcome_notes': 'Outcome Notes',
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Optional name given by the shelter'
            }),
            'age': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Example: Puppy, Adult, 2 years, Unknown'
            }),
            'gender': forms.Select(attrs={
                'class': 'form-select'
            }),
            'animal_image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
            'health_status': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Describe the animal’s current health condition'
            }),
            'treatment_status': forms.Select(attrs={
                'class': 'form-select'
            }),
            'treatment_notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Add treatment progress notes'
            }),
            'vet_info': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Example: City Vet Clinic, Maharagama'
            }),
            'arrival_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'outcome_notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Required if the animal passed away. Optional for other outcomes.'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['gender'].choices = self.fields['gender'].choices[1:]
        self.fields['treatment_status'].choices = self.fields['treatment_status'].choices[1:]

    def clean(self):
        cleaned_data = super().clean()

        treatment_status = cleaned_data.get('treatment_status')
        health_status = cleaned_data.get('health_status')
        treatment_notes = cleaned_data.get('treatment_notes')
        outcome_notes = cleaned_data.get('outcome_notes')

        if not health_status:
            self.add_error(
                'health_status',
                'Please enter the animal health status.'
            )

        if not treatment_notes:
            self.add_error(
                'treatment_notes',
                'Please enter treatment notes.'
            )

        if treatment_status == 'PASSED_AWAY' and not outcome_notes:
            self.add_error(
                'outcome_notes',
                'Please add a short outcome note when the animal status is Passed Away.'
            )

        return cleaned_data

    def clean_animal_image(self):
        animal_image = self.cleaned_data.get('animal_image')

        if animal_image:
            max_size = 5 * 1024 * 1024

            if hasattr(animal_image, 'size') and animal_image.size > max_size:
                raise forms.ValidationError('Image size must be less than 5MB.')

            allowed_content_types = [
                'image/jpeg',
                'image/png',
                'image/webp',
            ]

            if hasattr(animal_image, 'content_type'):
                if animal_image.content_type not in allowed_content_types:
                    raise forms.ValidationError('Only JPG, PNG, or WEBP images are allowed.')

        return animal_image


class AdoptionRequestForm(forms.ModelForm):
    class Meta:
        model = AdoptionRequest
        fields = [
            'message',
        ]

        labels = {
            'message': 'Adoption Request Message',
        }

        widgets = {
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Explain why you want to adopt this animal and how you will care for it.'
            }),
        }

    def clean_message(self):
        message = self.cleaned_data.get('message')

        if not message:
            raise forms.ValidationError('Please enter a message for your adoption request.')

        if len(message.strip()) < 20:
            raise forms.ValidationError('Please write at least 20 characters explaining your adoption request.')

        return message


class AdoptionDecisionForm(forms.ModelForm):
    status = forms.ChoiceField(
        choices=[
            ('APPROVED', 'Approve Request'),
            ('REJECTED', 'Reject Request'),
        ],
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = AdoptionRequest
        fields = [
            'status',
            'decision_notes',
        ]

        labels = {
            'status': 'Decision',
            'decision_notes': 'Decision Notes',
        }

        widgets = {
            'decision_notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Optional notes explaining the adoption decision.'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)