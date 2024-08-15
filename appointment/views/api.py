from rest_framework.decorators import api_view
from rest_framework.response import Response
from appointment.models import Appointment
from appointment.serializer import AppointmentSerializer, UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.contrib.auth.models import User


@api_view()
def appointments_api_list(request):
    appointments = Appointment.objects.all()
    serializer = AppointmentSerializer(instance=appointments, many=True, context={'request': request})
    return Response(serializer.data)

@api_view()
def appointments_api_detail(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    serializer = AppointmentSerializer(instance=appointment, many=False, context={'request': request})
    return Response(serializer.data)

@api_view()
def user_api_detail(request, id):
    user = get_object_or_404(User, id=id)
    serializer = UserSerializer(instance=user, many=False, context={'request': request})
    return Response(serializer.data)