from django.contrib import admin
from .models import CustomUser, MedicalInformation

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(MedicalInformation)