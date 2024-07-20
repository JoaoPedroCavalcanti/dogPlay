from django.urls import path
from appointment import views


urlpatterns = [
    path('', views.appointmentHome),
    path('123/', views.appointmentConfirmation),
]
