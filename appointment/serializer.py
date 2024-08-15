from rest_framework import serializers
from django.contrib.auth.models import User
from appointment.models import Appointment

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField(max_length=255)

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'time', 'date', 'public', 'time_and_date', 'petOwner', 'petOwner_link']
        
    public = serializers.BooleanField(source='is_confirmed', read_only=True)
    time_and_date = serializers.SerializerMethodField(read_only=True)
    
    petOwner_link = serializers.HyperlinkedRelatedField(
        many=False,
        source='petOwner',
        view_name='appointment:user_detail_api_v1',
        lookup_field='id',
        read_only=True
    )
    
        
    def get_time_and_date(self, appointment):
        return f'Time: {appointment.time} and Date: {appointment.date}'
    
    
    
    
