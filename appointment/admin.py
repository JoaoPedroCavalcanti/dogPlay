from django.contrib import admin
from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    ...

admin.site.register(Appointment, AppointmentAdmin)

# Or
# @admin.register(Appointment)
# class AppointmentAdmin(admin.ModelAdmin):
#     ...


