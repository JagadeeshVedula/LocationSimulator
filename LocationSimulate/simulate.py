from geopy.distance import geodesic,distance
from geopy.point import Point
from robot.libraries.BuiltIn import BuiltIn
from geopy.geocoders import Nominatim


def intermediate_points(sourceLat,sourceLon,desLat,desLon,speed):
    speed = int(speed)*(5/18)
    start = Point(sourceLat,sourceLon)
    end=Point(desLat,desLon)
    total_distance = geodesic(start,end).meters
    total_distance = int(total_distance)
    distance=int(speed)
    num_points = total_distance/distance
    points=[]
    for i in range(round(num_points)+1):
        fraction=i*distance/total_distance
        if fraction >1:
            fraction=1
        lat = start.latitude+(end.latitude-start.latitude)*fraction
        lon=start.longitude+(end.longitude-start.longitude)*fraction
        points.append((lat,lon))
    # print(points)
    oldlocation=''
    for point in points:
        print(point)
        try:
            geolocator = Nominatim(user_agent="my_unique_app_name_1.0")
            Newlocation = geolocator.reverse(f"{point[0]}, {point[1]}")
            if oldlocation != Newlocation.address:
# Print the address
                print(f"user reached {Newlocation.address}")
                oldlocation=Newlocation.address
        except:
            print(f'location not found for the current coordinates: {point}')
        driver=BuiltIn().get_library_instance('AppiumLibrary')
        driver.set_location(point[0],point[1])
    print(f"user reached the destination: {Newlocation.address}")
intermediate_points('17.663702194239555', '82.61622655240457','17.652175430830592', '82.64533666707842',100)