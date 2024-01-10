'''
 * 506. Relative Ranks
 * https://leetcode.com/problems/relative-ranks/description/
'''
import unittest
from heapq import heappush, heappop
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        def medal(ith: int):
            if ith > 2:
                return str(ith+1)
            elif ith == 2:
                return 'Bronze Medal'
            elif ith == 1:
                return 'Silver Medal'
            else:
                return 'Gold Medal'

        hq = []
        for x, v in enumerate(score):
            heappush(hq, (-v, x))

        ith = 0
        while len(hq) > 0:
            head = heappop(hq)
            score[head[1]] = medal(ith)
            ith += 1

        return score


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()
        self.assertEqual(["Gold Medal","Silver Medal","Bronze Medal","4","5"], s.findRelativeRanks([5,4,3,2,1]))
        self.assertEqual(["18","Silver Medal","17","16","15","14","13","12","11","10","9","8","7","6","5","4","Bronze Medal","Gold Medal"],
                         s.findRelativeRanks([0,16,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17]))


if __name__ == '__main__':
    unittest.main()
