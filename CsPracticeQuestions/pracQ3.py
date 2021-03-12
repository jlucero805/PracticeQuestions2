import unittest

"""
3)The lists_range function takes a list of integer lists and returns a tuple containing the smallest and largest items in the list of lists. 
For example: lists = [[3, 4, 18], [-1, 0], [7, -4, 17]] lists_range(lists) will return (-4, 18) You must NOT change the original input list. 
You MAY assume the original input list has at least one integer list in it containing at least one integer. For example: lists = [[1]]will return (1,1)
"""

def min_and_max(array: list) -> tuple:
    valMin = array[0][0]
    valMax = array[0][0]
    for subArr in array:
        for val in subArr:
            if val < valMin:
                valMin = val
            if val > valMax:
                valMax = val
    return valMin, valMax


class Tests(unittest.TestCase):
    def test_min_and_max(self):
        input1 = [[3, 4, 18], [-1, 0], [7, -4, 17]]
        output1 = (-4, 18) 
        self.assertEqual(min_and_max(input1), output1)

if __name__ == '__main__':
   unittest.main()