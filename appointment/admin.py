from django.contrib import admin
from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['petOwner', 'is_confirmed', 'time', 'date', 'id',]
    search_fields = ['is_confirmed', 'id', 'date', 'time',]

admin.site.register(Appointment, AppointmentAdmin)

# Or
# @admin.register(Appointment)
# class AppointmentAdmin(admin.ModelAdmin):
#     ...


