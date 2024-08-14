from django.urls import path
from appointment import views
# from appointment import views

app_name = 'appointment'

urlpatterns = [
    path('', 
         views.site.appointmentHome, 
         name='home'
    ), #The name will be appointment:home
    path('<int:id>/', 
         views.site.appointmentConfirmation, 
         name='confirmation'
    ),#The name will be appointment:confirmation
    path('my-appointments/', 
         views.site.my_appointments, 
         name='myAppointments'
    ),
    path('api/v1', 
         views.api.appointments_api_list, 
         name='appointments_api_v1'
    ),
]
