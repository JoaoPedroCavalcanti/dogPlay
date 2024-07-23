from django.shortcuts import render
from .models import Appointment
# To import dateAndTimeFuncion that is in another file
import sys
import os

# Add the utils/appointment directory to the system path
appointment_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../utils/appointment'))
sys.path.append(appointment_path)

# Now import the function
from randomDateAndTime import generate_random_date_time, generate_random_data

# Use the function
# a = generate_random_date_time()
# print(a)

def appointmentHome(req):
    appointments = Appointment.objects.all().order_by('-id')
    return render(req, 'appointment/pages/appointmentHome.html', context={
        'datesAndTimes': appointments
    })

def appointmentConfirmation(req, id):
    appointments = Appointment.objects.filter(id = id)
    return render(req, 'appointment/pages/appointmentConfirmation.html', context={
        # 'dataConfirmation': generate_random_data()
        'dataConfirmation': appointments.first()
    })


