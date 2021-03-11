from django.shortcuts import render

# Create your views here.
from .models import Reviews
from .serializers import ReviewsSerializer
from rest_framework import mixins
from rest_framework import generics

class ReviewList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)