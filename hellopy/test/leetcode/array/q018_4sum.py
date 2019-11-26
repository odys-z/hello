'''
18. 4Sum
https://leetcode.com/problems/4sum/

Given an array nums of n integers and an integer target, are there elements
a, b, c, and d in nums such that a + b + c + d = target? Find all unique
quadruplets in the array which gives the sum of target.

Note:
The solution set must not contain duplicate quadruplets.

Example:
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

Created on 26 Nov 2019

@author: odys-z@github.com
'''
import unittest
from typing import List
from _collections import defaultdict

class Solution:
    def fourSum_back(self, nums: List[int], target: int) -> List[List[int]]:
        ''' Check the example, there are two '0', but only output [-1, 0, 0, 1] once.
            So this solution doen't show the question understanding.
        '''
        sums = []
        for i, v0 in enumerate(nums[:-1]):
            for j in range(i + 1, len(nums)):
                sums.append((v0 + nums[j], i, j))
        
        buff = defaultdict(list)
        for s, i, j in sums:
            buff[target - s].append((i, j))
        
        reslt = []
        duplicatings = set()
        for s, i, j in sums:
            if s in buff:
                diffs = buff[s]
                for d in diffs:
                    k, l = d
                    ijkl = tuple(sorted((i, j, k, l)))
                    if i < k and j < l and ijkl not in duplicatings:
                        reslt.append([nums[i], nums[k], nums[j], nums[l]]) 
                        diffs.remove(d)
                        duplicatings.add(ijkl)
                if len(diffs) == 0:
                    buff.pop(s)
        
        print(reslt)
        return reslt
            
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or len(nums) < 4:
            return []
        
        mxSum = - float("inf")
        mnSum = float("inf")
        sums = []
        
        # task in this n^2 iteration slow down things (188ms)
        for i, v0 in enumerate(nums[:-1]):
            for j in range(i + 1, len(nums)):
                s = v0 + nums[j]
                sums.append((s, i, j))
                if mxSum < s:
                    mxSum = s
                if mnSum > s:
                    mnSum = s
        
        buff = defaultdict(list)
        for s, i, j in sums:
            buff[target - s].append((i, j))
        
        reslt = []
        duplicatings = set()
        for s, i, j in sums:
            if mnSum > target - s or target - s > mxSum:
                continue

            if s in buff:
                diffs = buff[s]
                for d in diffs:
                    k, l = d
                    answ = sorted((nums[i], nums[k], nums[j], nums[l]))
                    if i < k and j < l and j != k and i != l and tuple(answ) not in duplicatings:
                        reslt.append(answ) 
                        duplicatings.add(tuple(answ))
        
        return reslt

    def fourSumRef(self, n: List[int], t: int) -> List[List[int]]:
        n.sort()
        if not n:
            return []

        L, N, S, M = len(n), {j:i for i,j in enumerate(n)}, set(), n[-1]

        for i in range(L-3):
            a = n[i]
            if a + 3*M < t: continue
            if 4*a > t: break
            for j in range(i+1, L-2):
                b = n[j]
                if a + b + 2*M < t: continue
                if a + 3*b > t: break
                for k in range(j+1, L-1):
                    c = n[k]
                    d = t - (a+b+c)
                    if d > M:
                        # diff is too large, try smaller
                        continue
                    if d < c:
                        # no element can get smaller diff, so stop
                        break

                    if d in N and N[d] > k:
                        S.add((a,b,c,d))
        return S

class Test(unittest.TestCase):


    def test1(self):
        s = Solution()
        self.assertEqual([], s.fourSum([], 1))

        self.assertEqual([[-4,5,5,5],[0,1,5,5]],
            sorted(s.fourSum([0,1,5,0,1,5,5,-4], 11)))

        self.assertEqual([[-1,0,1,2]], s.fourSum([2,1,0,-1], 2))

        self.assertEqual([
              [-2, -1, 1, 2],
              [-2,  0, 0, 2],
              [-1,  0, 0, 1] ],
            sorted(s.fourSum([1, 0, -1, 0, -2, 2], 0)))

        self.assertEqual([[-4,-3,3,4],[-4,-2,2,4],[-4,-1,1,4],
                          [-4,-1,2,3],[-4,0,1,3],[-3,-2,1,4],
                          [-3,-2,2,3],[-3,-1,0,4],[-3,-1,1,3],
                          [-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2]],
            sorted(s.fourSum([-4,-3,-2,-1,0,1,2,3,4], 0))
            )

        self.assertEqual([[-89,-22,8,103],[-22,2,3,17],[-2,-1,0,3],
                          [-2,-1,1,2],[-2,0,0,2],[-2,0,1,1],
                          [-1,-1,0,2],[-1,-1,1,1],[-1,0,0,1]],
            sorted(s.fourSum([1,0,-1,0,-2,3, 8, 10, 2, -1, -34, 1, 17,-22, 103, -135, 38,-89,2], 0)))

        self.assertEqual([
              (-2, -1, 1, 2), # leetcode will change this tuple to list
              (-2,  0, 0, 2),
              (-1,  0, 0, 1) ],
            sorted(s.fourSumRef([1, 0, -1, 0, -2, 2], 0)))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()