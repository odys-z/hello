'''
15. 3Sum
https://leetcode.com/problems/3sum/

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
Created on 21 Dec 2019
@author: ody
'''
import unittest
from typing import List

'''
test practice
'''
class Solution0():
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sum2 = dict()
        for ix in range(1, len(nums)):
            for jx in range(ix):
                s = nums[ix] + nums[jx]
                if s in sum2:
                    sum2[s].append()
                else: sum2[s] = nums[jx], nums[ix]
        
        for n3 in nums():
            if -n3 in sum2:
                

class Solution():
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pass

class Test(unittest.TestCase):

    def testName(self):
        s = Solution()
        self.assertEq([[-1, 0, 1], [-1, -1, 2]], s.threeSum([-1, 0, 1, 2, -1, -4]))


    def assertEq(self, a: List[List[int]], b: List[List[int]]) -> None:
        pass

