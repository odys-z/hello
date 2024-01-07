'''
 * 448. Find All Numbers Disappeared in an Array
 * https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
'''
import unittest
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.insert(0, 0)

        for v in nums:
            vx = v if v >= 0 else -v
            if nums[vx] > 0:
                nums[vx] = - nums[vx] if nums[vx] > 0 else nums[vx]

        res = []
        for x, v in enumerate(nums):
            if v > 0:
                res.append(x)
        return res


class Solution2:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        res = []

        for i in range(1, len(nums)+1):
            if i in s:
                continue
            res.append(i)
        return res


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution2()
        self.assertEqual([5, 6], s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))  # add assertion here


if __name__ == '__main__':
    unittest.main()
