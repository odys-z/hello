'''
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
Runtime: 680 ms, faster than 56.50% of Python3 online submissions for K Closest Points to Origin.
Memory Usage: 19.9 MB, less than 56.15% of Python3 online submissions for K Closest Points to Origin.

@author: Odys Zhou
'''

from unittest import TestCase
from typing import List
from _heapq import heapify, heappush 
from heapq import nsmallest

class Solution():
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        q = []
        heapify(q)
        for p in points:
            d = p[0] * p[0] + p[1] * p[1]
            heappush(q, (d, p))
            
        q = list(item for _, item in nsmallest(K, q))
        return q

if __name__ == '__main__':
    
    t = TestCase()
    s = Solution()
    t.assertCountEqual([[-2, 2]], s.kClosest([[-2, 2], [1, 3]], 1))
    t.assertCountEqual([[3,3],[-2,4]], s.kClosest([[3,3],[5,-1],[-2,4]], 2))

    print('OK!')