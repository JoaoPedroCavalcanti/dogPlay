from rest_framework.decorators import api_view
from rest_framework.response import Response
from appointment.models import Appointment
from appointment.serializer import AppointmentSerializer, UserSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAdminUser
from appointment.permissions import IsOwnerOrAdmin

class AppointmentAPIV1Pagination(PageNumberPagination):
    page_size = 10
    
class AppointmentAPIV1ViewSet(ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    pagination_class = AppointmentAPIV1Pagination
    permission_classes = [AllowAny,]
    http_method_names = ['get', 'patch', 'post', 'delete']

    def get_serializer_context(self):
        context = super(AppointmentAPIV1ViewSet, self).get_serializer_context()
        context.update({"request": self.request})
        return context

    # def get_object(self):
    #     pk = self.kwargs.get('pk', '')
    #     obj = get_object_or_404(
    #         self.get_queryset(),
    #         pk = pk
    #     )
    #     self.check_object_permissions(request=self.request, obj = obj)
    #     return obj

    def get_permissions(self):
        if self.request.method == 'PATCH':
            return [IsOwnerOrAdmin(),]
        
        if self.request.method in ['DELETE', 'POST']:
            return [IsAdminUser(), ]
        
        return super().get_permissions()


@api_view()
def user_api_detail(request, id):
    user = get_object_or_404(User, id=id)
    serializer = UserSerializer(instance=user, many=False, context={'request': request})
    return Response(serializer.data)

    