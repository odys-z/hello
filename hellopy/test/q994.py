'''
Created on 11 Nov 2019

@author: ody
'''
import unittest
from typing import List
import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        # queue - all starting cells with rotting oranges
        queue = collections.deque()
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    queue.append((r, c, 0))

        def neighbors(r, c):
            for nr, nc in ((r-1,c),(r,c-1),(r+1,c),(r,c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        d = 0
        while queue:
            r, c, d = queue.popleft()
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, d+1))

        if any(1 in row for row in grid):
            return -1
        return d

    
    def myOrange(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        # TODO use sparse matrix
        colhead = [0] * C
        rowhead = [0] * R
        mat = [[(0, 0)] * (C) for _ in range(R)]

        for cx in colhead:
            r0 = colhead[cx]
            rotten = grid[r0][cx]
            up = grid[r0 - 1][cx] if r0 - 1 >= 0 else -1
            down = grid[r0 + 1][cx] if r0 + 1 == R else -1

            if rotten == -1:
                colhead[cx] = colhead[cx] + 1
                continue
            elif rotten == 3: # if this is rotting, turn rotten
                if (down == 2 or up == 2):
                    linkColumn(mat, r0, cx)
            elif rotten == 2:
                linkColumn(mat, r0, cx)
            elif rotten == 1:
                grid[r0][cx] == 3 # rotting

            if rotten == 3:
                grid[r0][cx] == 2
        
        for rx in rowhead:
            c0 = rowhead[rx]

def linkColumn(mat, r, c):
    pass

def linkRow(mat, r, c):
    pass

class Test(unittest.TestCase):


    def test994(self):
        s = Solution()
        self.assertEqual(4, s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()