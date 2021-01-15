'''
'''
from unittest import TestCase
from typing import List

class Solution:
    '''
    Runtime: 52 ms, faster than 68.07% of Python3 online submissions for Rotting Oranges.
    Memory Usage: 14.3 MB, less than 35.28% of Python3 online submissions for Rotting Oranges.
    '''
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # find a rotten
        def findRottens(grid):
            rottens = []
            freshes = 0
            if len(grid) == 0: return rottens, freshes

            for rx in range(len(grid)):
                for cx in range(len(grid[0])):
                    if grid[rx][cx] == 2:
                        rottens.append((rx, cx))
                    elif grid[rx][cx] == 1:
                        freshes += 1
            return rottens, freshes
        
        def rottenAdj(grid, r, c):
            adjs = []
            for rx, cx in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                rx += r
                cx += c
                if 0 <= rx < len(grid) and 0 <= cx < len(grid[0]):
                    adj = grid[rx][cx]
                    if adj == 1:
                        grid[rx][cx] = 2
                        adjs.append((rx, cx))
            return adjs

        rottens, freshing = findRottens(grid)
        cnt = 0

        while len(rottens) > 0 and freshing > 0:
            rottings = []
            while len(rottens) > 0:
                r, c = rottens.pop(0)
                adj = rottenAdj(grid, r, c)
                rottings.extend(adj)
            if len(rottings) > 0:
                cnt += 1
                freshing -= len(rottings)
            rottens = rottings
        
        # check any more oranges
        for r in grid:
            for o in r:
                if o == 1:
                    return -1
        return cnt


if __name__ == "__main__":
    t = TestCase()
    s = Solution()

    t.assertEqual(4, s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
    t.assertEqual(6, s.orangesRotting(
        [[2,1,0,1,1,1,1],
         [0,1,1,0,0,1,1],
         [0,0,1,1,0,1,1],
         [2,1,0,0,1,1,2],
         [0,0,1,0,1,1,1],
         [0,1,2,1,0,0,1]]))
    t.assertEqual(22, s.orangesRotting(
        [[1,0,1,1,1,0,2],
         [1,0,1,0,1,0,1],
         [1,0,1,0,1,0,1],
         [1,0,1,0,1,0,1],
         [1,1,1,0,1,1,1]]))
    
    print('OK!')