from django.shortcuts import render

# Create your views here.
from .models import States
from .serializers import StatesSerializer
from rest_framework import mixins
from rest_framework import generics

class StateList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = States.objects.all()
    serializer_class = StatesSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)