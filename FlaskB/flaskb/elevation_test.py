import unittest
import sys
sys.path.append('../flaskb')
from elevation import evalute

class ElevationTest(unittest.TestCase):
    
    def test_calculate_elevation(self):
        latitude = 22.123456
        longtitude = 65.432165
        
        result = evalute(longtitude, latitude)
        expectedEvaluation = 10.77192401885986
        self.assertEqual(expectedEvaluation, result)
        
if __name__ == '__main__':
    unittest.main()