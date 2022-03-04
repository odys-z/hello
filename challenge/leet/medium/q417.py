'''
417. Pacific Atlantic Water Flow
https://leetcode.com/problems/pacific-atlantic-water-flow/

'''

from unittest import TestCase
from typing import List

class Land:
    def __init__(self, x, y, h):
        self.x, self.y, self.h = x, y, h
        self.vp, self.va, self.p, self.a = False, False, False, False

class Solution:
    '''
    46.93% 
    '''
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        X, Y = len(heights[0]), len(heights)
        lands = [ [Land(x, y, heights[y][x]) for y in range(Y)] for x in range(X) ]
        
        def floodPacific(land: Land, dx, dy):
            x, y, h = land.x, land.y, land.h
            x1, y1 = x + dx, y + dy

            if 0 <= x1 < X and 0 <= y1 < Y:
                nxt = lands[x + dx][y + dy]
                if h > nxt.h or nxt.vp:
                    return None
                else:
                    return nxt
            else: return None

        def floodAtlantic(land: Land, dx, dy):
            x, y, h = land.x, land.y, land.h
            x1, y1 = x + dx, y + dy

            if 0 <= x1 < X and 0 <= y1 < Y:
                nxt = lands[x + dx][y + dy]
                if h > nxt.h or nxt.va:
                    return None
                else:
                    return nxt
            else: return None


        # Pacific, Atlantic
        P, A = [], []
        
        for x in range(X):
            land = lands[x][0]
            land.p, land.vp = True, True

            P.append(land)

            land = lands[x][-1]
            land.a, land.va = True, True

            A.append(land)

        for y in range(0, Y-1): 
            land = lands[0][y+1]
            land.p, land.vp = True, True

            P.append(land)

            land = lands[-1][y]
            land.a, land.va = True, True

            A.append(land)

        # Pacific flood - unknown Atlantic
        while len(P) > 0:
            P_ = [] 
            
            for p in P:
                for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    nxt = floodPacific(p, dx, dy)
                    
                    if nxt != None:
                        nxt.p = True
                        nxt.vp = True
                        P_.append(nxt)
            P = P_[:]
            
        both = []
        # Atlantic flood - known Pacific
        while len(A) > 0:
            A_ = [] 

            
            for a in A:
                for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    nxt = floodAtlantic(a, dx, dy)
                    
                    if nxt != None:
                        nxt.a = True
                        nxt.va = True
                        A_.append(nxt)
                
                if a.a and a.p:
                    both.append([a.y, a.x])

            A = A_[:]
        
        return both

t = TestCase()
s = Solution()

t.assertCountEqual([[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]],
    s.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))

t.assertCountEqual([[0,0],[0,1],[1,0],[1,1]],
    s.pacificAtlantic([[2, 1], [1, 2]]))

t.assertCountEqual( [[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]], 
    s.pacificAtlantic([[1,2,3],
                       [8,9,4],
                       [7,6,5]]))

t.assertCountEqual( [[0,3],[1,0],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[2,3],[3,0],[3,1],[3,2],[3,3]], 
    s.pacificAtlantic([[1, 2, 3, 4],
                       [12,13,14,5],
                       [11,16,15,6],
                       [10, 9, 8,7]]))
print("OK!")
