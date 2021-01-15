'''
    Example 1:
        Input: [[1,3],[2,6],[8,10],[15,18]]
        Output: [[1,6],[8,10],[15,18]]
        Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

        Example 2:
        Input: [[1,4],[4,5]]
        Output: [[1,5]]
        Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''
from unittest import TestCase
from typing import List

class Solution2(object):
    '''
        Runtime: 84 ms, faster than 98.55% of Python3 online submissions for Merge Intervals.
        Memory Usage: 14.7 MB, less than 6.52% of Python3 online submissions for Merge Intervals.
    '''
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        if not intervals:
            return merged
        nodes = sorted(intervals)
        last = nodes.pop(0)
        merged.append(last)
        for l, r in nodes:
            if l > r: l, r = r, l
            if last[0] <= l <= last[1]:
                last[1] = max(r, last[1])
            else:
                last = [l, r]
                merged.append(last)
        print(merged)
        return merged
            
class Solution(object):
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        while len(intervals) > 0:
            l, r = intervals.pop(0)
            while len(intervals) > 0 and intervals[0][0] <= r:
                _, r1 = intervals.pop(0)
                r = max(r1, r)
            
            res.append([l, r])
        return res


if __name__ == "__main__":
    t = TestCase()
    s = Solution()
    t.assertEqual([[1,6],[8,10],[15,18]],
                  s.merge([[1,3],[2,6],[8,10],[15,18]]))

    t.assertEqual([[-3,6],[8,10],[15,18]],
                  s.merge([[-3, 5], [1,3],[2,6],[8,10],[15,18]]))
        
    t.assertEqual([], s.merge([]))
    
    t.assertEqual([[1, 5]], s.merge([[1, 4], [4, 5]]))
    
    print('OK!')