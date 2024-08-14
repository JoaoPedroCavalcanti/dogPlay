from rest_framework import serializers
from appointment.models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField(max_length=255)

class AppointmentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    time = serializers.TimeField()
    date = serializers.DateField()
    public = serializers.BooleanField(source='is_confirmed')
    time_and_date = serializers.SerializerMethodField()
    # petOwner = serializers.StringRelatedField()
    
    # petOwner_id = serializers.PrimaryKeyRelatedField(
    #     queryset=User.objects.all()
    # )
    petOwner = UserSerializer()
    
    def get_time_and_date(self, appointment):
        return f'Time: {appointment.time} and Date: {appointment.date}'