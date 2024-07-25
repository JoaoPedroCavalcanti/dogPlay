from django.shortcuts import render, get_object_or_404
from .models import Appointment
from django.contrib import messages

def appointmentHome(req):
    
    appointments = Appointment.objects.all().order_by('-id')
    return render(req, 'appointment/pages/appointmentHome.html', context={
        'datesAndTimes': appointments
    })

def appointmentConfirmation(req, id):
    
    # Message to confirm appointment
    messages.success(req, 'Appointment confirmed')
    
    appointment = get_object_or_404(Appointment, pk = id)   
    return render(req, 'appointment/pages/appointmentConfirmation.html', context={
        'dataConfirmation': appointment
    })

def my_appointments(req):
    
    return render(req, 'appointment/pages/my_appointments_page.html')