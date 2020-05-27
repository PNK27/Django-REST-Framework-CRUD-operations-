from solarsystem.viewsets import PlanetViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('v1/claim',PlanetViewSet)