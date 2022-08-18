'''
561. Array Partition I
https://leetcode.com/problems/array-partition-i/

'''
from typing import List
from unittest.case import TestCase

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort();
        s = 0
        for i in range(0, len(nums), 2):
            s += nums[i]
        
        return s

t = TestCase()
s = Solution()

t.assertEqual(4, s.arrayPairSum([1, 4, 3, 2]));
t.assertEqual(9, s.arrayPairSum([6,2,6,5,1,2]));

print('OK')