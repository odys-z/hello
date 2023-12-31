'''
 * 268. Missing Number
 * https://leetcode.com/problems/missing-number/
'''
import unittest
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        v = 0
        for x, n in enumerate(nums):
            v ^= (x+1) ^ n
        return v


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()
        self.assertEqual(2, s.missingNumber([0,1,3]))
        self.assertEqual(0, s.missingNumber([2,1,3]))
        self.assertEqual(6, s.missingNumber([2,1,3,5,0,7,4]))


if __name__ == '__main__':
    unittest.main()
