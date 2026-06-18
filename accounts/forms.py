from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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

    class Meta:
        model = User
        fields = [
            'username',
            'full_name',
            'email',
            'phone_number',
            'role',
            'service_area',
            'password1',
            'password2',
        ]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Required for rescuers'
            }),
            'service_area': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Required for shelters. Example: Colombo'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field_name == 'role':
                field.widget.attrs.update({'class': 'form-select'})
            else:
                field.widget.attrs.update({'class': 'form-control'})

        self.fields['username'].widget.attrs.update({'placeholder': 'Enter username'})
        self.fields['full_name'].widget.attrs.update({'placeholder': 'Enter full name'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter email address'})
        self.fields['phone_number'].widget.attrs.update({'placeholder': 'Required for rescuers'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Enter password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm password'})

    def clean(self):
        cleaned_data = super().clean()

        role = cleaned_data.get('role')
        phone_number = cleaned_data.get('phone_number')
        service_area = cleaned_data.get('service_area')

        if role == 'RESCUER' and not phone_number:
            self.add_error('phone_number', 'Phone number is required for rescuer accounts.')

        if role == 'SHELTER' and not service_area:
            self.add_error('service_area', 'Service area is required for shelter accounts.')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)

        role = self.cleaned_data.get('role')
        user.role = role

        if role in ['RESCUER', 'SHELTER']:
            user.account_status = 'PENDING'
        else:
            user.account_status = 'APPROVED'

        if commit:
            user.save()

        return user


class UserLoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter username'
        })

        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter password'
        })


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'full_name',
            'email',
            'phone_number',
            'service_area',
        ]

        widgets = {
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
                'placeholder': 'Required for rescuers'
            }),
            'service_area': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Required for shelters. Example: Colombo'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()

        phone_number = cleaned_data.get('phone_number')
        service_area = cleaned_data.get('service_area')

        if self.instance.role == 'RESCUER' and not phone_number:
            self.add_error('phone_number', 'Phone number is required for rescuer accounts.')

        if self.instance.role == 'SHELTER' and not service_area:
            self.add_error('service_area', 'Service area is required for shelter accounts.')

        return cleaned_data