'''
976. Largest Perimeter Triangle
https://leetcode.com/problems/largest-perimeter-triangle/


Created on 27 Nov 2021
@author: Odys Zhou
'''

from typing import List
from unittest.case import TestCase

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        for x in range(len(nums) - 2):
            a, b, c = nums[x], nums[x+1], nums[x+2]
            if a < b + c:
                # sum is expensive (323ms)
                # return sum([a, b, c])
                # 210ms
                return a + b + c
        return 0
        

if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    
    t.assertEqual(5 , s.largestPerimeter([2, 1, 2]))
    t.assertEqual(0 , s.largestPerimeter([1, 2, 1]))
    t.assertEqual(10, s.largestPerimeter([3, 2, 3, 4]))
    t.assertEqual(8 , s.largestPerimeter([3, 6, 2, 3]))
    
    print('OK')