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
        nmin, nmax = nums[0], nums[-1]
        sum2 = dict()
        for ix in range(1, len(nums)):
            for jx in range(ix):
                s = nums[ix] + nums[jx]
                if s < -nmax:
                    continue
                elif s > -nmin:
                    break
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
        print(ans)
        return ans

class Solution1():
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def two_sum(idx):
            target = - nums[idx]
            left, right = 0, len(nums) - 1
            two_sum_set = set()
            while left < right:
                if left == idx or right == idx:
                    if left == idx:
                        left += 1
                    else:
                        right -= 1
                    continue
                if nums[left] + nums[right] > target:
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    two_sum_set.add((nums[left], nums[right]))
                    left += 1
                    right -= 1
            return two_sum_set
        
        if not nums or len(nums) < 3:
            return []
        if len(nums) == 3:
            return [nums] if sum(nums) == 0 else []
        nums.sort() # help to avoid duplicate triplets
        three_set_sum = set()  # using set to hold unique triplets
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: # no need to check this case becasue results would be duplicates
                continue
            two_set_sum = two_sum(i)
            for num1, num2 in two_set_sum:
                candidates = [nums[i], num1, num2]
                candidates.sort()
                three_set_sum.add((candidates[0], candidates[1], candidates[2]))
        return [[num1, num2, num3] for num1, num2, num3 in three_set_sum]
    
class Solution():
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pass
# 311 / 313 test cases passed.
# Status: Time Limit Exceeded

class Test(unittest.TestCase):

    def test0(self):
        s = Solution0()
        self.assertEqual([[0, 0, 0]], [[0, 0, 1]])
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
        # self.assertEqual([[-99927, 27134, 72793]], s.threeSum(case1))
        ans = s.threeSum(case1)

    def test1(self):
        s = Solution1()
        self.assertEqual([], s.threeSum([0, 0]))
        self.assertEqual([[0, 0, 0]], s.threeSum([0, 0, -0]))
        self.assertEqual([[0, 1, -1]], s.threeSum([0, 1, -1]))
        self.assertEqual([[-1, 0, 1]], s.threeSum([-1, 0, 1, 0]))
        self.assertEqual([], s.threeSum([0, -1, -1, -3, -3, -4, -1]))
        self.assertEqual([[2, -1, -1]], s.threeSum([2, -1, -1]))
        self.assertEqual([], s.threeSum([-2, 4]))
        self.assertEqual([], s.threeSum([-2, 4, 4]))
        self.assertEqual([], s.threeSum([-2, 2, 4, 4]))
        self.assertEqual([[-2, -2, 4], [-3, -1, 4], [-2, 1, 1]], s.threeSum([ -1, 1, 1, -3, -2, 4, -2,-3,-4]))
        self.assertEqual([[-1, 0, 1], [-2, -1, 3], [-2, 0, 2]], s.threeSum([0, -1, 1, -2, 2, 3, 3, 3, 3, 3, 3, 4,4,4]))
        self.assertEqual([[-1, -1, 2], [-1, 0, 1]], s.threeSum([-1, 0, 1, 2, -1, -4]))
        # self.assertEqual([[-99927, 27134, 72793]], s.threeSum(case1))

        ans = s.threeSum(case1)
        print(ans)
