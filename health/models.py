from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField

# Create your models here.
GENDER = [
    ('male', 'MALE'),
    ('female', 'FEMALE'),
    ]
CATEGORY = [
    ('health_worker', 'HEALTH_WORKER'),
    ('normal_patient', 'NORMAL_PATIENT'),
]
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)
    phonenumber = models.CharField(max_length=12, null=True)
    gender = models.CharField(max_length=6, choices=GENDER, default=1)
    dob = models.DateField(max_length=8, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, default=1)
    country = CountryField(blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ()

    def __str__(self):
        return str(self.email)

class MedicalInformation(models.Model):
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    existingmedcondition = models.BooleanField(default=False)
    takingmedications = models.BooleanField(default=False)
    anyallergies = models.BooleanField(default=False)
    previoussurgeries = models.BooleanField(default=False)
    familymedhistory = models.BooleanField(default=False)
    covid = models.BooleanField(default=False)
    ebola = models.BooleanField(default=False)
    diabetes = models.BooleanField(default=False)
    malaria = models.BooleanField(default=False)
    smoker = models.BooleanField(default=False)
    drinker = models.BooleanField(default=False)
    exercise = models.BooleanField(default=False)

class Appointments(models.Model):
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='normal_patient', null=True)
    worker = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='health_worker', null=True)
    full_name = models.CharField(max_length=100)
    description = models.TextField()
