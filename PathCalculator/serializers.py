from rest_framework import serializers

from PathCalculator.models import Location, Obstacle, DroneFlight,DroneFlightPath,HiddenObstacle
import json


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


class CreateDroneFlightSerializer(serializers.Serializer):
    json_data = serializers.JSONField()
    id = serializers.IntegerField(read_only=True)

    def validate(self, attrs):
        return attrs
    
    def create(self, validated_data):
        # validated_data.pop("fcm_token",None)
        print("data before register: ",validated_data)
        # DroneFlight.objects.create_user(**validated_data)
        return validated_data
    

class GetDroneFlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = DroneFlightPath
        fields = ['id','flight_data_path','start','end','date_field']
        read_only_fields = ['id']


        def validate(self, attrs):
            return attrs
 
        

class CreateObstacleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obstacle
        fields = ['id','obstacle_data']
        read_only_fields = ['id']
    # json_data = serializers.JSONField()
    # id = serializers.IntegerField(read_only=True)

        def validate(self, attrs):
            return attrs
        
        # def create(self, validated_data):
        #     # validated_data.pop("fcm_token",None)
        #     print("data before register: ",validated_data)
        #     # DroneFlight.objects.create_user(**validated_data)
        #     return validated_data

        def create(self, validated_data):
            
            data = validated_data['obstacle_data']
            print(data)
            obs=Obstacle.objects.create(description="building",obstacle_data=data)
            print(obs)
            return obs
        
class CreateHiddenObstacleSerializer(serializers.ModelSerializer):
    class Meta:
        model = HiddenObstacle
        fields = ['id','hidden_obstacle_data']
        read_only_fields = ['id']
    # json_data = serializers.JSONField()
    # id = serializers.IntegerField(read_only=True)

        def validate(self, attrs):
            return attrs
        
        # def create(self, validated_data):
        #     # validated_data.pop("fcm_token",None)
        #     print("data before register: ",validated_data)
        #     # DroneFlight.objects.create_user(**validated_data)
        #     return validated_data

        def create(self, validated_data):
            
            data = validated_data['hidden_obstacle_data']
            print(data)
            h_obs=HiddenObstacle.objects.create(description="anythininair",hidden_obstacle_data=data)
            print(h_obs)
            return h_obs