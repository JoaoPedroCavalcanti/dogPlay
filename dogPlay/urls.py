from django.contrib import admin
from django.urls import include,  path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('appointment/', include('appointment.urls')),
    path('petOwner/', include('petOwner.urls')),
]
