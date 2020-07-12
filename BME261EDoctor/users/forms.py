from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class PatientRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, *args, **kwargs):
        print("test 1")
        user = super().save()
        current_profile = user.Profile
        print(current_profile)
        current_profile.is_patient = True
        current_profile.save()

class TechnicianRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, *args, **kwargs):
        user = super().save()
        current_profile = user.Profile
        current_profile.is_technician = True
        current_profile.save()


class DoctorRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, *args, **kwargs):
        user = super().save()
        current_profile = user.Profile
        current_profile.is_doctor = True
        current_profile.save()


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        #model = AudioFiles
        #fields = ['audio']
