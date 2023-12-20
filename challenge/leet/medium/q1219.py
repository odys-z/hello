'''
1219. Path with Maximum Gold
https://leetcode.com/problems/path-with-maximum-gold/description
'''
import unittest
from typing import List


class Solution:
    mx = 0

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        self.mx = 0

        def backtrack(x, y, gold):
            if x < 0 or y < 0 or x >= C or y >= R or grid[y][x] <= 0:
                return

            temp = grid[y][x]
            # gold += temp
            grid[y][x] = -1

            self.mx = max(self.mx, gold + temp)

            backtrack(x - 1, y, gold + temp)
            backtrack(x + 1, y, gold + temp)
            backtrack(x, y - 1, gold + temp)
            backtrack(x, y + 1, gold + temp)
            grid[y][x] = temp

        for y in range(R):
            for x in range(C):
                backtrack(x, y, 0)
        return self.mx


class MyTestCase(unittest.TestCase):
    def test_1219(self):
        s = Solution()
        self.assertEqual(72, s.getMaximumGold([
            [0,0,0,0,0,0,0,0,0],
            [0,3,3,3,3,3,3,3,0],
            [0,3,0,0,0,0,0,3,0],
            [0,3,0,3,3,3,0,3,0],
            [0,0,0,3,0,3,0,3,0],
            [0,0,0,3,0,0,0,3,0],
            [0,0,0,3,3,3,3,3,0],
            [0,0,0,0,0,0,0,0,0]]))


if __name__ == '__main__':
    unittest.main()
