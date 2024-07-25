from django.urls import path
from . import views
# from appointment import views

app_name = 'appointment'

urlpatterns = [
    path('', views.appointmentHome, name='home'), #The name will be appointment:home
    path('<int:id>/', views.appointmentConfirmation, name='confirmation'),#The name will be appointment:confirmation
    path('my-appointments/', views.my_appointments, name='myAppointments')
]
