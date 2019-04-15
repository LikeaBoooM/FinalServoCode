import pandas,os,geopy
from math import pi,cos,sqrt
from geopy.geocoders import Nominatim
import unittest
class tesGeopy(unittest.TestCase):

    def test_getLatLon(self):
        nom = Nominatim()
        pointA = 'Sandomierz'
        pointB = 'Rzeszów'
        n = nom.geocode(pointA)
        d = nom.geocode(pointB)

        x1 = n.longitude
        y1 = n.latitude
        x2 = d.longitude
        y2 = d.latitude
        distance = self.obliczOdlegloscA(x1, y1, x2, y2)
        expectedDistance = 77.58283254164151
        self.assertEqual(expectedDistance, distance)

    def obliczOdlegloscA(self, x2,y2,x1,y1):
        return sqrt(pow((x2-x1),2)+(cos((x1*pi)/180))*pow((y2-y1),2))*(40075.704/360)
        
if __name__ == '__main__':
    unittest.main()