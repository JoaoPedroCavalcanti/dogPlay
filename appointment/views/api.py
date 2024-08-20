from rest_framework.decorators import api_view
from rest_framework.response import Response
from appointment.models import Appointment
from appointment.serializer import AppointmentSerializer, UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination

class AppointmentAPIV1Pagination(PageNumberPagination):
    page_size = 2

class AppointmentAPIV1List(ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    pagination_class = AppointmentAPIV1Pagination
    # def get(self, request):
    #     appointments = Appointment.objects.all()
    #     serializer = AppointmentSerializer(instance=appointments, many=True, context={'request': request})
    #     return Response(serializer.data)

        
    # def post(self, request):
    #     data = request.data
    #     serialized_data = AppointmentSerializer(
    #         data=data,
    #         context={'request': request}
    #     )

    #     serialized_data.is_valid(raise_exception=True)
    #     print(serialized_data)
    #     serialized_data.save()
        
    #     return Response(serialized_data.data, status=status.HTTP_201_CREATED)
    
class AppointmentAPIV1Detail(APIView):
    def get_appointment(self, id):
        appointment = get_object_or_404(Appointment, id=id)
        return appointment
    
    def get(self, request, id):
        appointment = self.get_appointment(id)
        serializer = AppointmentSerializer(
            instance=appointment, 
            many=False, 
            context={'request': request}
        )
        return Response(serializer.data)
    
    def patch(self, request, id):
        appointment = self.get_appointment(id)
        serializer = AppointmentSerializer(
            instance=appointment,
            data = request.data,
            many=False,
            partial = True,
            context={'request': request}
        )
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, id):
        appointment = self.get_appointment(id)
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(http_method_names=['get', 'post'])
def appointments_api_list(request):
    if request.method == 'GET':
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(instance=appointments, many=True, context={'request': request})
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serialized_data = AppointmentSerializer(
            data=data,
            context={'request': request}
        )

        serialized_data.is_valid(raise_exception=True)
        print(serialized_data)
        serialized_data.save()
        
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)

@api_view(http_method_names=['get', 'patch', 'delete'])
def appointment_api_detail(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    
    if request.method == 'GET':
        serializer = AppointmentSerializer(
            instance=appointment, 
            many=False, 
            context={'request': request}
        )
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        serializer = AppointmentSerializer(
            instance=appointment,
            data = request.data,
            many=False,
            partial = True,
            context={'request': request}
        )
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

@api_view()
def user_api_detail(request, id):
    user = get_object_or_404(User, id=id)
    serializer = UserSerializer(instance=user, many=False, context={'request': request})
    return Response(serializer.data)

    