'''
169. Majority Element
https://leetcode.com/problems/majority-element/description/
'''

import unittest
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c, v0 = 0, None

        for x, n in enumerate(nums):
            if c == 0:
                c += 1
            else:
                c += 1 if n == v0 else -1
            v0 = n
        return v0


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()
        self.assertEqual(2, s.majorityElement([2,2,1,1,2]))  # add assertion here


if __name__ == '__main__':
    unittest.main()
