import unittest
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        bits = [False] * 1001
        for n in nums1:
            bits[n] = True

        res = []
        for m in nums2:
            if bits[m]:
                bits[m] = False
                res.append(m)
        return res


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()
        self.assertEqual([2], s.intersection([1,2,2,1], [2,2]))


if __name__ == '__main__':
    unittest.main()
