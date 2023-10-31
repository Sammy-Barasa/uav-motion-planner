from math import radians, sin,cos, asin, sqrt, degrees,atan
from pygc import great_circle, great_distance

class Geocalculation:
    reference_lat = -1.4319392
    reference_long= 36.7052538
    ratio = 1
    def distance_between_set_lat_long(self,set_one,set_two):
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
            return distance

    def get_distance_and_azimuth_result_points(self,list_of_result_points):
            distance_list = []
            azimuth_angle_list = []
            height_list =[]

            for i in range(len(list_of_result_points)):
                calc_distance = (sqrt((list_of_result_points[i][0])**2+list_of_result_points[i][1]**2))*self.ratio
                calc_azimuth = 90-(degrees(atan((list_of_result_points[i][1])/(list_of_result_points[i][0]))))
                distance_list.append(calc_distance)
                azimuth_angle_list.append(calc_azimuth)
                height_list.append(list_of_result_points[i][2])

            return {"distance_list":distance_list,
                    "angle_list":azimuth_angle_list,
                    "height_list":height_list}

    def get_new_lat_long_from_calculated_distance_and_azimuth(self,data):
        final_waypoints=[]
        res=great_circle(distance=data["distance_list"], azimuth=data["angle_list"], latitude=self.reference_lat, longitude=self.reference_long) 
        
        for i in range(len(data["distance_list"])):
                final_waypoints.append([res["latitude"][i],res["longitude"][i],data["height_list"][i]])
        return final_waypoints
    
    

    def get_azimuth_distance_set_lat_long_map_points(self,set_two_lat_long):
        # [lat,long,height] 
        result= great_distance(start_latitude=self.reference_lat, start_longitude=self.reference_long, end_latitude=set_two_lat_long[0], end_longitude=set_two_lat_long[1])
        return result

    def get_single_map_point_to_space_point(self,set_two_lat_long):
            # [lat,long,height] 
        point_distance_and_azimuth= self.get_azimuth_distance_set_lat_long_map_points(set_two_lat_long)
        # {
        # 'distance': array(2.67369853), 
        # 'azimuth': 67.76046817353448, 
        # 'reverse_azimuth': 247.76046761797653
        # }

        calc_theta = 90-(point_distance_and_azimuth["azimuth"])
        x = (point_distance_and_azimuth["distance"]/self.ratio)* cos(radians(calc_theta))
        y = (point_distance_and_azimuth["distance"]/self.ratio)* sin(radians(calc_theta))
        h = set_two_lat_long[2]

        return {"x":x,"y":y,"h":h}
    
    def get_multiple_map_point_to_space_point(self,list_of_set_two_lat_long):
        # [[lat,long,height],[lat,long,height],[lat,long,height]] 
        # 
        multiple_point_result = []   
        for i in range(len(list_of_set_two_lat_long)):
              multiple_point_result.append(self.get_single_map_point_to_space_point(list_of_set_two_lat_long[i]))

        return multiple_point_result 
    
    def test_functions(self):
        # marke1 and marker3
        # area = " maerke1 and marker3"
        # set_one = [-1.4319392,36.7052538]
        # set_two = [-1.4318248,37.1412825]

        # marke1 and marker2
        # area = " maerke1 and marker2"
        # set_one = [-1.4319392,36.7052538]
        # set_two = [-1.1528961,36.7021043]

        # marke1 and marker4
        # area = " maerke1 and marker4"
        # set_one = [-1.4319392,36.7052538]
        # set_two = [-1.15548797882537,37.1431655215938]

        # marke3 and marker4
        # area = " maerke3 and marker4"
        # set_one = [-1.4318248,37.1412825]
        # set_two = [-1.15548797882537,37.1431655215938]

        # marke3 and marker4
        area = " maerke2 and marker4"
        set_one = [-1.1528961,36.7021043]
        set_two = [-1.15548797882537,37.1431655215938]

        print(area)
        self.distance_between_set_lat_long(set_one,set_two)

        list_of_result_points = [[2.474801212023016, 1.011940112109814, 6.416164668457312], [41.770368304609654, 50.27496815775435, 53.0987462545056], [60.250551647885395, 51.6634602732759, 61.23890031999082], [66.92375162031392, 60.49669795433024, 70.77233989831947], [100, 100, 100]]

        print("List of result points: ",list_of_result_points)

        data=self.get_distance_and_azimuth_result_points(list_of_result_points)
        print("azimuth and distance: ",data)

        res=self.get_new_lat_long_from_calculated_distance_and_azimuth(data)
        print(res) 

        self.get_azimuth_distance_set_lat_long_map_points(res[0])
        l = self.get_single_map_point_to_space_point(res[0])
        print("l: ",l)


if __name__ ==  "__main__":
    gc =  Geocalculation()
    gc.test_functions()