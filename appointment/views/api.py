from rest_framework.decorators import api_view
from rest_framework.response import Response
from appointment.models import Appointment
from appointment.serializer import AppointmentSerializer

@api_view()
def appointments_api_list(request):
    appointments = Appointment.objects.all()
    serializer = AppointmentSerializer(instance=appointments, many=True)
    return Response(serializer.data)