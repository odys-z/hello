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
                    sum2[s].add((nums[jx], nums[ix], jx, ix))
                else: sum2[s] = set([(nums[jx], nums[ix], jx, ix)])
        
        ans = []
        anset = set()
        for i3, n3 in enumerate(nums):
            if -n3 in sum2:
                # merge sums
                for n1, n2, i1, i2 in sum2[-n3]:
                    if n3 != n1 and n3 != n2:
                        n1, n2, n3_ = sorted([n1, n2, n3])
                        if (n1, n2, n3_) not in anset and i3 != i1 and i3 != i2: 
                            ans.append([n1, n2, n3_])
                            anset.add((n1, n2, n3_))
                    elif (n3 == 0 and # n2 == 0 and n1 == 0 and
                          (0, 0, 0) not in anset and i3 != i1 and i3 != i2):
                        ans.append([n1, n2, n3])
                        anset.add((n1, n2, n3))
        return ans

class Solution():
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pass

class Test(unittest.TestCase):

    def testName(self):
        s = Solution0()
        self.assertEqual([], s.threeSum([0, 0]))
        self.assertEqual([[0, 0, 0]], s.threeSum([0, 0, -0]))
        self.assertEqual([[-1, 0, 1]], s.threeSum([0, 1, -1]))
        self.assertEqual([[-1, 0, 1]], s.threeSum([-1, 0, 1, 0]))
        self.assertEqual([], s.threeSum([0, -1, -1, -3, -3, -4, -1]))
        self.assertEqual([[-1, -1, 2]], s.threeSum([2, -1, -1]))
        self.assertEqual([], s.threeSum([-2, 4]))
        self.assertEqual([], s.threeSum([-2, 4, 4]))
        self.assertEqual([], s.threeSum([-2, 2, 4, 4]))
        self.assertEqual([[-3,-1,4],[-2,1,1],[-2, -2, 4]], s.threeSum([ -1, 1, 1, -3, -2, 4, -2,-3,-4]))
        self.assertEqual([[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]], s.threeSum([0, -1, 1, -2, 2, 3, 3, 3, 3, 3, 3, 4,4,4]))
        self.assertEqual([[-1, 0, 1], [-1, -1, 2]], s.threeSum([-1, 0, 1, 2, -1, -4]))


