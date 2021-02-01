'''
Given an integer array nums, find the contiguous subarray (containing at least
one number) which has the largest sum and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

@author: ody
'''
from unittest import TestCase
from typing import List

class Solution:
    '''
    11.29% but all solutions in O(n)
    '''
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dpsum = nums[0]
        maxsum = dpsum
        for n in nums[1:]:
            dpsum = max(dpsum + n, n) # Kadane's
            maxsum = max(dpsum, maxsum)
        return maxsum
              
        
if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    t.assertEqual(6, s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    t.assertEqual(1, s.maxSubArray([1]))
    t.assertEqual(0, s.maxSubArray([0]))
    t.assertEqual(-1, s.maxSubArray([-1]))
    t.assertEqual(-100, s.maxSubArray([-100]))
    
    print('OK!')