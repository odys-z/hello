'''
 * 2391. Minimum Amount of Time to Collect Garbage
 * https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/description/
'''
import unittest
from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        M, G, P = 'M', 'G', 'P'

        for x in range(1, len(travel)):
            travel[x] += travel[x-1]

        collects, tg, tp, tm = len(garbage[0]), 0, 0, 0
        for x, h in enumerate(garbage[1:]):
            if h.find(G) >= 0:
                tg = travel[x]
            if h.find(M) >= 0:
                tm = travel[x]
            if h.find(P) >= 0:
                tp = travel[x]
            collects += len(h)
        return collects + tg + tm + tp


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()

        self.assertEqual(21, s.garbageCollection(["G","P","GP","GG"], [2,4,3]))
        self.assertEqual(37, s.garbageCollection(["MMM","PGM","GP"], [3,10]))


if __name__ == '__main__':
    unittest.main()
