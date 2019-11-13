'''
Max Of Min Altitudes

https://leetcode.com/discuss/interview-question/383669/

Created on 13 Nov 2019
@author: odys-z@github.com
'''

import unittest
from typing import List

class Tile:
    def __init__(self, tiles, i, j):
        self.i = i
        self.j = j
        self.r = len(tiles)
        self.c = len(tiles[i])
        self.tiles = tiles

    def stepj(self) -> int:
        '''
        :rtype: int min cost if go left path
        '''
        i, j = self.i, self.j
        r, c = self.r, self.c  # @UnusedVariable

        if j + 1 >= c:
            return float('Inf')
        else:
            return min(self.tiles[i][j], self.tiles[i][j + 1])

    def stepi(self) -> int:
        '''
        :rtype: int min cost if go down path
        '''
        i, j = self.i, self.j
        r, c = self.r, self.c  # @UnusedVariable

        if i + 1 >= r:
            return float('Inf')
        else:
            return min(self.tiles[i][j], self.tiles[i + 1][j])
    
    def maxMin(self, costi, costj):
        self.tiles[self.i][self.j] = max(costi if costi != float("Inf") else 0,
                                         costj if costj != float("Inf") else 0)
    

class DiagnalLine:
    def __init__(self, u, d, l, r):
        self.u = u
        self.d = d
        self.l = l
        self.r = r
        self.i, self.j = d, l

    def diagque(self):
        q = self
        while True:
            if q.i < q.u or q.j > q.r:
                yield None
            else:
                yield q.i, q.j
                q.i -= 1
                q.j += 1

class Solution:
    
    def nextDiag(self, que: DiagnalLine) -> DiagnalLine:
        if (que.d == 0 and que.l == 0):
            return None
        
        d, l = que.d, que.l - 1
        while l < 0: # not much, should be only once
            l += 1
            d -= 1

        u, r = que.u - 1, que.r
        while u < 0: # not much, should be only once
            u += 1
            r -= 1

        q = DiagnalLine(u, d, l, r) 
        return q
        
    
    def maxMinCost(self, r: int , c: int , tileMap: List[List[int]]) -> int:
        ''' 1. for tile(i, j), find 2 good path's min cost to tile(i + 1, j) and tile(i, j + 1)
                    cost(i, j)[0] = min(tile(i, j), maxMin(i + 1, j)
                    cost(i, j)[1] = min(tile(i, j), maxMin(i, j + 1)
            2. maxMin(i, j) = max(cost(i, j))
        '''
        
        tileMap[0][0] = float("Inf")
        tileMap[r - 1][c - 1] = float("Inf")

        # searching queue for [r-1, c-1]
        diag = self.nextDiag(DiagnalLine(r-1, r-1, c-1, c-1))
        que = diag.diagque()
        nxt = next(que)
        while nxt:
            tile = Tile(tileMap, nxt[0], nxt[1])
            costi = tile.stepi()
            costj = tile.stepj()
            tile.maxMin(costi, costj)
            nxt = next(que)
            if nxt is None:
                # iterate on a new diagnal line
                diag = self.nextDiag(diag)
                if diag is not None:
                    que = diag.diagque()
                    nxt = next(que)

        return tileMap[0][0]

class Test(unittest.TestCase):

    def testOA(self):
        sl = Solution()
        self.assertEqual(3, sl.maxMinCost(
            3, 4, [[1, 2, 5, 2],
                   [4, 3, 8, 1],
                   [3, 9, 7, 1]]))

        self.assertEqual(2, sl.maxMinCost(
            3, 3, [[1,3,1],
                   [1,5,1],
                   [4,2,1] ]))

        self.assertEqual(4, sl.maxMinCost(
            2, 2, [[5, 1],
                   [4, 5]]))

        self.assertEqual(4, sl.maxMinCost(
            2, 3, [[1, 2, 3],
                   [4, 5, 1]]))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
