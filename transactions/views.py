from django.shortcuts import render

# Create your views here.
from .models import Transactions
from .serializers import TransactionsSerializer
from rest_framework import mixins
from rest_framework import generics

class TransactionList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)