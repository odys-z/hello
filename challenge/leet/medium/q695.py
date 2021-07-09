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
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        
        def parentOf(islands, ix):
            p = islands.get(ix)
            while islands.has(ix):
                p = islands.get(ix)
                if (p[0] * row + p[1] != ix):
                    ix == p[0] * row + p[1]
                else:
                    return p
            
            return islands.get(ix)
        
        def dsu(islands, grid):
            for r in grid:
                for c in r:
                    if grid[r][c] != 1 or islands.has(r * row + c):
                        continue

                    # new found land
                    p0 = islands.get(r * row + c)
                    if not p0:
                        p0 = (r, c)
                        islands.update({r * row + c: p0})

                    adjs = [(r-1, c), (r, c-1), (r+1, c), (r, c+1)]
                    for x, y in adjs:
                        if 0 <= x < row and 0 <= y < col:
                            ix = x * row + y
                            p = parentOf(islands, ix)
                            islands.update({ix: p})
                                    
                                


        islands = dict() # {ix: parent}
        dsu(islands, grid)
        
        


if __name__ == '__main__':
    s = Solution()
    
    t = TestCase()