from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, CreateView
from .forms import CustomUserCreationForm, MedicalInfoForm, AppointmentForm
from .models import MedicalInformation, CustomUser, Appointments
from django.urls import reverse_lazy
from django.core.mail import send_mail

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class SignupView(CreateView):
    template_name = 'signup.html'
    success_url = reverse_lazy('signin')
    form_class = CustomUserCreationForm

class SigninView(TemplateView):
    template_name = 'signin.html'

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

class MedinfoView(CreateView):
    template_name = 'medinfo.html'
    success_url = reverse_lazy('dashboard')
    form_class = MedicalInfoForm


def statistics(request):
    records = MedicalInformation.objects.all()
    covid = records.filter(covid=True).count()
    ebola = records.filter(ebola=True).count()
    malaria = records.filter(malaria=True).count()
    diabetes = records.filter(diabetes=True).count()
    
    context = {
        "records": records,
        "covid": covid,
        "ebola": ebola,
        "malaria": malaria,
        "diabetes": diabetes,
    }
    return render(request, 'stats.html', context=context)

    # urls should have something like path("records/<int:id>")
def records_detail(request, id):
    # if the user is a patient, redirect back to dashboard
    if request.user.category == 'normal_patient':
        return redirect("dashboard")
    
    user = CustomUser.objects.get(id=id)
    info = MedicalInformation.filter(user=user)

    context = {
        "user": user,
        "info": info,
    }	

    return render(request, "records_detail.html", context=context)
        
def records(request):
        # if the user is a patient, redirect back to dashboard
    if request.user.category == 'normal_patient':
        return redirect("dashboard")
    
    # get all patients 
    users = CustomUser.objects.filter(category="normal_patient")
    
    context = {
        "users": users,
    }	

    return render(request, "records.html", context=context)

    # to filter by condition, use /record_filter/?condition=malaria 
def record_filter(request):
    # if the user is a patient, redirect back to dashboard
    if request.user.category == 'normal_patient':
        return redirect("dashboard")
    
    condition = request.GET.get('condition')
    info = MedicalInformation.objects.filter(condition=True).user

    context = {
        "info": info,
    }	

    return render(request, "record_filter.html", context=context)

    # to serach for medical practioner use /appointment_filter/?worker=princewill 
def worker_filter(request):
    # if the user is a patient, redirect back to dashboard
    if request.user.category == 'normal_patient':
        return redirect("dashboard")
    
    worker = request.GET.get('princewill')
    user = CustomUser.objects.filter(first_name=worker).first()
    
    form = AppointmentForm()

    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            # google how to send email
            send_mail(user.email)

    context = {
        "user": user,
        "form": form,
    }	

    return render(request, "worker_filter.html", context=context)

def appointment_list(request):
# if the user is a patient, redirect back to dashboard
    if request.user.category == 'normal_patient':
        return redirect("dashboard")
    
    user = request.user
    appointments = Appointments.objects.filter(worker=user)

    context = {
        "user": user,
        "appointments": appointments,
    }	

    return render(request, "appoint.html", context=context)

def appointment_detail(request, id):
    # if the user is a patient, redirect back to dashboard
    if request.user.category == 'normal_patient':
        return redirect("dashboard")
    
    appointment = Appointments.objects.get(id=id)
    
    form = AppointmentForm(instance=appointment)

    if request.method == "POST":
        form = AppointmentForm(instance=appointment, data=request.POST)
        if form.is_valid():
            form.save()

    context = {
        "form": form,
    }	

    return render(request, "worker_filter.html", context=context)

    # to serach for medical practioner use /appointment_filter/?month=january 
def appointment_filter(request):
    # if the user is a patient, redirect back to dashboard
    if request.user.category == 'normal_patient':
        return redirect("dashboard")
    
    worker = request.GET.get('worker')
    user = CustomUser.objects.filter(first_name=worker).first()
    
    form = AppointmentForm()

    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            # google how to send email
            send_mail(user.email)

    context = {
        "user": user,
        "form": form,
    }	

    return render(request, "worker_filter.html", context=context)        