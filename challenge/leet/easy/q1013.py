'''
1013. Partition Array Into Three Parts With Equal Sum

https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/

Created on 10 Dec 2021

@author: Odys Zhou
'''

from typing import List
from unittest import TestCase

'''
                 l-1
   1  2  3  4  5  6
 i .  |  .  .   
 j       .  .  |      
   1  3  6 10 15 21
'''

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        s = sum(arr)
        if int(s) != s:
            return False
        if s % 3 != 0:
            return False

        s /= 3

        acc, counter = 0, 0
        for i in range(len(arr)):
            acc += arr[i]
            if acc == s:
                counter += 1
                acc = 0
            
        return counter >= 3

t = TestCase()
s = Solution()

t.assertFalse(s.canThreePartsEqualSum([6,1,1,13,-1,0,-10,20]))
t.assertTrue(s.canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))
t.assertFalse(s.canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1]))
t.assertTrue(s.canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]))
t.assertTrue(s.canThreePartsEqualSum([1, 1, 1]))
t.assertTrue(s.canThreePartsEqualSum([1, -1, 1, -1, 1, -1]))
t.assertTrue(s.canThreePartsEqualSum([0, 0, 0]))
t.assertTrue(s.canThreePartsEqualSum([0, 0, 1, 1, -2]))
t.assertTrue(s.canThreePartsEqualSum([0, 0, 1, 1, -2, 0]))
t.assertTrue(s.canThreePartsEqualSum([0, -1, 1, 0]))
t.assertTrue(s.canThreePartsEqualSum([0, -1, 1, 2, -2]))

print('OK')