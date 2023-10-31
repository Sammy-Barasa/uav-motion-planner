from math import radians, sin,cos, asin, sqrt, degrees,atan
from pygc import great_circle, great_distance
# from geopy.distance import geodesic as GD

reference_lat = -1.4319392
reference_long= 36.7052538
def distance_between_set_lat_long(set_one,set_two):
        # start latitude and longitude
        # print(set_one)
        slat = radians(float(set_one[0]))
        slong = radians(float(set_one[1]))


        # end latitude and longitude
        elat = radians(float(set_two[0]))
        elong = radians(float(set_two[1]))
        
        # calculate distance using harversine formula
        d_lat = elat - slat
        d_long = elong - slong
        P = sin(d_lat/2)**2 + cos(slat)*cos(elat)*sin(d_long/2)**2
        # distance = 6371.01* acos(sin(slat))*sin(elat) + cos(slat)*cos(elat)*cos(slong-elong)
        Q = 2 * asin(sqrt(P))
        distance = Q * 6371
        print(f"The distance is {distance:.10f} km")

def get_distance_and_azimuth_result_points(list_of_result_points):
        # [[x,y,z],[x,y,z]]
        # [[2.474801212023016, 1.011940112109814, 6.416164668457312], 
        # [41.770368304609654, 50.27496815775435, 53.0987462545056], 
        # [60.250551647885395, 51.6634602732759, 61.23890031999082], 
        # [66.92375162031392, 60.49669795433024, 70.77233989831947], 
        # [100, 100, 100]]
        distance_list = []
        azimuth_angle_list = []
        height_list =[]

        for i in range(len(list_of_result_points)):
            calc_distance = sqrt((list_of_result_points[i][0])**2+list_of_result_points[i][1]**2)
            calc_azimuth = 90-(degrees(atan((list_of_result_points[i][1])/(list_of_result_points[i][0]))))
            distance_list.append(calc_distance)
            azimuth_angle_list.append(calc_azimuth)
            height_list.append(list_of_result_points[i][2])

        return {"distance_list":distance_list,
                "angle_list":azimuth_angle_list,
                "height_list":height_list}

def get_new_lat_long_from_calculated_distance_and_azimuth(data):
      
      # data =
      # {
      # 'distance_list': [2.6736985300380094, 65.36310956163233, 79.36776487518634, 90.21440569174601, 141.4213562373095], 
      # 'angle_list': [67.76046817545937, 39.7211001677931, 49.38767175894157, 47.88753678279864, 45.0], 
      # 'height_list': [6.416164668457312, 53.0987462545056, 61.23890031999082, 70.77233989831947, 100]
      # }
 
      final_waypoints=[]
      res=great_circle(distance=data["distance_list"], azimuth=data["angle_list"], latitude=reference_lat, longitude=reference_long) 
      
      for i in range(len(data["distance_list"])):
             final_waypoints.append([res["latitude"][i],res["longitude"][i],data["height_list"][i]])
      return final_waypoints

def get_azimuth_distance_set_lat_long_map_points(set_two_lat_long):
       # [lat,long,height] 
       result= great_distance(start_latitude=reference_lat, start_longitude=reference_long, end_latitude=set_two_lat_long[0], end_longitude=set_two_lat_long[1])
       return result

def get_single_map_point_to_space_point(set_two_lat_long):
        # [lat,long,height] 
       point_distance_and_azimuth= get_azimuth_distance_set_lat_long_map_points(set_two_lat_long)
       # {
       # 'distance': array(2.67369853), 
       # 'azimuth': 67.76046817353448, 
       # 'reverse_azimuth': 247.76046761797653
       # }

       calc_theta = 90-(point_distance_and_azimuth["azimuth"])
       x = point_distance_and_azimuth["distance"]* cos(radians(calc_theta))
       y = point_distance_and_azimuth["distance"]* sin(radians(calc_theta))
       h = set_two_lat_long[2]

       return {"x":x,"y":y,"h":h}

def get_multiple_map_point_to_space_point(list_of_set_two_lat_long):
        # [[lat,long,height],[lat,long,height],[lat,long,height]] 
        # 
        multiple_point_result = []   
        for i in range(len(list_of_set_two_lat_long)):
              multiple_point_result.append(get_single_map_point_to_space_point(list_of_set_two_lat_long[i]))

        return multiple_point_result 
# Abuja and Dakar
# set_one = [9.072264 , 7.491302]
# set_two = [14.716677 , -17.467686]

# Nairobi and Cairo
# set_one = [36.817223,-1.286389]
# set_two = [31.233334,30.033333]

# marke1 and marker3
# area = " maerke1 and marker3"
# set_one = [-1.4319392,36.7052538]
# set_two = [-1.4318248,37.1412825]

# marke1 and marker2
# area = " maerke1 and marker2"
# set_one = [-1.4319392,36.7052538]
# set_two = [-1.1528961,36.7021043]

# marke1 and marker4
area = " maerke1 and marker4"
set_one = [-1.4319392,36.7052538]
set_two = [-1.15548797882537,37.1431655215938]

# marke3 and marker4
# area = " maerke3 and marker4"
# set_one = [-1.4318248,37.1412825]
# set_two = [-1.15548797882537,37.1431655215938]

# marke3 and marker4
# area = " maerke2 and marker4"
# set_one = [-1.1528961,36.7021043]
# set_two = [-1.15548797882537,37.1431655215938]

print(area)
distance_between_set_lat_long(set_one,set_two)

list_of_result_points = [[2.474801212023016, 1.011940112109814, 6.416164668457312], [41.770368304609654, 50.27496815775435, 53.0987462545056], [60.250551647885395, 51.6634602732759, 61.23890031999082], [66.92375162031392, 60.49669795433024, 70.77233989831947], [100, 100, 100]]
# list_of_result_points = [[3551.1571154482776, 2277.3305193309034, 1329.5361396428564], [100, 100, 100]]
print("List of result points: ",list_of_result_points)
data=get_distance_and_azimuth_result_points(list_of_result_points)
print("azimuth and distance: ",data)
res=get_new_lat_long_from_calculated_distance_and_azimuth(data)

print("Calculated results: ",res)

get_azimuth_distance_set_lat_long_map_points(res[0])
l = get_single_map_point_to_space_point(res[0])
print("l: ",l)
# [[2.474801212023016, 1.011940112109814, 6.416164668457312], [41.770368304609654, 50.27496815775435, 53.0987462545056], [60.250551647885395, 51.6634602732759, 61.23890031999082], [66.92375162031392, 60.49669795433024, 70.77233989831947], [100, 100, 100]]

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a new figure
fig = plt.figure()

# Get the current 3D axis
# ax = fig.gca(projection='3d')
ax=fig.add_subplot(111, projection='3d')
# Now, you can use 'ax' to plot your 3D data, such as scatter plots or surfaces.
# For example:
ax.scatter([1, 2, 3], [4, 5, 6], [7, 8, 9])

# Finally, show the plot
plt.show()