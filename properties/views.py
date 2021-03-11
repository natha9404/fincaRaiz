from django.shortcuts import render

# Create your views here.
from .models import Properties
from .serializers import PropertiesSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PropertiesList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView,
                  APIView):
    queryset = Properties.objects.all()
    serializer_class = PropertiesSerializer

    def get(self, request, format=None):
        category = request.data['category']
        propertie = Properties.objects.filter(category=category)
        serializer = PropertiesSerializer(propertie, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)