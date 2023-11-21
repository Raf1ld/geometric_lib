from math import pi
import unittest
def area(r):
    '''принимает число r, возвращает квадрат числа r умноженный на число π'''
    if r < 0:
        raise ValueError
    return pi * r * r

def perimeter(r):
    '''принимает число r,возвращает удвоенное число r умноженное на число π'''
    if r < 0:
        raise ValueError
    return 2 * pi * r
    
class cicleTestcase (unittest.TestCase):
    def test_area_perimeter (self):
        self.assertEqual(area(0),0)
        self.assertEqual(area(1),pi)
        self.assertEqual(area(3),pi*3*3)
        self.assertEqual(perimeter(0),0)
        self.assertEqual(perimeter(1),2*pi)
        self.assertEqual(perimeter(3),2*pi*3)

    def test_value (self):
        self.assertEqual(ValueError,area,-2)
        self.assertEqual(ValueError,perimeter,-2)
