from django.shortcuts import render

# Create your views here.
from .models import PropertyTypes
from .serializers import PropertyTypesSerializer
from rest_framework import mixins
from rest_framework import generics

class PropertyTypeList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = PropertyTypes.objects.all()
    serializer_class = PropertyTypesSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)