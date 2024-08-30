from rest_framework import serializers
from django.contrib.auth.models import User
from appointment.models import Appointment

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField(max_length=255)

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'time', 'date', 'petOwner', 'petOwner_link', 'is_confirmed']
        # extra_kwargs = {
        #     'id': {'read_only': True},
        #     'time': {'read_only': True},
        #     'date': {'read_only': True},
        #     'is_confirmed': {'read_only': True},
        # }
        
    def __init__(self, *args, **kwargs):
        super(AppointmentSerializer, self).__init__(*args, **kwargs)
        user = self.context['request'].user
        if not user.is_staff:
            self.fields['petOwner'].read_only = False  # Permite que o usuário altere o campo 'time'
            for field in self.fields:
                if field != 'petOwner':
                    self.fields[field].read_only = True  # Torna os outros campos read-only
        
        
    
    petOwner_link = serializers.HyperlinkedRelatedField(
        many=False,
        source='petOwner',
        view_name='appointment:user_detail_api_v1',
        lookup_field='id',
        read_only=True
    )
    
        
    def get_time_and_date(self, appointment):
        return f'Time: {appointment.time} and Date: {appointment.date}'
    
    
    # def validate(self, attrs):
    #     if attrs['is_confirmed'] == False:
    #         raise serializers.ValidationError({
    #             "Error description": "is_confirmed should be True"
    #         })
    #     return attrs
    
    # def validate_is_confirmed(self, value):
    #     if value == False:
    #         raise serializers.ValidationError("is_confirmed should be True")
    #     return value

    def validate_petOwner(self, value):
        request = self.context['request']
        if not request.user.is_staff:
            # Se não for admin, só pode definir o petOwner como ele mesmo ou None
            if value and value != request.user:
                raise serializers.ValidationError("You can only define this fiels as None or yours.")
        return value