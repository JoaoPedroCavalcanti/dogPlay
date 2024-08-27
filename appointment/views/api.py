from rest_framework.decorators import api_view
from rest_framework.response import Response
from appointment.models import Appointment
from appointment.serializer import AppointmentSerializer, UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

class AppointmentAPIV1Pagination(PageNumberPagination):
    page_size = 10
    
class AppointmentAPIV1ViewSet(ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    pagination_class = AppointmentAPIV1Pagination


@api_view()
def user_api_detail(request, id):
    user = get_object_or_404(User, id=id)
    serializer = UserSerializer(instance=user, many=False, context={'request': request})
    return Response(serializer.data)

    