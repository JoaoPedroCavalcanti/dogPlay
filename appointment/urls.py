from django.urls import path
from appointment.views import appointmentForm

urlpatterns = [
    path('', appointmentForm)
]
