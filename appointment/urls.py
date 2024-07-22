from django.urls import path
from . import views
# from appointment import views



urlpatterns = [
    path('', views.appointmentHome),
    path('<int:id>/', views.appointmentConfirmation),
]
