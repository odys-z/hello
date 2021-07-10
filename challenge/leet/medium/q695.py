'''
695. Max Area of Island
 
 https://leetcode.com/problems/max-area-of-island/

Input: grid = [
[_,_,1,_,_,_,_,1,_,_,_,_,_],
[_,_,_,_,_,_,_,1,1,1,_,_,_],
[_,1,1,_,1,_,_,_,_,_,_,_,_],
[_,1,_,_,1,1,_,_,1,_,1,_,_],
[_,1,_,_,1,1,_,_,1,1,1,_,_],
[_,_,_,_,_,_,_,_,_,_,1,_,_],
[_,_,_,_,_,_,_,1,1,1,_,_,_],
[_,_,_,_,_,_,_,1,1,_,_,_,_]  ]

Output: 6

Explanation:
The answer is not 11, because the island must be connected 4-directionally.

Created on 1_ Jul 2_21

@author: Odys Zhou
'''
from typing import List
from unittest import TestCase

class Solution:
    '''
    21.01% -> 40.01%
    '''
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        maxlands = 0
        
        def parentOf(islands, ix):
            if ix not in islands:
                return (ix, 1)
            p, l = islands.get(ix)
            while p != ix: # {ix 15: p 7}, {7: 7}
                ix = p
                p, l = islands.get(ix)
            return p, l

        def dsu(islands, u, v, maxlands):
            '''
                u      u v      v
                v               u
            '''
            pu, cu = parentOf(islands, u)
            pv, cv = parentOf(islands, v)
            
            if pu < pv:
                pu, pv = pv, pu
            lands = cu + cv
            islands.update({v: (pu, lands)})
            islands.update({pu: (pu, lands)})
            islands.update({pv: (pu, lands)})
            
           
            return max(maxlands, cu + cv)
        
        islands = dict() # {ix: parent}

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    continue

                me = r * col + c

                # new found land
                if me not in islands:
                    maxlands = max(maxlands, 1)
                    islands.update({me: (me, 1)})

                adjs = [(r+1, c), (r, c+1)]
                for x, y in adjs:
                    if 0 <= x < row and 0 <= y < col and grid[x][y] != 0:
                        ix = x * col + y
                        if parentOf(islands, ix)[0] == parentOf(islands, me)[0]:
                            continue
                        maxlands = dsu(islands, me, ix, maxlands)
        return maxlands

if __name__ == '__main__':
    s = Solution()
    
    t = TestCase()

    grid = [[1,0,1],
            [1,1,1]] 
    t.assertEqual(5, s.maxAreaOfIsland(grid))

    grid = [[1,0],
            [1,1]] 
    t.assertEqual(3, s.maxAreaOfIsland(grid))

    grid = [[1,0,0],
            [1,1,1]] 
    t.assertEqual(4, s.maxAreaOfIsland(grid))

    grid = [[0,0,1],
            [1,1,1]] 
    t.assertEqual(4, s.maxAreaOfIsland(grid))

    grid = [[1,0,0],
            [1,1,0]] 
    t.assertEqual(3, s.maxAreaOfIsland(grid))
   
    _ = 0
    grid = [
        #0 1 2 3 4 5 6 7 8 9 10  12
        [_,_,1,_,_,_,_,1,_,_,_,_,_],
        [_,_,_,_,_,_,_,1,1,1,_,_,_],
        [_,1,1,_,1,_,_,_,_,_,_,_,_],
        [_,1,_,_,1,1,_,_,1,_,1,_,_],
        [_,1,_,_,1,1,_,_,1,1,1,_,_], # 4
        [_,_,_,_,_,_,_,_,_,_,1,_,_],
        [_,_,_,_,_,_,_,1,1,1,_,_,_],
        [_,_,_,_,_,_,_,1,1,_,_,_,_]  ]

    t.assertEqual(6, s.maxAreaOfIsland(grid))
    
    grid = [[1]]
    t.assertEqual(1, s.maxAreaOfIsland(grid))

    grid = [[0]]
    t.assertEqual(0, s.maxAreaOfIsland(grid))

    grid = [[1 for _ in range(4)] for i in range(3)]
    t.assertEqual(12, s.maxAreaOfIsland(grid))

    grid = [[0 for _ in range(4)] for i in range(3)]
    t.assertEqual(0, s.maxAreaOfIsland(grid))

    grid = [
        #0 1 2 3 4 5 6 7 8 9 10  12
        [1,_,1,_,1,_,1,_,1,_,1,_,1],
        [_,1,_,1,_,1,_,1,_,1,_,1,_],
        [1,_,1,_,1,_,1,_,1,_,1,_,1],
        [_,1,_,1,_,1,_,1,_,1,_,1,_],
        [1,_,1,_,1,_,1,_,1,_,1,_,1],
        [_,1,_,1,_,1,_,1,_,1,_,1,_],
        [1,_,1,_,1,_,1,_,1,_,1,_,1], # 4
        [_,1,_,1,_,1,_,1,_,1,_,1,_],
        [1,_,1,_,1,_,1,_,1,_,1,_,1],
        [_,1,_,1,_,1,_,1,_,1,_,1,_],
        [1,_,1,_,1,_,1,_,1,_,1,_,1],
        [_,1,_,1,_,1,_,1,_,1,_,1,_],
        [1,_,1,_,1,_,1,_,1,_,1,_,1]  ]
    t.assertEqual(1, s.maxAreaOfIsland(grid))

    print('OK!')
    
    
    