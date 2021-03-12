import unittest

"""
4)Write a function called parse_tris that takes alist of Triangles as an input parameter. 
The function will return a tuple. The first item in the tuple is the number of triangles 
for which the x coordinates of all three points are the same, or the y coordinates of all three points are the same, 
or the z coordinates of all three points are the same. The second item in the tuple is a list of the perimeters of each of the triangles. 
You must use at least three helper functions in your solution.
"""

class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

class Triangle:
    def __init__(self,p1,p2,p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

def parse_tris(triangles: list) -> tuple:
    same = 0
    perimeters = [] 
    for tri in triangles:
        if are_same(tri):
            same += 1
        perimeters.append(perimeter(tri))
    return same, perimeters

def are_same(triangle: Triangle) -> bool:
    if triangle.p1.x == triangle.p2.x == triangle.p3.x or \
        triangle.p1.y == triangle.p2.y == triangle.p3.y or \
        triangle.p1.z == triangle.p2.z == triangle.p3.z:
        return True
    return False

def len_vector(point: Point):
    return (point.x ** 2 + point.y ** 2 + point.z ** 2) ** (1/2)

def perimeter(triangle: Triangle) -> int:
    return len_vector(triangle.p1) + len_vector(triangle.p2) + len_vector(triangle.p3)

class Tests(unittest.TestCase):
    def test_parse_tris(self):
        input1 = [Triangle(Point(1,2,4),Point(1,4,2),Point(1,1,1)),Triangle(Point(0,0,0),Point(0,4,2),Point(0,2,1))]
        self.assertEqual(parse_tris(input1), (2, [10.897202197480556, 6.708203932499369]))

if __name__ == '__main__':
   unittest.main()