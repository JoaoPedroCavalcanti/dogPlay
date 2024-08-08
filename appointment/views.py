from django.shortcuts import render, get_object_or_404
from .models import Appointment
from django.contrib import messages
from utils.past_and_future_appointments import past_and_future_appointments


def appointmentHome(req):
    appointments = Appointment.objects.filter(
        petOwner = None
    )
    past_appointments, future_appointments = past_and_future_appointments(appointments)

    print(past_appointments)
    print(future_appointments)
    
    return render(req, 'appointment/pages/appointmentHome.html', context={
        'appointments': future_appointments
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