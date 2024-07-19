from django.shortcuts import render



def appointmentForm(req):
    return render(req, 'appointment/pages/appointmentForm.html')

