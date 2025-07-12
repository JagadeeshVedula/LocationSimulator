from geopy.distance import geodesic,distance
from geopy.point import Point
from robot.libraries.BuiltIn import BuiltIn


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
    for point in points:
        print(point)
        driver=BuiltIn().get_library_instance('AppiumLibrary')
        driver.set_location(point[0],point[1])
# intermediate_points('17.6628357','82.6198010','17.650833','82.606044',10)