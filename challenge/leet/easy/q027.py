'''
27. Remove Element
https://leetcode.com/problems/remove-element/

Created on 11 Feb 2021

@author: Odys Zhou
'''
from unittest import TestCase
from typing import List

class Solution:
    '''
    93.06%
    '''
    def removeElement(self, nums: List[int], val: int) -> int:
        i0 = -1
        for i in range(len(nums)):
            if val == nums[i]:
                continue
            i0 += 1
            nums[i0] = nums[i]

        return min(i0 + 1, len(nums))
            
if __name__ == '__main__':
    t = TestCase()
    s = Solution()

    l = [1, 1, 2]
    c = s.removeElement(l, 2)
    t.assertEqual(2, c)
    t.assertCountEqual([1, 1], l[0:c])
    
    l = [1, 1, 2, 3]
    c = s.removeElement(l, 1)
    t.assertEqual(2, c)
    t.assertCountEqual([2, 3], l[0:c])

    l = []
    c = s.removeElement(l, 1)
    t.assertEqual(0, c)
    t.assertCountEqual([], l[0:c])

    l = [1]
    c = s.removeElement(l, 1)
    t.assertEqual(0, c)
    t.assertCountEqual([], l[0:c])

    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    c = s.removeElement(l, 9)
    t.assertEqual(8, c)
    t.assertCountEqual([1, 2, 3, 4, 5, 6, 7, 8], l[0:c])

    l = [1, 1]
    c = s.removeElement(l, 1)
    t.assertEqual(0, c)
    t.assertCountEqual([], l[0:c])

    l = [1, 1, 1, 1, 1 ,1, 1, 1, 1, 1]
    c = s.removeElement(l, 1)
    t.assertEqual(0, c)
    t.assertCountEqual([], l[0:c])

    print('OK!')