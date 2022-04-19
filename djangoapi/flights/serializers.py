from rest_framework import serializers
from .models import Flight

class FlightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flight
        fields = ('id', 'url', 'name', 'code', 'price')
