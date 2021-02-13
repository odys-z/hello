'''
658. Find K Closest Elements
https://leetcode.com/problems/find-k-closest-elements/

Given a sorted integer array arr, two integers k and x, return the k
closest integers to x in the array. The result should also be sorted
in ascending order.

An integer a is closer to x than an integer b if:
    |a - x| < |b - x|, or
    |a - x| == |b - x| and a < b
'''
from unittest import TestCase
from typing import List
from heapq import heapify, heappush, heappop

class SolutionUnsorted:
    '''
        If arr is unsorted.
        13.82%
    '''
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        x = -(x - 0.001)
        def enbuf(buf, v) -> List[int]:
            heappush(buf, (-abs(-v - x), v))
            if len(buf) > k:
                heappop(buf)
            return buf

        buf = []
        heapify(buf)

        for v in arr:
            enbuf(buf, v)
        
        buf = map(lambda e: e[1], buf)
        return sorted((buf))
        
class Solution:
    '''
    27.16%
    '''
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        buf = []
        l = len(arr)
        if l == 0: return buf
        elif x <= arr[0]:
            buf = arr[0 : min(l, k)]
        elif x >= arr[-1]:
            buf = arr[max(0, l - k) : l]
        else:
            # binary search
            low, hi, mid = 0, l-1, l // 2
            while low < mid < hi:
                if arr[mid] > x:
                    hi = mid
                elif arr[mid] < x:
                    low = mid
                else: break # arr[mid] == x
                mid = (low + hi) // 2
            
            # x != arr[mid]
            if x != arr[mid] and x - arr[mid] > arr[hi] - x:
                mid = hi
            elif x != arr[mid]:
                mid = low
            buf.append(arr[mid])
                
            # found, expand lower & upper
            low, hi = mid, mid 

            while len(buf) < k:
                if 0 < low and hi+1 < l and x - arr[low - 1] <= arr[hi+1] -x:
                    buf.insert(0, arr[low - 1])
                    low -= 1
                elif hi+1 < l:
                    buf.append(arr[hi+1])
                    hi += 1
                elif 0 < low:
                    buf.insert(0, arr[low - 1])
                    low -= 1
                else:
                    break

        return buf
            
if __name__ == '__main__':
    t = TestCase()
    s = SolutionUnsorted()
    
    t.assertCountEqual([1], s.findClosestElements([1, 3], 1, 2))
    t.assertCountEqual([-2,-1,1,2,3,4,5], s.findClosestElements([-2,-1,1,2,3,4,5], 7, 3))
    t.assertCountEqual([10], s.findClosestElements([1, 1, 1, 10, 10, 10], 1, 9))
    t.assertCountEqual([10, 10, 10], s.findClosestElements([1, 1, 1, 10, 10, 10], 3, 9))
    t.assertCountEqual([1, 10, 10, 10], s.findClosestElements([1, 1, 1, 10, 10, 10], 4, 9))
    t.assertCountEqual([1, 1, 10, 10, 10], s.findClosestElements([1, 1, 1, 10, 10, 10], 5, 9))
    t.assertCountEqual([1], s.findClosestElements([1], 1, 1))
    t.assertCountEqual([1, 2], s.findClosestElements([1, 2, 3], 2, 1))
    t.assertCountEqual([1, 2, 3, 4], s.findClosestElements([1,2,3,4,5], 4, 3))

    r = s.findClosestElements([1,2,3,4,5], 4, 100)
    t.assertCountEqual([2, 3, 4, 5], r)
    t.assertEqual(2, r[0])
    t.assertEqual(5, r[-1])

    t.assertCountEqual([], s.findClosestElements([], 1, 1))
    t.assertCountEqual([3], s.findClosestElements([1,2,3,4,5], 1, 3))
    t.assertCountEqual([2, 4], s.findClosestElements([1,2,4,5], 2, 3))

    r = s.findClosestElements([1,3], 2, 2)
    t.assertEqual(1, r[0])
    t.assertEqual(3, r[1])

    print('OK!')