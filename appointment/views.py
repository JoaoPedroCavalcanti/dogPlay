from django.shortcuts import render
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
    return render(req, 'appointment/pages/appointmentHome.html', context={
        'datesAndTimes': [generate_random_date_time() for _ in range(10)]
    })

def appointmentConfirmation(req, id):
    return render(req, 'appointment/pages/appointmentConfirmation.html', context={
        'dataConfirmation': generate_random_data()
    })


