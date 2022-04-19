from django.shortcuts import render
from rest_framework import viewsets
from .models import Flight
from .serializers import FlightSerializer

class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer