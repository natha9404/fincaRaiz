from rest_framework import serializers
from .models import States

class StatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = States
        fields = '__all__'