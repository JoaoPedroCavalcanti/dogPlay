from rest_framework import serializers

class AppointmentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    time = serializers.TimeField()
    date = serializers.DateField()
    public = serializers.BooleanField(source='is_confirmed')
    time_and_date = serializers.SerializerMethodField()
    
    def get_time_and_date(self, appointment):
        return f'Time: {appointment.time} and Date: {appointment.date}'