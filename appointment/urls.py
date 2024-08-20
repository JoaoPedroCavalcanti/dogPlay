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
    
    path('api/v1/', 
         views.api.AppointmentAPIV1List.as_view(),
          name='appointments_list_api_v1'
    ),
    
     path('api/v1/<int:id>/',
          views.api.AppointmentAPIV1Detail.as_view(), 
          name='appointment_detail_api_v1'
    ),
     
      path('api/v1/user/<int:id>/', 
          views.api.user_api_detail, 
          name='user_detail_api_v1'
    ),
     

]
