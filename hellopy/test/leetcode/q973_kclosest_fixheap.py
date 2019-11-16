'''
973. K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin/

Created on 16 Nov 2019

@author: ody
'''
import unittest
import heapq
from typing import List

class FixHeap(object):
    def __init__(self, size, reverse = False):
        self.size = size
        self.reverse = reverse
        self.h = []
        heapq.heapify(self.h)
        

    def tryPush(self, item):
        heapq.heappush(self.h, item)
        if len(self.h) > self.size:
            self.h = (heapq.nlargest(self.size, self.h)
                if self.reverse else heapq.nsmallest(self.size, self.h))

    def nFirst(self, n, key):
        if self.h:
            if self.reverse:
                return heapq.nlargest(n, self.h, key)
            else:
                return heapq.nsmallest(n, self.h, key)

class Solution(object):
    '''
        Input: points = [[1,3],[-2,2]], K = 1
        Output: [[-2,2]]
        
        Input: points = [[3,3],[5,-1],[-2,4]], K = 2
        Output: [[3,3],[-2,4]]
        (The answer [[-2,4],[3,3]] would also be accepted.)
    '''
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        closests = FixHeap(K)
        for p in points:
            d = p[0] ** 2 + p[1] ** 2
            closests.tryPush((d, p))
        return list(item for _, item in closests.h)
        
class Test(unittest.TestCase):

    def test973(self):
        s = Solution()
        self.assertEqual([[-2, 2]], s.kClosest([[1,3],[-2,2]], 1))
        self.assertEqual([[0, 0]], s.kClosest([[1,3],[-2,2], [0, 0]], 1))
        self.assertEqual([[3, 3], [-2, 4]], s.kClosest([[3,3],[5,-1],[-2,4]], 2))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()