from rest_framework.decorators import api_view
from rest_framework.response import Response
from appointment.models import Appointment
from appointment.serializer import AppointmentSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status

@api_view()
def appointments_api_list(request):
    appointments = Appointment.objects.all()
    serializer = AppointmentSerializer(instance=appointments, many=True)
    return Response(serializer.data)

@api_view()
def appointments_api_detail(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    serializer = AppointmentSerializer(instance=appointment, many=False)
    return Response(serializer.data)


    