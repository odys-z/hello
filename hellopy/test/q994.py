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
        global colhead
        colhead = [0 for _ in range(C)]
        global rowhead
        rowhead = [0 for _ in range(R)]
        mat = [[[x + 1, y + 1] for y in range(C)] for x in range(R)]

        hour = -1
        rotted = -1
        while rotted != 0:
            hour = hour + 1
            rotted = 0
            rottings = []
            for cx in range(C):
                rx = colhead[cx]
                while (rx < R):
                    rotten = grid[rx][cx]
#                     up = grid[rx - 1][cx] if rx - 1 >= 0 else -1
                    down = grid[rx + 1][cx] if rx + 1 < R else -1

                    if rotten == -1:
                        colhead[cx] = colhead[cx] + 1
                        rx = rx + 1
                        continue
#                     elif rotten == 3: # if this is rottings, turn rotten
#                         if down == 2 or up == 2:
#                             rx = linkColumn(mat, rx, cx, up, down)
                    elif rotten == 2:
                        rx = linkColumn(mat, rx, cx, down)
                    elif rotten == 1:
                        if down == 2:
                            # grid[rx][cx] == 3 # rottings
                            rottings.append([rx, cx])
                            rotted = rotted + 1
                            rx = mat[rx + 1][cx][0] if rx + 1 < R else rx + 1
                        else:
                            rx = rx + 1
                    else: # rotten = 0
                        rx = mat[rx + 1][cx][0] if rx + 1 < R else rx + 1
            
            for rx in range(R):
                cx = rowhead[rx]
                while (cx < C):
                    rotten = grid[rx][cx]
#                     left = grid[rx][cx - 1] if cx - 1 >= 0 else -1
                    right = grid[rx][cx + 1] if cx + 1 < C else -1

                    if rotten == -1:
                        rowhead[cx] = rowhead[cx] + 1
                        cx = cx + 1
                        continue
#                     elif rotten == 3: # if this is rottings, turn rotten
#                         if down == 2 or up == 2:
#                             cx = linkRow(mat, rx, cx, left, down)
                    elif rotten == 2:
                        cx = linkRow(mat, rx, cx, right)
                    elif rotten == 1:
                        if right == 2:
                            # grid[rx][cx] == 3 # rottings
                            rottings.append([rx, cx])
                            rotted = rotted + 1
                            cx = mat[rx][cx + 1][1] if cx + 1 < C else cx + 1
                        else:
                            cx = cx + 1
                    else: # rotten = 0
                        cx = mat[rx][cx + 1][1] if cx + 1 < C else cx + 1
            
            for r, c in rottings:
                grid[r][c] = 2
            
            print(grid)
        return hour

colhead = []
rowhead = []

# How?
# How?
# How?
def linkColumn(mat, r, c, down):
    # first rotten jump here
    if colhead[c] < len(rowhead):
        mat[colhead[c]][c][0] = c

#     if up == 2 and c > 0:
#         cell = mat[r - 1][c]
#         # mat[r][c][0] = cell[0] if cell[0] >= 0 else r - 1
#         mat[r][c][0] = cell[0]
#         if mat[r][c][0] < 0:
#             colhead[c] = r

    # this is turning rotten, link down
    if down == 2:
        if r < len(mat) - 1:
            cell = mat[r + 1][c]
            # mat[r][c][0] = cell[0] if cell[0] < len(mat) else r + 1
            mat[r][c][0] = cell[0]
        else:
            mat[r][c][0] = len(rowhead)
        return mat[r][c][0]
    return r + 1

def linkRow(mat, r, c, right):
#     if left == 2 and r > 0:
#         cell = mat[r][c - 1]
#         # mat[r][c][1] = cell[1] if cell[1] >= 0 else c - 1
#         mat[r][c][1] = cell[1]
#         if mat[r][c][1] < 0:
#             rowhead[c] = r

    # first rotten jump here
    if rowhead[r] < len(colhead):
        mat[r][rowhead[r]][1] = r

    if right == 2:
        if c < len(mat[r]) - 1:
            cell = mat[r][c + 1]
            # mat[r][c][1] = cell[1] if cell[1] < len(mat[r]) else c + 1
            mat[r][c][1] = cell[1]
        else:
            mat[r][c][1] = len(colhead)
        return mat[r][c][1]
    return c + 1

class Test(unittest.TestCase):

    def test994(self):
        s = Solution()
        # self.assertEqual(4, s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
#         self.assertEqual(4, s.myOrange([[2,1,1],[1,1,0],[0,1,1]]))
#         print('')
#         self.assertEqual(2, s.myOrange([[1,1,1],[1,2,0],[0,1,1]]))
        print('')
        self.assertEqual(4, s.myOrange([[1,1,1,1,1],[1,1,1,1,1],[0,1,2,0,1],[0,1,1,1,0],[1,1,1,1,1]]))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()