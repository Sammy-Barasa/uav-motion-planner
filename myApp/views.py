from rest_framework import generics
from .models import Location, Obstacle, DroneFlight
from .serializers import LocationSerializer, ObstacleSerializer, DroneFlightSerializer


class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class ObstacleList(generics.ListCreateAPIView):
    queryset = Obstacle.objects.all()
    serializer_class = ObstacleSerializer


class ObstacleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Obstacle.objects.all()
    serializer_class = ObstacleSerializer


class DroneFlightList(generics.ListCreateAPIView):
    queryset = DroneFlight.objects.all()
    serializer_class = DroneFlightSerializer


class DroneFlightDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DroneFlight.objects.all()
    serializer_class = DroneFlightSerializer
