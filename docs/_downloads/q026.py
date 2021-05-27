'''
26. Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Created on 11 Feb 2021

@author: Odys Zhou
'''
from unittest import TestCase
from typing import List

class Solution:
    '''
        98.02% 
    '''
    def removeDuplicates(self, nums: List[int]) -> int:
        i0 = 0
        for i in range(1, len(nums)):
            if nums[i0] == nums[i]:
                continue
            i0 += 1
            nums[i0] = nums[i]

        return min(i0 + 1, len(nums))
            
if __name__ == '__main__':
    t = TestCase()
    s = Solution()

    l = [1, 1, 2]
    c = s.removeDuplicates(l)
    t.assertEqual(2, c)
    t.assertCountEqual([1, 2], l[0:c])
    
    l = [1, 1, 2, 3]
    c = s.removeDuplicates(l)
    t.assertEqual(3, c)
    t.assertCountEqual([1, 2, 3], l[0:c])

    l = []
    c = s.removeDuplicates(l)
    t.assertEqual(0, c)
    t.assertCountEqual([], l[0:c])

    l = [1]
    c = s.removeDuplicates(l)
    t.assertEqual(1, c)
    t.assertCountEqual([1], l[0:c])

    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    c = s.removeDuplicates(l)
    t.assertEqual(9, c)
    t.assertCountEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], l[0:c])

    l = [1, 1]
    c = s.removeDuplicates(l)
    t.assertEqual(1, c)
    t.assertCountEqual([1], l[0:c])

    l = [1, 1, 1, 1, 1 ,1, 1, 1, 1, 1]
    c = s.removeDuplicates(l)
    t.assertEqual(1, c)
    t.assertCountEqual([1], l[0:c])

    print('OK!')