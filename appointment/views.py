from django.shortcuts import render



def home(req):
    return render(req, 'appointment/pages/home.html')

