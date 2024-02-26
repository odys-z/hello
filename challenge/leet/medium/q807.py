'''
 * 807. Max Increase to Keep City Skyline
 * https://leetcode.com/problems/max-increase-to-keep-city-skyline/description/
'''
import unittest
from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        xrow = [0] * m
        xcol = [0] * n

        for rx, r in enumerate(grid):
            for cx, c in enumerate(r):
                xrow[rx] = max(xrow[rx], c)
                xcol[cx] = max(xcol[cx], c)

        ans = 0
        for rx, r in enumerate(grid):
            for cx, c in enumerate(r):
                ans += min(xrow[rx], xcol[cx]) - c
        return ans


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()

        self.assertEqual(35, s.maxIncreaseKeepingSkyline([[3,0,8,4], [2,4,5,7], [9,2,6,3], [0,3,1,0]]))


if __name__ == '__main__':
    unittest.main()
