from unittest import TestCase
from typing import List

class Solution:
    '''
    93%
    '''
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        If overlapped, delete it. The only thing about math is delete the longer
        '''
        if not intervals: return 0

        intervals.sort()
        
        c = 0
        s, e = intervals[0]
        for s1, e1 in intervals[1:]:
            if s1 < e:
                c += 1
                e = min(e1, e) 
            else:
                e = e1
        return c

           
if __name__ == "__main__":
    t = TestCase()
    s = Solution()
    t.assertEqual(0, s.eraseOverlapIntervals([[1,2]]))
    t.assertEqual(1, s.eraseOverlapIntervals([[1,3], [2, 4]]))
    t.assertEqual(3, s.eraseOverlapIntervals([[10,16],[2,8],[1,6],[7,12],[5,6]]))
    t.assertEqual(0, s.eraseOverlapIntervals([]))
    t.assertEqual(2, s.eraseOverlapIntervals([[10,16],[2,8],[1,6],[7,12]]))
    t.assertEqual(0, s.eraseOverlapIntervals([[1,2],[3,4],[5,6],[7,8]]))
    t.assertEqual(0, s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[4,5]]))
    t.assertEqual(0, s.eraseOverlapIntervals([[1,2],[2,3]]))
    
    print('OK!')