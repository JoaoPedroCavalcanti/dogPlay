from rest_framework import serializers

class AppointmentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    time = serializers.TimeField()
    date = serializers.DateField()