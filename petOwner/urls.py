from django.urls import path
from petOwner import views

app_name = 'petOwner'

urlpatterns = [
    path('register/', views.registerPetOwner, name='register'),
    path('register/create/', views.createPetowner, name='create_register'),
    path('login/', views.loginPetOwner, name='login'),
    path('register/create_login/', views.create_login, name='create_login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
]
