from rest_framework import viewsets
from . import models
from . import serializers

class PlanetViewSet(viewsets.ModelViewSet):
    queryset = models.Planet.objects.all()
    serializer_class = serializers.PlanetSerializer