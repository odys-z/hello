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
from utils.hello_case import FileCase
from utils import Assrt

'''
# 311 / 313 test cases passed.
# Status: Time Limit Exceeded
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
        return ans

class Solution02():
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nmin, nmax = nums[0], nums[-1]

        sum2dict = dict() # {sum: {ni, nj}}
        sum2list = [] # [sum]

        for ix in range(1, len(nums)):
            for jx in range(ix):
                s = nums[ix] + nums[jx]
                if s < -nmax:
                    continue
                elif s > -nmin:
                    break
                if s in sum2dict:
                    sum2dict[s].update({nums[ix]: (nums[jx], ix, jx)})
                else:
                    sum2dict[s] = dict({nums[ix]: (nums[jx], ix, jx)})
                    sum2list.append(s)
        sum2list.sort()
        
        ans = []

        n3_ = None # previous n3
        # i, j, l = 0, len(sum2list) - 1, len(sum2list)
        j, l = len(sum2list) // 2, len(sum2list)
        
        for i3, n3 in enumerate(nums):
            if n3 == n3_:
                continue
            n3_ = n3

            s = n3 + sum2list[j]
            while s > 0 and j >= 0:
                j -= 1
                s = n3 + sum2list[j]
            while s < 0 and j < l:
                j += 1
                s = n3 + sum2list[j]

            if s == 0:
                for n1 in sum2dict[-n3]:
                    n2, i1, i2 = sum2dict[-n3][n1]
                    if i3 != i1 and i3 != i2:
                        ans.append([n1, n2, n3])
            # if s != 0, try next n3
       
        return ans


''' wrong '''
class Solution01():
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nmin, nmax = nums[0], nums[-1]

        sum2dict = dict() # {sum: {ni, nj}}
        sum2list = [] # [sum]
        i, j, l = 0, len(nums) - 1, len(nums)
        while i < l and j >= 0 and i < j:
            s = nums[i] + nums[j]
            if s < -nmax:
                i += 1
            elif s > -nmin:
                j -= 1
            else:
                if s in sum2dict:
                    sum2dict[s].update({nums[i]: (nums[j], i, j)})
                else:
                    sum2dict[s] = dict({nums[i]: (nums[j], i, j)})
                    sum2list.append(s)
                i += 1

        sum2list.sort()

        ans = []

        n3_ = None # previous n3
        i, j, l = 0, len(sum2list) - 1, len(sum2list)

        while i < l and j >= 0:
            n3 = nums[i]
            if n3 == n3_:
                i += 1
                continue

            s = n3 + sum2list[j]
            if s < 0:
                i += 1
                n3_ = n3
            elif s > 0:
                j -= 1
            else: # s=0
                for n1 in sum2dict[-n3]:
                    n2, i1, i2 = sum2dict[-n3][n1]
                    if i != i1 and i != i2:
                        ans.append([n1, n2, n3])
                i += 1
                n3_ = n3
        
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

case1 = FileCase().loadArr('case/case1.txt')[0]
veri1 = FileCase().loadArr('case/veri1.txt', 2)[0]

class Test(unittest.TestCase):

    def test1(self):
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
        # self.assertEqual([[-99927, 27134, 72793]], s.threeSum(case1))
        ans = s.threeSum(case1)
        print(ans)
#         Assrt.Eq().int2dArr(veri1, ans)

    def test02(self):
        s = Solution02()
        eq = Assrt.Eq()
        eq.int2dArr([], s.threeSum([0, 0]))
        eq.int2dArr([[0, 0, 0]], s.threeSum([0, 0, -0]))
        eq.int2dArr([[0, 1, -1]], s.threeSum([0, 1, -1]))
        eq.int2dArr([[-1, 0, 1]], s.threeSum([-1, 0, 1, 0]))
        eq.int2dArr([], s.threeSum([0, -1, -1, -3, -3, -4, -1]))
        eq.int2dArr([[-1, -1, 2]], s.threeSum([2, -1, -1]))
        eq.int2dArr([], s.threeSum([-2, 4]))
        eq.int2dArr([], s.threeSum([-2, 4, 4]))
        eq.int2dArr([], s.threeSum([-2, 2, 4, 4]))
        eq.int2dArr([[-3,-1,4],[-2,1,1],[-2, -2, 4]], s.threeSum([ -1, 1, 1, -3, -2, 4, -2,-3,-4]))

        eq.int2dArr([[-5,-3, 8], [-5, 1, 4], [-5, -3, 8], [-3, -1, 4], [-3, 1, 2]], s.threeSum([ -5, -3, -1, 1, 2, 4, 8 ]))
        eq.int2dArr([[-5,-3, 8], [-5, 1, 4], [-5, -3, 8], [-3, -1, 4], [-3, 1, 2], [-1, 0, 1]],
                    s.threeSum([ -5, -3, -1, 0, 1, 2, 4, 8 ]))

        eq.int2dArr([[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]], s.threeSum([0, -1, 1, -2, 2, 3, 3, 3, 3, 3, 3, 4,4,4]))
        eq.int2dArr([[-1, 0, 1], [-1, -1, 2]], s.threeSum([-1, 0, 1, 2, -1, -4]))
        # self.assertEqual([[-99927, 27134, 72793]], s.threeSum(case1))
        ans = s.threeSum(case1)
        print(ans)
#         Assrt.Eq().int2dArr(veri1, ans)

    def test0(self):
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
#         Assrt.Eq().int2dArr(veri1, ans)
