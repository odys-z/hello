'''
    152. Maximum Product Subarray
    https://leetcode.com/problems/maximum-product-subarray/

    Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

    Example 1:

    Input: [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.
    Example 2:

    Input: [-2,0,-1]
    Output: 0
    Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

    @author: odys zhou
'''

from unittest import TestCase
from typing import List

class SolutionErr:
    def maxProduct(self, nums: List[int]) -> int:
        maxpos = maxnn = nums[0]
        for n in nums[1:]:
            if n == 0:
                maxpos = max(maxpos, maxnn, 0)
                maxnn = 0
            else:
                maxnn = maxnn * n if maxnn != 0 else n
                maxpos = max(maxpos, maxnn, n)
        return max(maxpos, maxnn)

class Solution1:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1
        
        for n in nums:
            
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n) 
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        return res

class Solution:
    '''
    66.34% ~ 84.95% 
    
    x x  0  y        y                      y ...
            Ui-1    Ui = max(ui * ni, li * ni, ni)
            Li-1    Li = min(ui * ni, li * ni, ni)
    ^  
    res_k-1
            ^
            res_k

    U(i) = [ U(i-1) ] * n[i]
    L(i) = [ L(i-1) ] * n[i]
    '''
    def maxProduct(self, nums: List[int]) -> int:
        Ui = Li = res = nums[0]
        
        for n in nums[1:]:
            nu, nl = n * Ui, n * Li
            Ui, Li = max(nu, nl, n), min(nu, nl, n)
            res = max(res, Ui)
        return res
        
if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    t.assertEqual(0, s.maxProduct([0]))
    t.assertEqual(6, s.maxProduct([2, 3, -2, 4]))
    t.assertEqual(48, s.maxProduct([2, 3, -2, 4, -1]))
    t.assertEqual(-1, s.maxProduct([-1]))
    t.assertEqual(0, s.maxProduct([-1, 0]))
    t.assertEqual(1, s.maxProduct([-1, 1]))
    t.assertEqual(1, s.maxProduct([-1, 0, 1]))
    t.assertEqual(0, s.maxProduct([-2, 0, -1]))
    t.assertEqual(8, s.maxProduct([-2, 4, -1, 0, 3]))
    t.assertEqual(105, s.maxProduct([0, -1, -15, 7]))
    t.assertEqual(24, s.maxProduct([2, -5, -2, -4, 3]))


    print('ok!')