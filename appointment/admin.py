from django.contrib import admin
from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'date',]
    search_fields = ['id', 'date', 'time',]

admin.site.register(Appointment, AppointmentAdmin)

# Or
# @admin.register(Appointment)
# class AppointmentAdmin(admin.ModelAdmin):
#     ...


