'''
Created on 16 Nov 2019

@author: ody
'''
import unittest
from typing import List

class Solution(object):
    ''' Example 1:
        Input: [[1,3],[2,6],[8,10],[15,18]]
        Output: [[1,6],[8,10],[15,18]]
        Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

        Example 2:
        Input: [[1,4],[4,5]]
        Output: [[1,5]]
        Explanation: Intervals [1,4] and [4,5] are considered overlapping.
        
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
            

class Test(unittest.TestCase):


    def testName(self):
        s = Solution()
        self.assertEqual([[1,6],[8,10],[15,18]],
                         s.merge([[1,3],[2,6],[8,10],[15,18]]))

        self.assertEqual([[-3,6],[8,10],[15,18]],
                         s.merge([[-3, 5], [1,3],[2,6],[8,10],[15,18]]))
        
        self.assertEqual([], s.merge([]))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()