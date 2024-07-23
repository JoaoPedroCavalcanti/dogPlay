from django.shortcuts import render, get_object_or_404
from .models import Appointment
from django.http import Http404

def appointmentHome(req):
    
    appointments = Appointment.objects.all().order_by('-id')
    return render(req, 'appointment/pages/appointmentHome.html', context={
        'datesAndTimes': appointments
    })

def appointmentConfirmation(req, id):
    
    appointment = get_object_or_404(Appointment, pk = id)   
    return render(req, 'appointment/pages/appointmentConfirmation.html', context={
        'dataConfirmation': appointment
    })


