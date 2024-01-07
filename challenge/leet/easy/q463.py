import unittest
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])

        def dfs(y: int, x: int):
            if y < 0 or y >= r or x < 0 or x >= c:
                return 1
            elif grid[y][x] == 0:
                return 1
            elif grid[y][x] == -1:
                return 0

            grid[y][x] = -1
            ans = 0
            ans += dfs(y + 1, x)
            ans += dfs(y - 1, x)
            ans += dfs(y, x + 1)
            ans += dfs(y, x - 1)
            return ans

        for y in range(r):
            for x in range(c):
                if grid[y][x] == 1:
                    return dfs(y, x)
        return 0


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()
        self.assertEqual(16, s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
        self.assertEqual(4, s.islandPerimeter([[0],[1]]))
        self.assertEqual(4, s.islandPerimeter([[1]]))


if __name__ == '__main__':
    unittest.main()
