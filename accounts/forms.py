from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User


class UserRegistrationForm(UserCreationForm):
    role = forms.ChoiceField(
        choices=[
            ('PUBLIC', 'Public User'),
            ('RESCUER', 'Rescuer'),
            ('SHELTER', 'Shelter'),
        ],
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    linked_shelter = forms.ModelChoiceField(
        queryset=User.objects.none(),
        required=False,
        empty_label='Select linked shelter',
        label='Linked Shelter',
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
            'service_area': 'Service Area',
            'shelter_address': 'Shelter Address / Handover Location',
            'shelter_map_link': 'Shelter Map Link',
        }

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Choose a username'
            }),
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email address'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number'
            }),
            'service_area': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Example: Kottawa, Maharagama, Colombo'
            }),
            'shelter_address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Example: No. 25, Main Road, Maharagama'
            }),
            'shelter_map_link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Optional Google Maps or Apple Maps link'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter password'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm password'
        })

        self.fields['linked_shelter'].queryset = User.objects.filter(
            role='SHELTER',
            account_status='APPROVED',
            is_active=True
        ).order_by('full_name', 'username')

    def clean(self):
        cleaned_data = super().clean()

        role = cleaned_data.get('role')
        phone_number = cleaned_data.get('phone_number')
        service_area = cleaned_data.get('service_area')
        shelter_address = cleaned_data.get('shelter_address')
        linked_shelter = cleaned_data.get('linked_shelter')

        if role == 'RESCUER':
            if not phone_number:
                self.add_error(
                    'phone_number',
                    'Phone number is required for rescuer accounts.'
                )

            if not linked_shelter:
                self.add_error(
                    'linked_shelter',
                    'Please select the shelter you are linked with.'
                )

        if role == 'SHELTER':
            if not phone_number:
                self.add_error(
                    'phone_number',
                    'Phone number is required for shelter accounts.'
                )

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
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
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
            'service_area': 'Service Area',
            'shelter_address': 'Shelter Address / Handover Location',
            'shelter_map_link': 'Shelter Map Link',
        }

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'service_area': forms.TextInput(attrs={'class': 'form-control'}),
            'shelter_address': forms.TextInput(attrs={'class': 'form-control'}),
            'shelter_map_link': forms.URLInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        role = self.instance.role
        phone_number = cleaned_data.get('phone_number')
        service_area = cleaned_data.get('service_area')
        shelter_address = cleaned_data.get('shelter_address')

        if role == 'RESCUER' and not phone_number:
            self.add_error(
                'phone_number',
                'Phone number is required for rescuer accounts.'
            )

        if role == 'SHELTER':
            if not phone_number:
                self.add_error(
                    'phone_number',
                    'Phone number is required for shelter accounts.'
                )

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

        return cleaned_data