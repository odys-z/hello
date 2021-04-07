'''
https://leetcode.com/problems/number-of-islands/

200. Number of Islands
Medium

Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or
vertically. You may assume all four edges of the grid are all surrounded by water.
 
Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

@author: Odys Zhou
'''
import unittest
import collections
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def merge(r, c, tempId):
            cells = collections.deque()
            cells.append((r, c))

            while len(cells) > 0:
                r0, c0 = cells.popleft()
                terrian = grid[r0][c0]
                # grid[r][c]= tempId
                if terrian == '1':
                    grid[r0][c0] = tempId
                    for (r1, c1) in [(r0+1, c0), (r0-1, c0), (r0, c0+1), (r0, c0-1)]:
                        if (r1 in range(m) and c1 in range(n)
                            and grid[r1][c1] == '1' and (r1, c1) not in cells):
                            cells.append((r1, c1))
                        # else already merged this
                    
                elif type(terrian) == int and terrian >= 0:
                    # needs merging into an old one
                    return terrian, cells

            return tempId + 1, cells

        
        def setCells(cells, isd):
            for r, c in cells:
                grid[r][c] = isd

        if len(grid) <= 0: return 0

        m, n = len(grid), len(grid[0])
        cIs = 0

        # find first

        # brutal path to merge into a known island
        for rx in range(m):
            for ilx in range(n):
                cell = grid[rx][ilx]
                if cell == '0': continue # water

                if cell == '1':
                    # new cell found, try merge or add a new island
                    theId, cells = merge(rx, ilx, cIs)
                    if theId > cIs:
                        # new
                        cIs += 1
                        setCells(cells, cIs)
                    elif theId < cIs:
                        setCells(cells, theId)

        return cIs
        

if __name__ == "__main__":
    
    t = unittest.TestCase()
    s = Solution()
    t.assertEqual(1, s.numIslands([
        ["1","0","0","0","0"],
        ["0","0","0","0","0"],
        ["0","0","0","0","0"],
        ["0","0","0","0","0"]
    ]))
    t.assertEqual(1, s.numIslands([
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]))
    t.assertEqual(3, s.numIslands([
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]))
    t.assertEqual(10, s.numIslands([
        ["1","0","1","0","1"],
        ["0","1","0","1","0"],
        ["1","0","1","0","1"],
        ["0","1","0","1","0"]
    ]))
    t.assertEqual(1, s.numIslands([
        ["1","1","1","1","1","1"],
        ["0","0","0","0","0","1"],
        ["0","1","1","1","0","1"],
        ["0","1","0","1","0","1"],
        ["0","1","0","0","0","1"],
        ["0","1","1","1","1","1"]
    ]))
    t.assertEqual(3, s.numIslands([
        ["1","1","1","1","1","1","1","1","1"],
        ["1","0","0","0","0","0","0","0","1"],
        ["1","0","1","1","1","1","1","0","1"],
        ["1","0","1","0","0","0","1","0","1"],
        ["1","0","1","0","1","0","1","0","1"],
        ["1","0","1","0","0","0","1","0","1"],
        ["1","0","1","1","1","1","1","0","1"],
        ["1","0","0","0","0","0","0","0","1"],
        ["1","1","1","1","1","1","1","1","1"]
    ]))
    t.assertEqual(1, s.numIslands([
        ["0","0","0","0","0","0","0","0","1"],
        ["0","0","0","0","0","0","0","1","1"],
        ["0","0","0","0","0","0","1","1","0"],
        ["0","0","0","0","0","1","1","0","0"],
        ["0","0","0","0","1","1","0","0","0"],
        ["0","0","0","1","1","0","0","0","0"],
        ["0","0","1","1","0","0","0","0","0"],
        ["0","1","1","0","0","0","0","0","0"],
        ["1","1","0","0","0","0","0","0","0"]
    ]))

    print('OK!')
