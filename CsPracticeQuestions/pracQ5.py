import unittest

"""
5) Write a function called middle that takes a list of lists of integers representing a 
table (each list withinthe list represents the row of a table). The function returns the 
value in the middle row and middlecolumn of the table.If there is no exact middle, 
it returns the average of the values. You may assumethat the list is not empty, that no row is empty, 
and that each row has the same length.
"""

def middle(nums: list):
    if len(nums) % 2 == 0:
        mid = int(len(nums) / 2)
        return (avg_in_arr(nums[mid]) + avg_in_arr(nums[mid - 1])) / 2
    return avg_in_arr(nums[len(nums) // 2])

def avg_in_arr(arr: list) -> int:
    if len(arr) % 2 == 0:
        mid = int(len(arr) / 2)
        return (arr[mid] + arr[mid-1]) / 2
    return arr[len(arr) // 2]

class Tests(unittest.TestCase):
    def test_middle(self):
        in1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        ans1 = 5
        self.assertEqual(middle(in1), ans1)

        in2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        ans2 = 6.5
        self.assertEqual(middle(in2), ans2)

        in3 = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]]
        ans3 = 8.5
        self.assertEqual(middle(in3), ans3)

if __name__ == '__main__':
   unittest.main()