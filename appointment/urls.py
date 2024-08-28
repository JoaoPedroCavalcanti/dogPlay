from django.urls import path, include
from appointment import views
from rest_framework.routers import SimpleRouter

app_name = 'appointment'


appointment_api_v1_router = SimpleRouter()

appointment_api_v1_router.register(
      prefix= 'api/v1',
      viewset= views.AppointmentAPIV1ViewSet,
      # basename='appointment-api',
)
print(f'router: {appointment_api_v1_router.urls}')

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
    
#     path('api/v1/', 
#          views.api.AppointmentAPIV1ViewSet.as_view({
#                'get': 'list',
#                'post': 'create'
#             }),
#           name='appointments_list_api_v1'
#     ),
    
#      path('api/v1/<int:pk>/',
#           views.api.AppointmentAPIV1ViewSet.as_view({
#                 'get': 'retrieve',
#                 'patch': 'partial_update',
#                 'delete': 'destroy'
#             }), 
#           name='appointment_detail_api_v1'
#     ),
     
      path('api/v1/user/<int:id>/', 
          views.api.user_api_detail, 
          name='user_detail_api_v1'
    ),
      path('', include(appointment_api_v1_router.urls)),

]
