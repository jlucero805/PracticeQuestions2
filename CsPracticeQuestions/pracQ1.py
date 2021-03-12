import unittest

"""
1)Consider a list with elements denoting the distance between two cities. 
For example: [('San Luis Obispo', 'Atascadero', 16.8),('Atascadero', 'San Francisco', 214.6)]. 
Write a function that, given a route and a list with distances as above, computes total distance traveled. 
A route will be a list of the names of cities visited (in that order). 
For example: ['Atascadero', 'San Luis Obispo', 'Atascadero', 'San Francisco', 'Atascadero']. 
"""

def distanceSum(cities: list, route: list) -> int:
    sum = 0
    for i in range(len(route) - 1):
        for city in cities:
            if route[i] in city and route[i+1] in city:
                sum += city[2]
    return sum


class Tests(unittest.TestCase):
    def test_distanceSum(self):
        cities1 = [('San Luis Obispo', 'Atascadero', 16.8),('Atascadero', 'San Francisco', 214.6)]
        route1 = ['Atascadero', 'San Luis Obispo', 'Atascadero', 'San Francisco', 'Atascadero']
        ans1 = 462.79999999999995
        self.assertEqual(distanceSum(cities1, route1), ans1)

if __name__ == '__main__':
   unittest.main()