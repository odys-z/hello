'''
Created on 16 Jan 2021

@author: odys-z@github.com
'''
from unittest import TestCase
from typing import List

class SolutionTimeout:
    def maxProduct(self, nums: List[int]) -> int:
        def prodct(nums, s, e):
            p = 1
            for n in nums[s:e]:
                p *= n
            return p

        dp = [-float('inf')] * (len(nums) + 1)
        mxx = -float('inf')
        mxxrange = None

        for i in range(1, len(nums) + 1):
            for j in range(i):
                mxdp = max(prodct(nums, j, i), dp[i])
                if mxx < mxdp:
                    mxx = mxdp
                    mxxrange = (j, i)
        print(mxxrange)
        return mxx
        
class Solution:
    '''
    The trick here is that keeping accumulate the product, value 0 where do the work.
    Dont' forget the number n itself is max/min after been cleared by zero.
    '''
    def maxProduct(self, nums: List[int]) -> int:
        
        curr_max = curr_min = all_max = nums[0]
        for ele in nums[1:]:  
            curr_max = max(curr_max * ele, curr_min * ele, ele)
            curr_min = min(curr_max * ele, curr_min * ele, ele)
            all_max = max(all_max, curr_max)
            
        return all_max
    
if __name__ == '__main__':
    
    t = TestCase()
    s = Solution()
    t.assertEqual(6, s.maxProduct([2,3,-2,4]))
    
    print('OK!')