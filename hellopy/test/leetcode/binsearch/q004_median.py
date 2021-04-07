'''
4. Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5

Created on 7 Dec 2019

@author: odys-z@github.com
'''
import unittest
from typing import List

'''
Runtime: 92 ms, faster than 94.65% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Median of Two Sorted Arrays.
'''
class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        m, n = len(A), len(B)
        if m > n:
            m, n, A, B = n, m, B, A
        
        mini, maxi, len0_5 = 0, m, (m + n + 1) // 2
        ''' m <= n
        m,n = 1, 3; 2, 3; 3, 3;
        i,j = 0, 2; 1, 2; 1, 2;
        '''
        
        while mini <= maxi:
            i = (mini + maxi) // 2
            j = len0_5 - i
            if i < m and A[i] < B[j - 1]:
                mini = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                maxi = i - 1
            else:
                # a[i] > b[j-1], b[j-1] < a[i]
                maxleft = max(A[i - 1] if i > 0 else -float('inf'),
                              B[j - 1] if j > 0 else -float('inf'))
                if (m + n) % 2 == 1:
                    return maxleft
                
                minrit = min(A[i] if i < m else float('inf'),
                             B[j] if j < n else float('inf'))
                
                return (maxleft + minrit) / 2
        
'''
Runtime: 92 ms, faster than 94.65% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Median of Two Sorted Arrays.
'''
class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        tmp = sorted(nums1 + nums2)
        N = len(tmp)
        if N % 2 == 0:
            _med = len(tmp) // 2
            last_med = tmp[_med-1]
            next_med = tmp[_med]
            return (next_med + last_med) / 2
        else:
            # return tmp[round(N / 2) - 1]
            return tmp[N // 2]
        
class Test(unittest.TestCase):


    def testName(self):
        s = Solution2();
        self.assertEqual(2, s.findMedianSortedArrays([1, 3], [2]))
        self.assertEqual(0, s.findMedianSortedArrays([0], [0]))
        self.assertEqual(0, s.findMedianSortedArrays([-1, 100], [0]))
        self.assertEqual(2.5, s.findMedianSortedArrays([1, 2], [3, 4]))
        self.assertEqual(2, s.findMedianSortedArrays([], [1,2,3]))
        self.assertEqual(3, s.findMedianSortedArrays([], [1,2,3,4,5]))
        self.assertEqual(1, s.findMedianSortedArrays([1, 1, 1, 1, 1], [2]))
        self.assertEqual(5.5, s.findMedianSortedArrays([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()