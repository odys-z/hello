'''
88. Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
one sorted array.

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has a size equal to m + n such that it has enough
space to hold additional elements from nums2.
 

Example 1:
    Input:  nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]

Example 2:
    Input:  nums1 = [1], m = 1, nums2 = [], n = 0
    Output: [1]
 

Constraints:
    nums1.length == m + n
    nums2.length == n
    0 <= m, n <= 200
    1 <= m + n <= 200
    -109 <= nums1[i], nums2[i] <= 109
'''
from unittest import TestCase
from typing import List

class Solution:
    '''
        76.30%
    '''
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m, n, x = m-1, n-1, m+n-1
        while 0 <= m and 0 <= n:
            if nums1[m] <= nums2[n]:
                nums1[x] = nums2[n]
                n -= 1
            else:
                nums1[x] = nums1[m]
                # nums1[m] = -float('inf')
                m -= 1
            x -= 1

        if 0 <= n:
            nums1[0 : n+1] = nums2[0 : n+1]
            


if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    
    l = [1, 2, None]
    s.merge(l, 2, [3], 1)
    t.assertCountEqual([1, 2, 3], l)
    
    l = [1, 3, None, None]
    s.merge(l, 2, [2, 3], 2)
    t.assertCountEqual([1, 2, 3, 3], l)

    l = [1, 3, 5, None, None]
    s.merge(l, 3, [2, 4], 2)
    t.assertCountEqual([1, 2, 3, 4, 5], l)

    l = [0, 0, 0]
    s.merge(l, 0, [2, 5, 6], 3)
    t.assertCountEqual([2, 5, 6], l)

    l = [1, 2, 2, None]
    s.merge(l, 3, [1], 1)
    t.assertCountEqual([1, 1, 2, 2], l)

    print('OK!')