from rest_framework import serializers
from .models import Mentee, Mentor

class MentorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Mentor
        fields = (
            'id',
            'first_name', 
            'last_name',
            'email',
            'phone_number',
            'stack'
        )


class MenteeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mentee
        fields = (
            'id',
            'first_name', 
            'last_name',
            'email',
            'phone_number',
            'stack'
        )
