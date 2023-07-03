from django.urls import path
from .views import IndexView, SignupView, SigninView, DashboardView, MedinfoView, records, records_detail, appointment_filter, appointment_detail, appointment_list, worker_filter, record_filter, statistics

urlpatterns = [
path('', IndexView.as_view(), name='index'),
path('signup/', SignupView.as_view(), name='signup'),
path('signin/', SigninView.as_view(), name='signin'),
path('dashboard/', DashboardView.as_view(), name='dashboard'),
path('medinfo/', MedinfoView.as_view(), name='medinfo'),
path('records/', records, name='records'),
path('records/<int:id>', records_detail, name='records'),
path('record_filter/<int:id>', record_filter, name='record_filter'),
path('stats/', statistics, name='stats'),
path('worker_filter/', worker_filter, name='worker_filter'),
path('worker_filter/', appointment_filter, name='worker_filter'),
path('worker_filter/<int:id>', appointment_detail, name='worker_filter'),
path('appoint/', appointment_list, name='appoint'),
]