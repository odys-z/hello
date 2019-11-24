'''
16. 3Sum Closest
https://leetcode.com/problems/3sum-closest/

Given an array nums of n integers and an integer target, find three integers
in nums such that the sum is closest to target. Return the sum of the three
integers. You may assume that each input would have exactly one solution.

Example:
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Created on 23 Nov 2019

@author: odys-z@github.com
'''
import unittest
from typing import List
from heapq import heapify, heappush, heappop


'''
Runtime: 156 ms, faster than 36.98% of Python3 online submissions for 3Sum Closest.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for 3Sum Closest.
'''
class SolutionBrutal(object):
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        lst = sorted(nums) 
        
        closest = float("Inf")
        lastix = len(lst) - 1
         
        for ix0 in range(0, len(lst)):
            target2, lastix = findClosest(target, lst, ix0, lastix)
            if target == target2:
                return target
            elif abs(target - target2) < abs(target - closest):
                # getting closer
                closest = target2
                ix0 += 1
        
        return closest
        
def findClosest(target, nums: List[int], ix0, lastix) -> (int, int):
    closest = float("inf")
    # ix1 increase, searching upward
    # ix2 decrease, searching downward
    ix1 = ix0 + 1
    # ix2 = len(nums) - 1
    ix2 = lastix 
    while ix1 < ix2:
        # avoid ix0
        if ix1 == ix0:
            ix1 += 1
            continue
        elif ix2 == ix0:
            ix2 -= 1
            continue

        d = target - nums[ix1] - nums[ix2] - nums[ix0]

        if d == 0:
            return target, ix2
        if (d > 0 and d < abs(target - closest)
            or d < 0 and -d < abs(target - closest)):
            # getting closer
            closest = target - d # n1 + n2 + n0
            
        # n1 + n2 > target - n0: try lower
        # n1 + n2 < target - n0: try bigger
        if nums[ix1] + nums[ix2] > target - nums[ix0]:
            ix2 -= 1
            while ix2 > ix0 and nums[ix2] == nums[ix2 + 1]:
                ix2 -= 1
        else:
            ix1 += 1
            while ix1 < ix2 and nums[ix1] == nums[ix1 - 1]:
                ix1 += 1

    return closest, min(ix2 + 1, lastix)
                    
''' 40ms '''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float('inf')
        for i in range(len(nums)-2):
            print(i, ans)
            if i>0 and nums[i-1] == nums[i]:
                continue
            minsum = nums[i] + nums[i+1] + nums[i+2]
            maxsum = nums[i] + nums[-1] + nums[-2]
            if minsum >= target:
                if abs(minsum-target) >= abs(ans-target):
                    return ans
            if maxsum < target:
                if abs(maxsum-target) < abs(ans-target):
                    ans = maxsum
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                thsum = nums[i] + nums[left] + nums[right]
                # print(thsum)
                if abs(thsum - target) < abs(ans - target):
                    ans = thsum
                if thsum == target:
                    return thsum
                elif thsum < target:
                    left += 1
                    while left < len(nums)-1 and nums[left-1] == nums[left]:
                        left += 1
                else:
                    right -= 1
                    while right > i and nums[right+1] == nums[right]:
                        right -= 1
        return ans


def NumPipe(h : List):
    for ix, e in enumerate(h):
        yield(ix, e)
        
class SolutionPipe(object):
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        dists = []

        for ix1 in range(len(nums)):
            for ix2 in range(ix1):
                dists.append((nums[ix1] + nums[ix2], ix1, ix2))
        dists.sort(key = lambda e: e[0])
        
        p1_2 = NumPipe(reversed(dists))
        p0 = NumPipe(nums)
        try: 
            n1_2 =  next(p1_2)
            n0 = next(p0)
            closest = n0[1] + n1_2[1][0] # e.n1 + n2
            while True:
                ix0, ix1, ix2 = n0[0], n1_2[1][1], n1_2[1][2]
                if ix0 == ix1 or ix0 == ix2:
                    n1_2 = next(p1_2)
                    continue
                sum3 = nums[ix0] + n1_2[1][0]
                if sum3 == target:
                    return sum3
                elif sum3 < target and abs(target - sum3) < abs(closest):
                        closest = sum3
                elif sum3 > target and abs(target - sum3) < abs(closest):
                        closest = sum3

                # now sum3 != target
                if sum3 > target:
                    n1_2 = next(p1_2)
                else:
                    n0 = next(p0)
                    
        except StopIteration:
            pass
        
        return closest

                    

'''
Runtime: 76 ms, faster than 97.07% of Python3 online submissions for 3Sum Closest.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for 3Sum Closest.
'''
class SolMimic40ms(object):
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        lst = nums
        
        closest = float("Inf")
        lastix = len(lst) - 1
         
        for ix0 in range(0, len(lst) - 2):

            minsum = nums[ix0] + nums[ix0 + 1] + nums[ix0 + 2]
            maxsum = nums[ix0] + nums[lastix] + nums[lastix-1]
            if minsum >= target:
                if abs(minsum-target) >= abs(closest - target):
                    # return closet
                    break
            if maxsum < target:
                if abs(maxsum - target) < abs(closest - target):
                    closest = maxsum
                    continue

            target2, lastix = findClosest(target, lst, ix0, lastix)
            if target == target2:
                return target
            elif abs(target - target2) < abs(target - closest):
                # getting closer
                closest = target2
                ix0 += 1
        
        return closest
                
arr = [-1,2,1,-4, 5,7, 0, 11, 12, 51,22,33,-5,-7,-8,-21, 27, 27, 43, 28, 11, 20, 1, 4, 49, 18, 37, 31, 31, 7, 3, 31, 50, 6, 50, 46, 4, 13, 31, 49, 15, 52, 25, 31, 35, 4, 11, 50, 40, 1, 49, 14, 46, 16, 11, 16, 39, 26, 13, 4, 37, 39, 46, 27, 49, 39, 49, 50, 37, 9, 30, 45, 51, 47, 18, 49, 24, 24, 46, 47, 18, 46, 52, 47, 50, 4, 39, 22, 50, 40, 3, 52, 24, 50, 38, 30, 14, 12, 1, 5, 52, 44, 3, 49, 45, 37, 40, 35, 50, 50, 23, 32, 1, 2, 28,342,418,485,719,670,878,752,662,994,654,504,929,660,424,855,922,744,600,229,728,33,371,863,561,772,271,178,455,449,426,835,143,845,321,214,867,199,967,881,193,973,386,122,633,810,330,907,906,282,136,986,315,860,849,229,632,473,759,87,922,185,922,418,382,243,632,250,795,599,131,988,924,869,463,558,680,145,465,938,427,954,925,94,814,126,323,798,599,434,885,874,620,159,292,354,755,924,956,550,876,88,890,800,309,705,358,989,850,176,280,629,130,205,724,296,331,399,94,283,186,331,157,806,490,801,512,597,725,469,499,601,909,390,754,218,447,112,560,298,640,840,279,122,397,355,418,80,755,864,363,293,195,872,451,38,673,963,635,751,432,487,352,341,229,458,912,676,923,472,326,563,312,606,686,709,313,456,789,420,321,505,713,868,377,164,258,403,128,246,154,912,733,858,606,962,317,518,990,240,990,317,803,302,275,841,363,588,650,504,9,323,9,74,191,387,239,450,790,367,48,944,279,781,802,885,743,471,755,85,711,745,402,867,399,29,708,762,970,710,267,331,33,276,405,577,15,644,379,157,363,427,453,995, 46,53,93,82,78,20,49,76,43,67,52, 41,65,38,97,98,56,32,85,11,49,90, 68,95,38,53,96,94,57,36,93,55,89, 87,89,67,59,90,96,2,58,0,95,75,38, 44,73,94,76,10,57,25,1,25,21,91,30, 69,85,39,57,31,95,46,70,84,66,29,75, 14,83,85,14,79,60,52,23,85,98,0,96,55, 77,49,32,50,92,62,20,78,53,29,9,48,76, 79,85,94,60,60,60,43,97,74,74,9,78,98, 94,76,50,42,83,79,43,67,30,36,81,2,66, 34,31,27,35,59,58,20,53,18,32,13,13,29, 39,88,90,17,38,84,45,40,79,80,19,22,99, 49,10,80,51,76,67,83,3,2,42,61,74,48,31, 6,13,45,87,53,85,77,22,75,13,20,67,92,0, 86,67,0,88,77,32,91,6,99,26,61,53,69,75, 27,69,6,33,82,3,72,87,40,49,10,15,63,30, 82,7,82,21,74,34,9,4,67,0,10,18,27,23,72, 48,98,51,69,57,37,3,60,9,91,1,59,53,68,22, 35,3,29,69,76,56,4,37,12,23,89,74,41,68,97, 65,68,96,17,37,53,54,41,65,63,84,18,22,89, 87,96,76,42,78,45,70,34,1,7,46,24,96,20,66, 65,69,31,33,65,0,23,70,54,64,36,18,0,54,92, 41,93,89,17,87,19,14,57,53,16,64,51,40,61, 23,58,78,92,90,63,10,90,86,80,97,2,68,15,2, 75,59,95,68,0,64,56,19,79,65,24,47,30,27,87, 43,50,46,73,95,88,36,5,30,23,37,27,25,58,94, 80,33,6,75,1,6,40,9,26,19,27,50,66,9,30,5,52, 80,3,77,27,43,13,84,74,36,22,53,14,80,48,94, 65,6,69,18,12,61,80,90,32,7,93,50,16,23,56,20, 3,11,97,31,55,10,15,29,99,89,34,13,21,34,59,86, 40,28,5,53,42,37,43,74,44,36,25,60,59,33,80,15, 44,77,98,51,39,65,32,38,55,67,3,28,1,62,67, 42,43,24,47,85,61,90,59,5,79,36,65,90,21,97,5,66, 74,55,17,13,21,50,4,28,69,7,56,70,70,23,64,65,99, 11,50,60,2,61,65,33,50,82,23,71,79,81,89,5,36,59, 71,57,61,75,37,30,34,94,0,56,69,65,21,69,76,71, 29,30,85,47,15,35,29,39,6,61,72,48,66,8,7,89,18, 68,64,55,98,99,1,50,7,23,15, 29,92,44,52,73,26,89,72,42,24,2,33,83,15,5,31,33, 65,38,23,83,58,87,91,56,38,44,58,98,67,74,27,11,70, 31,85,48,21,57,90,97,11,75,80,78,80,63,12,46,53,35, 81,11,74,72,19,65,69,78,63,36,4,42,48,26,73,85,74,46, 94,17,44,58,92,24, 36,73,40,48,71,93,35,52,57,62,77,28,27,46,6,42,34,62, 36,34,88,61,71,63,8,66,32,52,24,24,28,60,49,20,61,20,66, 48,73,23,10,2,51,89,0,10,31,34,72,19,69,61,81,40,76,89, 58,8,93,82,84,73,95,34,94,8,6,12,56,31,35,19,33,38,8,33,48, 40,68,73,11,89,86,92,81,62,33,92,22,78,26,6,52,21,92,98, 81,99,10,90,30,97,9,16,87,17,49,36,9,69,61,21,10,47,65, 44,61,99,36,83,77,62,41,81,36,86,79,17,37,41,59,67,90, 68,83,78,38,85,66,47,6,27,20,17,26,86,61,87,85,97,22,14, 59,15,96,47,1,27,65,38,69,24,58,59,45,93,37,83,30,55,30, 37,82,3,54,8,89,67,47,74,16,69,40,27,85,36,75,38,64,92, 29,85,68,87,96,13,32,86,96,63,41,79,52,24,82,58,84,71, 25,32,97,41,1,89,68,38,26,95,77,90,87,6,27,56,45,23,69,77, 9,18,92,51,97,96,27,31,54,11,54,79,95,3,72,49,92,93,87, 70,88,16,12,28,74,39,84,19,63,5,49,72,75,93,75,24,90,2, 55,44,66,61,76,13,64,48,62,9,93,2,79,82,70,92,10,45,83, 46,64,46,3,65,71,79,59,98,3,49,53,59,45,19,72,21,84,89,22, 99,98,15,1,29,49,23,73,11,68,57,57,85,55,61,50,78,92,9, 77,95,10,30,6,56,1,79,77,85,68,99,84,18,67,37,47,16,61, 21,28,81,30,85,66,85,98,17,64,42,26,93,38,89,23,96,45, 24,75,74,61,95,74,46,13,93,35,13,9,96,86,37,78,16,75,96,53, 25,13,69,68]    

class Test(unittest.TestCase):
    def test40ms(self):
        s = Solution()
        self.assertEqual(2, s.threeSumClosest([-1, 2, 1, -4], 1))

    def test016(self):
        s = SolutionBrutal()
        self.assertEqual(3, s.threeSumClosest([0, 1, 2], 0))
        self.assertEqual(3, s.threeSumClosest([0, 1, 2], -5))
        self.assertEqual(2, s.threeSumClosest([-1, 2, 1, -4], 1))
        self.assertEqual(0, s.threeSumClosest([-1, 2, 1, -4, 5], 1))
        self.assertEqual(1, s.threeSumClosest([-1, 2, 7, 0], 1))
        self.assertEqual(1, s.threeSumClosest([-1, 2, 1, -4, 5, 7, 0], 1))
        self.assertEqual(82, s.threeSumClosest([1,2,4,8,16,32,64,128], 82))
        self.assertEqual(1, s.threeSumClosest([-1,2,1,-4, 5,7, 0, 11, 12, 51,22,33,-5,-7,-8,-21], 1))
    
        self.assertEqual(905, s.threeSumClosest(arr, 905))
        
    def testMimic(self):
        s = SolMimic40ms()
        self.assertEqual(3, s.threeSumClosest([0, 1, 2], 0))
        self.assertEqual(3, s.threeSumClosest([0, 1, 2], -5))
        self.assertEqual(2, s.threeSumClosest([-1, 2, 1, -4], 1))
        self.assertEqual(0, s.threeSumClosest([-1, 2, 1, -4, 5], 1))
        self.assertEqual(1, s.threeSumClosest([-1, 2, 7, 0], 1))
        self.assertEqual(1, s.threeSumClosest([-1, 2, 1, -4, 5, 7, 0], 1))
        self.assertEqual(82, s.threeSumClosest([1,2,4,8,16,32,64,128], 82))
        self.assertEqual(1, s.threeSumClosest([-1,2,1,-4, 5,7, 0, 11, 12, 51,22,33,-5,-7,-8,-21], 1))
    
        self.assertEqual(905, s.threeSumClosest(arr, 905))
    
    def testNeway(self):
        s = SolutionPipe()
        self.assertEqual(3, s.threeSumClosest([0, 1, 2], 0))
        self.assertEqual(3, s.threeSumClosest([0, 1, 2], -5))
        self.assertEqual(2, s.threeSumClosest([-1, 2, 1, -4], 1))
        self.assertEqual(0, s.threeSumClosest([-1, 2, 1, -4, 5], 1))
        self.assertEqual(1, s.threeSumClosest([-1, 2, 7, 0], 1))
        self.assertEqual(1, s.threeSumClosest([-1, 2, 1, -4, 5, 7, 0], 1))
        self.assertEqual(82, s.threeSumClosest([1,2,4,8,16,32,64,128], 82))
        self.assertEqual(1, s.threeSumClosest([-1,2,1,-4, 5,7, 0, 11, 12, 51,22,33,-5,-7,-8,-21], 1))
    
        self.assertEqual(905, s.threeSumClosest(arr, 905))
        
if __name__ == "__main__":
    unittest.main()
    