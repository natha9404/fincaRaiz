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

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PropertiesDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Properties.objects.all()
    serializer_class = PropertiesSerializer

    def get(self, request, *args, **kwargs):
        print (self.kwargs.get('pk'))
        category = self.kwargs.get('pk')
        propertie = Properties.objects.filter(category=category)
        serializer = PropertiesSerializer(propertie, many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)