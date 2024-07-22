from django.shortcuts import render



def appointmentHome(req):
    return render(req, 'appointment/pages/appointmentHome.html')

def appointmentConfirmation(req, id):
    return render(req, 'appointment/pages/appointmentConfirmation.html')
