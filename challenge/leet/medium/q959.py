'''
959. Regions Cut By Slashes
https://leetcode.com/problems/regions-cut-by-slashes/

In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.  
These characters divide the square into contiguous regions.

(Note that backslash characters are escaped, so a \ is represented as "\\".)

Return the number of regions.

Example 1:

Input:
[ " /",
  "/ " ]
Output: 2
Explanation: The 2x2 grid is as follows:

 ------
 |   /|
 |  / |
 | /  |
 |/   |
 ------

Created on 26 Mar 2021

@author: Odys Zhou
'''
from unittest import TestCase
from typing import List

class Dsu:
    def __init__(self, N):
        self.triangles = [i for i in range(N * N * 4)]
        self.rank = [0] * (4 * N * N)

    def find(self, x):
        while self.triangles[x] != x:
            x = self.triangles[x]
        return x
    
    def merge(self, a, b):
        x, y = self.find(a), self.find(b)
        if x == y:
            return False
        if self.rank[x] < self.rank[y]:
            self.triangles[x] = y
            self.rank[y] += 1
        else:
            self.triangles[y] = x
            self.rank[x] += 1
        return True
            
'''
  0
 1 2
  3
'''
class DSUSolution:
    '''
    76.00% 
    '''
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        dsu = Dsu(n)
        for x in range(n):
            for y in range(n):
                t0 = 4 * ((x * n) + y)
                t1, t2, t3 = t0 + 1, t0 + 2, t0 + 3
                if grid[x][y] == '/':
                    dsu.merge(t0, t1)
                    dsu.merge(t2, t3)
                elif grid[x][y] == '\\':
                    dsu.merge(t0, t2)
                    dsu.merge(t1, t3)
                else:
                    dsu.merge(t0, t1)
                    dsu.merge(t1, t2)
                    dsu.merge(t2, t3)
                
                if x < n - 1:
                    south, north = t3, t0 + n * 4
                    dsu.merge(south, north)
                if x > 1:
                    south, north = t3 - n * 4, t0
                    dsu.merge(south, north)

                if y < n - 1:
                    east, west = t2, t1 + 4
                    dsu.merge(east, west)
                if y > 1:
                    east, west = t2 - 4, t1
                    dsu.merge(east, west)

        res = 0
        for i in range(4 * n * n):
            res += 1 if dsu.find(i) == i else 0

        return res

class DFSSolution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        '''24.92%
        '''
        N = len(grid)
        tiles = [[0] * (N * 3) for _ in range(3*N)]
        for r in range(N):
            for c in range(N):
                if grid[r][c] == '/':
                    tiles[3*r][3*c+2] = tiles[3*r+1][3*c+1] = tiles[3*r+2][3*c] = 1
                elif grid[r][c] == '\\':
                    tiles[3*r][3*c] = tiles[3*r+1][3*c+1] = tiles[3*r+2][3*c+2] = 1
        # DFS
        def dfs(cells, x, y):
            if (0 <= x < 3 * N and  0 <= y < 3 * N
                and cells[x][y] == 0):
                    cells[x][y] = 1
                    for dx, dy in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]:
                        dfs(cells, dx, dy)
        
        res = 0
        for r in range(N * 3):
            for c in range(N * 3):
                if tiles[r][c] == 0:
                    res += 1
                    dfs(tiles, r, c)
        return res;
                

if __name__ == '__main__':
    t = TestCase()
    s = DSUSolution()
    r = DFSSolution()
    
    t.assertEqual(2, s.regionsBySlashes([" /", "/ "]))
    t.assertEqual(2, r.regionsBySlashes([" /", "/ "]))
    t.assertEqual(5, s.regionsBySlashes(["/\\", "\\/"]))
    t.assertEqual(5, r.regionsBySlashes(["/\\", "\\/"]))
    t.assertEqual(3, s.regionsBySlashes(["//", "/ "]))
    t.assertEqual(3, r.regionsBySlashes(["//", "/ "]))
    t.assertEqual(4, s.regionsBySlashes(["// ", "/  ", "  /"]))
    t.assertEqual(4, r.regionsBySlashes(["// ", "/  ", "  /"]))
    
    print('OK!')