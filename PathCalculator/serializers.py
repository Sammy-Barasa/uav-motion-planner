from rest_framework import serializers

from .models import Location, Obstacle, DroneFlight


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class ObstacleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obstacle
        fields = '__all__'


class DroneFlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = DroneFlight
        fields = '__all__'
