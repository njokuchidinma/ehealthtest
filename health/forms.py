from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MedicalInformation, Appointments, CustomUser

User = CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phonenumber', 'gender',
         'dob', 'category', 'country', 'password1', 'password2')

class MedicalInfoForm(forms.ModelForm):
    existingmedcondition = forms.BooleanField(label="Do you have any existing medical conditions?")
    takingmedications = forms.BooleanField(label="Are you currently taking any medications?")
    anyallergies = forms.BooleanField(label="Do you have any known allergies?")
    previoussurgeries = forms.BooleanField(label="Have you undergone any surgeries in the past?")
    familymedhistory = forms.BooleanField(label="Do you have any family members with a history of medical conditions?")
    covid = forms.BooleanField(label="Did you have covid?")
    ebola = forms.BooleanField(label="Did you have ebola?")
    diabetes = forms.BooleanField(label="Do you have diabetes?")
    malaria = forms.BooleanField(label="Do you have malaria?")
    smoker = forms.BooleanField(label="Do you smoke? ")
    drinker = forms.BooleanField(label="Do you consume alcohol?")
    exercise = forms.BooleanField(label="Do you exercise regularly?")
    class Meta:
        model = MedicalInformation
        fields = ('__all__')

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = ('__all__')
