from rest_framework import serializers
from bridgemate import models

class ReceivedDataSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = models.ReceivedData