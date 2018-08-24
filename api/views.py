# api/views.py
from rest_framework import generics

from bridgemate import models
from . import serializers


class ListReceivedData(generics.ListCreateAPIView):
    queryset = models.ReceivedData.objects.all()
    serializer_class = serializers.ReceivedDataSerializer


class DetailReceivedData(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ReceivedData.objects.all()
    serializer_class = serializers.ReceivedDataSerializer