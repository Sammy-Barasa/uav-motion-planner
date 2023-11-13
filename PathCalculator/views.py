from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import Location, Obstacle, DroneFlight
from .serializers import LocationSerializer, ObstacleSerializer, DroneFlightSerializer, CreateDroneFlightSerializer, CreateObstacleSerializer
from PathCalculator.Geocalculations import Geocalculation
from rest_framework.exceptions import ValidationError
import json

class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class DroneFlightDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DroneFlight.objects.all()
    serializer_class = DroneFlightSerializer


def ComputeNodeView(start_data, end_data):
    # get start from geogalculator
    # get end from geolocalculator
    # {"x":x,"y":y,"h":h}
    from PathCalculator.rrt_algo_api import RRT3d, env3d
    import matplotlib.pyplot as plt
    nmax = 8000

    #goal region
    xg=end_data["x"]
    yg=end_data["y"]
    zg=end_data["h"]
    # xg=5
    # yg=5
    # zg=5
    epsilon=5
    xgmin=xg-epsilon
    xgmax=xg+epsilon
    ygmin=yg-epsilon
    ygmax=yg+epsilon
    zgmin=zg-epsilon
    zgmax=zg+epsilon


    #extend step size
    dmax = 5
    #start the root of the tree
    nstart =(start_data["x"],start_data["y"],start_data["h"]) 
    # nstart =(100,100,100) 
    #specify vertices for rectangular obstacles (each object has four vertices)
    #obstacles known a priori
    # vx= [40,40,60,60,70,70,80,80,40,40,60,60]
    # vy= [52,100,100,52,40,60,60,40, 0,48,48, 0]
    serializer= CreateObstacleSerializer(Obstacle.objects.all(),many=True)
    # print(len(serializer.data))
    stored_obstacles = serializer.data
    vx= [400,400,600,600,700,700,800,800,400,400,600,600]
    vy= [520,1000,1000,520,400,600,600,400,0,480,480, 0]
    vz = [0,100,0,600,500,800]
    # print(json.dumps(stored_obstacles,indent=4))
    for i in range(len(stored_obstacles)):
        vx.append(stored_obstacles[i]["obstacle_data"]["space_points"]["A"]["x"])
        vy.append(stored_obstacles[i]["obstacle_data"]["space_points"]["A"]["y"])
        vz.append(stored_obstacles[i]["obstacle_data"]["space_points"]["A"]["h"])

        vx.append(stored_obstacles[i]["obstacle_data"]["space_points"]["C"]["x"])
        vy.append(stored_obstacles[i]["obstacle_data"]["space_points"]["C"]["y"])
        vz.append(stored_obstacles[i]["obstacle_data"]["space_points"]["C"]["h"])

        vx.append(stored_obstacles[i]["obstacle_data"]["space_points"]["B"]["x"])
        vy.append(stored_obstacles[i]["obstacle_data"]["space_points"]["B"]["y"])
        vz.append(stored_obstacles[i]["obstacle_data"]["space_points"]["B"]["h"])

        vx.append(stored_obstacles[i]["obstacle_data"]["space_points"]["D"]["x"])
        vy.append(stored_obstacles[i]["obstacle_data"]["space_points"]["D"]["y"])
        vz.append(stored_obstacles[i]["obstacle_data"]["space_points"]["D"]["h"])
    #hidden obstacle
    # hvx= [150,150,250,250,250,250,350,350]
    # hvy= [150,300,300,150,400,600,600,400]
    hvx= [15,15,25,25,25,25,35,35]
    hvy= [15,30,30,15,40,60,60,40]


    #create an RRT tree with a start node
    G=RRT3d(nstart,xgmin=xgmin,xgmax=xgmax,ygmin=ygmin,ygmax=ygmax,zgmin=zgmin,zgmax=zgmax,xg=xg,yg=yg,zg=zg,dmax=dmax,nmax=nmax)
    

    #environment instance
    # E=env3d(vx,vy,vz,0,4900,0,3100,0,3000)
    E=env3d(vx,vy,vz,0,4900,0,3100,0,3000,hvx=hvx,hvy=hvy,G=G,xgmin=xgmin,xgmax=xgmax,ygmin=ygmin,ygmax=ygmax,zgmin=zgmin,zgmax=zgmax)
    G.set_E(E)
    G.set_G(G)

    #balance between extending and biasing	
    for i in range(0,nmax):
        if i%10!=0: G.expand()
        else: G.bias()
	#check if sample is in goal, if so STOP!		
        if E.ingoal()==1:
            print('found')
            break
    G.path_to_goal()
    G.prun()
    test_ans=G.returnpath()
    # print("test_ans: ",test_ans)
    return test_ans

class CreateDroneFlightView(generics.GenericAPIView):
    serializer_class = CreateDroneFlightSerializer
    queryset = DroneFlight.objects.all()
    def post(self,request):
        gc = Geocalculation()
        data = request.data
        start_location = data["start_location"]
        end_location = data["end_location"]

        res1 = gc.get_single_map_point_to_space_point([start_location["lat"],start_location["long"],start_location["h"]])
        res2 = gc.get_single_map_point_to_space_point([end_location["lat"],end_location["long"],end_location["h"]])
        vals=ComputeNodeView(res1,res2)
        print("found space points ...")
        data=gc.get_distance_and_azimuth_result_points(vals)
        # print("azimuth and distance: ",data)

        res=gc.get_new_lat_long_from_calculated_distance_and_azimuth(data)
        # print("New_lat_long",res)
        print("found map points ...")
        flight_data = {
            "map_points":res,
            "space_points":vals
        }

        return Response(flight_data, status=status.HTTP_201_CREATED)
    

class CreateObstacleView(generics.GenericAPIView):
    serializer_class = CreateObstacleSerializer
    queryset = Obstacle.objects.all()

    def get(self,request):
        serializer= self.serializer_class(self.get_queryset(),many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self,request):
        gc = Geocalculation()
        object_map_data = request.data["obstacle_data"]
        
        
        # print(object_map_data)
        res1 = gc.get_mulptiple_object_map_point_to_space_point(object_map_data)
        
        # vals=ComputeNodeView(res1,res2)
        # print("found space points ...")
        # data=gc.get_distance_and_azimuth_result_points(vals)
        # print("azimuth and distance: ",data)

        # res=gc.get_new_lat_long_from_calculated_distance_and_azimuth(data)
        # print("New_lat_long",res)
        new_object_data = {
            "map_points":object_map_data,
            "space_points":res1
        }
        
        serializer = self.serializer_class(data={"obstacle_data":new_object_data})
        
        serializer.is_valid(raise_exception=True)
        # print(new_object_data)
        try:            
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as error:
            return Response(data={"error":error}, status=status.HTTP_400_BAD_REQUEST)
        
class ObstacleList(generics.ListCreateAPIView):
    queryset = Obstacle.objects.all()
    serializer_class = ObstacleSerializer


class ObstacleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Obstacle.objects.all()
    serializer_class = ObstacleSerializer        

class DroneFlightList(generics.ListCreateAPIView):
    queryset = DroneFlight.objects.all()
    serializer_class = DroneFlightSerializer