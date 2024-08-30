from django.urls import path, include
from appointment import views
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

app_name = 'appointment'


appointment_api_v1_router = SimpleRouter()

appointment_api_v1_router.register(
      prefix= 'api/v1',
      viewset= views.AppointmentAPIV1ViewSet,
      basename='appointment-api',
)
# print(f'router: {appointment_api_v1_router.urls}')

urlpatterns = [
      path('', 
          views.site.appointmentHome, 
          name='home'
      ),
    
      path('<int:id>/', 
          views.site.appointmentConfirmation, 
          name='confirmation'
      ),
    
      path('my-appointments/', 
          views.site.my_appointments, 
          name='myAppointments'
      ),
    
      path('api/v1/user/<int:id>/', 
          views.api.user_api_detail, 
          name='user_detail_api_v1'
      ),
      
      # JWT
      path('api/token/', 
           TokenObtainPairView.as_view(), 
           name='token_obtain_pair'
      ),
      path('api/token/refresh/', 
           TokenRefreshView.as_view(), 
           name='token_refresh'
      ),
      path('api/token/verify/', 
           TokenVerifyView.as_view(), 
           name='token_verify'
      ),
      
      # Router
      path('', include(appointment_api_v1_router.urls)),

]
