from unittest import TestCase
from typing import List
from _heapq import heapify, heappush 

class Solution2:
    '''
    65%
    '''
        
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        
        points.sort()
        
        # minimum r at top
        minr = [points[0][1]]
        arrows = 1
        heapify(minr)
        
        for l, r in points[1:]:
            if minr and l <= minr[0] :
                heappush(minr, r)
            else:
                minr.clear()
                arrows += 1
                heappush(minr, r)
        return arrows

class Solution:
    '''
     95.28%
    '''
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        points.sort(key = lambda intv: intv[1])
        arrows = 1
        minr = points[0][1]
        for l, r in points[1:]:
            if minr < l:
                arrows += 1
                minr = r # first r is sorted as the least
        return arrows
    
if __name__ == "__main__":
    t = TestCase()
    s = Solution2()
    t.assertEqual(2, s.findMinArrowShots([[10,16],[2,8],[1,6],[7,12],[5,6]]))
    t.assertEqual(0, s.findMinArrowShots([]))
    t.assertEqual(2, s.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
    t.assertEqual(4, s.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
    t.assertEqual(2, s.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))
    t.assertEqual(1, s.findMinArrowShots([[1,2]]))
    t.assertEqual(1, s.findMinArrowShots([[1,2],[2,3]]))
    
    print('OK!')