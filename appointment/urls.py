from django.urls import path
from appointment.views import home

urlpatterns = [
    path('', home)
]
