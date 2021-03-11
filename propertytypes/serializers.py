from rest_framework import serializers
from .models import PropertyTypes

class PropertyTypesSerializer(serializers.ModelSerializer):

    class Meta:
        model = PropertyTypes
        fields = '__all__'