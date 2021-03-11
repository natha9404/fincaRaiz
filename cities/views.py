from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from .models import Cities
from .serializers import CitiesSerializer
from rest_framework import mixins
from rest_framework import generics

class CitiesList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)