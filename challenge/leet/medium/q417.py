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
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        X, Y = len(heights[0]), len(heights)
        lands = [ [Land(x, y, heights[x][y]) for y in range(Y)] for x in range(X) ]
        
        # only for Pacific
        def right(land):
            if x >= X - 1: return None

            x, y, h = land.x, land.y, land.h
            r = lands[x+1][y]

            if h > lands[x+1][y].h or lands[x+1][y].vp:
                return None
            else:
                return lands[land.x+1][lands.y]

        def down(land):
            if land.y >= Y-1 or land.h > lands[land.x][land.y+1].h:
                return None
            else:
                return lands[land.x][lands.y+1]

        def left(land):
            if land.x <= 0 or land.h > lands[land.x-1][land.y].h:
                return None
            else:
                return lands[land.x-1][lands.y]

        def up(land):
            if land.y <= 0 or land.h > lands[land.x][land.y-1].h:
                return None
            else:
                return lands[land.x][lands.y-1]

        # Pacific, Atlantic
        P, A = [], []
        
        for x in range(X):
            land = lands[x][0]
            land.p, land.vp = True, True

            P.append(land)

            land = lands[x][-1]
            land.a, land.va = True, True

            A.append(land)

        for y in range(Y): 
            land = lands[0][y]
            land.p, land.vp = True, True

            P.append(land)

            land = lands[-1][y]
            land.a, land.va = True, True

            A.append(land)

        # Pacific flood - unknown Atlantic
        while len(P) > 0:
            p = [] 
            
            right, down = right(p), down(p)
            
            if right != None:
                right.p = True
                p.push(right)
            if down != None:
                down.p = True
                p.push(down)
            
        both = []
        # Atlantic flood - known Pacific
        while len(A) > 0:
            a = [] 

            left, up = left(a), up(a)
            
            if left != None:
                left.a = True
                a.push(right)
                if left.p: both.append(left)
            if up != None:
                up.a = True
                a.push(up)
                if up.p: both.append(up)
        
        return both

t = TestCase()
s = Solution()

t.assertCountEqual([[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]],
    s.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))

t.assertCountEqual([[0,0],[0,1],[1,0],[1,1]],
    s.pacificAtlantic([[2, 1], [1, 2]]))

print("OK!")
