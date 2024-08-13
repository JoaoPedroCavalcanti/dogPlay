from django.urls import path
from petOwner import views

app_name = 'petOwner'

urlpatterns = [
    path('register/', 
         views.registerPetOwner, 
         name='register'),
    
    path('register/create/', 
         views.createPetowner, 
         name='create_register'),
    path('login/', 
         views.loginPetOwner, 
         name='login'),
    
    path('register/create_login/', 
         views.create_login, 
         name='create_login'),
    
    path('logout/', 
         views.logout_view, 
         name='logout'),
    
    path('appointment/assign/<int:id>/', 
         views.assign_appointment, 
         name='assign_appointment'),
    
    path('appointment/unassign/<int:id>/', 
         views.unassign_appointment, 
         name='unassign_appointment'),
    
    path('dashboard/', 
         views.DashboardAppointments.as_view(), 
         name='dashboard'),
    
    path('dashboard/appointment/<int:id>/', 
         views.appointment, 
         name='appointment'),
    
    path('profile/<int:id>/', 
         views.ProfileView.as_view(),
         name='profile'),
]