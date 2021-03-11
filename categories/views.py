from django.shortcuts import render

# Create your views here.
from .models import Categories
from .serializers import CategoriesSerializer
from rest_framework import mixins
from rest_framework import generics

class CategoryList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)