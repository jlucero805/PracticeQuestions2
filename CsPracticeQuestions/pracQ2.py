import unittest

"""
2)Write a function shuffle that takes two lists as arguments. 
It returns a new list consisting of alternating members of the input lists, 
starting with the first list. If one input list runs out of members, 
the remaining items will be from the other list. 
For example: shuffle([2, 7, 1, 4], [6, -1]) will return: [2, 6, 7, -1, 1, 4]
"""

def shuffle(nums1: list, nums2: list) -> list:
    res = []
    len1 = len(nums1)
    len2 = len(nums2)
    i = 0
    j = 0
    while i < len1 and j < len2:
        if i <= j:
            res.append(nums1[i])
            i += 1
        else:
            res.append(nums2[j])
            j += 1
    while i < len1:
        res.append(nums1[i])
        i += 1
    while j < len2:
        res.append(nums2[j])
        j += 1
    return res


class Tests(unittest.TestCase):
    def test_shuffle(self):
        nums1 = [2, 7, 1, 4]
        nums2 = [6, -1]
        ans1 = [2, 6, 7, -1, 1, 4]
        self.assertEqual(shuffle(nums1, nums2), ans1)

        nums3 = [1,3,5,7,9]
        nums4 = [2,4,6,8]
        ans2 = [1,2,3,4,5,6,7,8,9]
        self.assertEqual(shuffle(nums3, nums4), ans2)

if __name__ == '__main__':
   unittest.main()