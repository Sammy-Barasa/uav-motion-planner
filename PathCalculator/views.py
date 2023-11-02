from rest_framework import generics
from .models import Location, Obstacle, DroneFlight
from .serializers import LocationSerializer, ObstacleSerializer, DroneFlightSerializer, CreateDroneFlightSerializer
from Geocalculations import Geocalculation

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

class CreateDroneFlightView(generics.GenericAPIView):
    serializer_class = CreateDroneFlightSerializer
    def post(self,request):
        gc = Geocalculation()
        data = request.data
        start_location = data["start_location"]
        end_location = data["end_location"]

        res1 = gc.get_single_map_point_to_space_point([start_location["lat"],start_location["long"]])
        res2 = gc.get_single_map_point_to_space_point([end_location["lat"],end_location["long"]])
        
        pass