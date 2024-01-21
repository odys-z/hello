'''
628. Maximum Product of Three Numbers
https://leetcode.com/problems/maximum-product-of-three-numbers
'''
import unittest
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        n = sorted(nums)
        return max(n[-1] * n[-2] * n[-3], n[0] * n[1] * n[-1])


class Solution2:
    def maximumProduct(self, nums: List[int]) -> int:
        a, b, c, y, z = -1001, -1001, -1001, 1001, 1001
        for v in nums:
            if v < y:
                (y, z) = (z, v) if v < z else (v, z)

            if v > c:
                if v > b:
                    (a, b, c) = (a, v, b) if a > v else (v, a, b)
                elif v <= b:
                    a, b, c = a, b, v

        return max(a*b*c, y*z*a)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution2()
        self.assertEqual(0, s.maximumProduct([0,0,0]))
        self.assertEqual(6, s.maximumProduct([1,2,3]))
        self.assertEqual(-6, s.maximumProduct([-1,-2,-3]))
        self.assertEqual(-100 * -99 * 3, s.maximumProduct([-100,-99,-3, 0, 2, 3]))
        self.assertEqual(0, s.maximumProduct([-100,-99,-3, 0, -2, -3, -4, -5]))


if __name__ == '__main__':
    unittest.main()
