from django.urls import path
from home.views import home

app_name = 'homePage'

urlpatterns = [
    path('', home, name='home')
]
