from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User, UserReport


class UserRegistrationForm(UserCreationForm):
    linked_shelter = forms.ModelChoiceField(
        queryset=User.objects.none(),
        required=False,
        label='Linked Shelter',
        empty_label='Select linked shelter',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = User
        fields = [
            'username',
            'full_name',
            'email',
            'phone_number',
            'role',
            'service_area',
            'shelter_address',
            'shelter_map_link',
            'linked_shelter',
            'password1',
            'password2',
        ]

        labels = {
            'username': 'Username',
            'full_name': 'Full Name',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'role': 'Account Role',
            'service_area': 'Service Area',
            'shelter_address': 'Shelter Address / Handover Location',
            'shelter_map_link': 'Shelter Map Link',
            'linked_shelter': 'Linked Shelter',
        }

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter username'
            }),
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email address'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number'
            }),
            'role': forms.Select(attrs={
                'class': 'form-select'
            }),
            'service_area': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Example: Kottawa, Maharagama, Homagama'
            }),
            'shelter_address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter shelter handover address'
            }),
            'shelter_map_link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Optional Google Maps or Apple Maps link'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['role'].choices = [
            ('PUBLIC', 'Public User'),
            ('RESCUER', 'Rescuer'),
            ('SHELTER', 'Shelter'),
        ]

        self.fields['linked_shelter'].queryset = User.objects.filter(
            role='SHELTER',
            account_status='APPROVED',
            is_active=True
        ).order_by('full_name', 'username')

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter password'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm password'
        })

    def clean(self):
        cleaned_data = super().clean()

        role = cleaned_data.get('role')
        phone_number = cleaned_data.get('phone_number')
        service_area = cleaned_data.get('service_area')
        shelter_address = cleaned_data.get('shelter_address')
        linked_shelter = cleaned_data.get('linked_shelter')

        if role in ['RESCUER', 'SHELTER'] and not phone_number:
            self.add_error(
                'phone_number',
                'Phone number is required for rescuer and shelter accounts.'
            )

        if role == 'SHELTER':
            if not service_area:
                self.add_error(
                    'service_area',
                    'Service area is required for shelter accounts.'
                )

            if not shelter_address:
                self.add_error(
                    'shelter_address',
                    'Shelter address / handover location is required for shelter accounts.'
                )

        if role == 'RESCUER' and not linked_shelter:
            self.add_error(
                'linked_shelter',
                'Please select the shelter you are linked with.'
            )

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)

        role = self.cleaned_data.get('role')

        user.role = role

        if role == 'PUBLIC':
            user.account_status = 'APPROVED'
            user.linked_shelter = None
            user.service_area = ''
            user.shelter_address = ''
            user.shelter_map_link = ''

        elif role == 'RESCUER':
            user.account_status = 'PENDING'
            user.linked_shelter = self.cleaned_data.get('linked_shelter')
            user.service_area = ''
            user.shelter_address = ''
            user.shelter_map_link = ''

        elif role == 'SHELTER':
            user.account_status = 'PENDING'
            user.linked_shelter = None

        if commit:
            user.save()

        return user


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter username'
        })
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter password'
        })
    )


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'full_name',
            'email',
            'phone_number',
            'service_area',
            'shelter_address',
            'shelter_map_link',
        ]

        labels = {
            'full_name': 'Full Name',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'service_area': 'Service Area',
            'shelter_address': 'Shelter Address / Handover Location',
            'shelter_map_link': 'Shelter Map Link',
        }

        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'service_area': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'shelter_address': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'shelter_map_link': forms.URLInput(attrs={
                'class': 'form-control'
            }),
        }


class UserReportForm(forms.ModelForm):
    class Meta:
        model = UserReport
        fields = [
            'reason',
            'description',
        ]

        labels = {
            'reason': 'Reason for Reporting',
            'description': 'Explanation',
        }

        widgets = {
            'reason': forms.Select(attrs={
                'class': 'form-select'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Explain why this account seems suspicious or unsafe.'
            }),
        }

    def clean_description(self):
        description = self.cleaned_data.get('description')

        if not description:
            raise forms.ValidationError('Please explain why you are reporting this account.')

        if len(description.strip()) < 20:
            raise forms.ValidationError('Please write at least 20 characters explaining the issue.')

        return description