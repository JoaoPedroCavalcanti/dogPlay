from django.urls import path
from petOwner import views

app_name = 'petOwner'

urlpatterns = [
    path('register/', views.registerPetOwner, name='register'),
    path('register/create/', views.createPetowner, name='create')
]
