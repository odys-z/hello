'''
Treasure Island
https://leetcode.com/discuss/interview-question/347457

Created on 15 Nov 2019

@author: odys-z@github.com
'''
import unittest
from typing import List
from _collections import deque

class Solution(object):
    def distanceDFS(self, tiles: List[List[int]]):
        r = len(tiles)
        c = len(tiles[0])
        dis = 0
        tiles[0][0] = 'D'
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#         path = [] # (tile-xy), [(step-dir)] ]
        edge = deque([(0, 0, 0)]) # searching tiles x, y, dist
        while edge:
            x, y, dis = edge.pop() # pop last, depth first
            for dx, dy in dirs:
                nxt = (x + dx, y + dy, dis + 1)
                if 0 <= nxt[0] < r and 0 <= nxt[1] < c:
                    if tiles[nxt[0]][nxt[1]] == 'X':
                        return dis + 1
                    elif tiles[nxt[0]][nxt[1]] == ' ':
                        tiles[nxt[0]][nxt[1]] = 'D'
                        nxtile = list(nxt)
                        nxtile[2] = min(dis + 1, nxt[2])
                        edge.append(tuple(nxtile))

        return dis

    def distanceBFS(self, tiles: List[List[int]]):
        r = len(tiles)
        c = len(tiles[0])
        dis = 0
        tiles[0][0] = 'D'
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        edge = deque([(0, 0, 0)]) # searching tiles x, y, dist
        while edge:
            x, y, dis = edge.popleft() # pop first, breadth first
            for dx, dy in dirs:
                nxt = (x + dx, y + dy, dis + 1)
                if 0 <= nxt[0] < r and 0 <= nxt[1] < c:
                    if tiles[nxt[0]][nxt[1]] == 'X':
                        return dis + 1
                    elif tiles[nxt[0]][nxt[1]] == ' ':
                        tiles[nxt[0]][nxt[1]] = 'D'
                        nxtile = list(nxt)
                        nxtile[2] = min(dis + 1, nxt[2])
                        edge.append(tuple(nxtile))

        return dis

class Pathpoint(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.to = None
        self.cost = float("Inf")
    
    def pathto(self, tox: int, toy: int, cost: int) -> 'Pathpoint':
        if cost < self.cost:
            self.cost = cost
            self.to = (tox, toy)
        return self
    
class AStarFinder(object):

    def findpath(self, tiles: List[List[int]]):
        r = len(tiles)
        c = len(tiles[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        endpoint = None
        
        # BFS build distance
        edge = deque([Pathpoint(0, 0).pathto(0, 0, 0)]) # searching tiles x, y, dist
        while edge:
            p = edge.popleft() # pop first, breadth first
            for dx, dy in dirs:
                nxtp = Pathpoint(p.x + dx, p.y + dy)
                if 0 <= nxtp.x < r and 0 <= nxtp.y < c:
                    nxtp.pathto(p.x, p.y, p.cost + 1)
                    if tiles[nxtp.x][nxtp.y] == 'X':
                        tiles[nxtp.x][nxtp.y] = nxtp
                        endpoint = nxtp
                        edge.clear()
                        break
                    elif tiles[nxtp.x][nxtp.y] == 'D':
                        # not a path point
                        pass
                    elif isinstance(tiles[nxtp.x][nxtp.y], Pathpoint):
                        if p.cost + 1 < tiles[nxtp.x][nxtp.y].cost:
                            tiles[nxtp.x][nxtp.y].pathto(p.x, p.y, p.cost + 1)
                    else:
                        tiles[nxtp.x][nxtp.y] = nxtp
                        edge.append(nxtp)

        dis = 0
        path = []
        p = endpoint
        while p:
            dis += 1
            path.append((p.x, p.y))
            if p.to:
                p = tiles[p.to[0]][p.to[1]]
                if (p.x, p.y) == (0, 0):
                    p = None
            else:
                p = None
        
        return (dis, path)


def printiles(tiles, path):
    for row in tiles:
        for p in row:
            if isinstance(p, str):
                print('   ' + p, end = '   ')
            else:
                print((p.x, p.y), end = ' ')
        print('')
    
    print(*path, sep = ' <- ')


class Test(unittest.TestCase):

    def testDFSDist(self):
        s = Solution()
        self.assertEqual(5, s.distanceDFS(
            [[' ', ' ', ' ', ' '],
             ['D', ' ', 'D', ' '],
             [' ', ' ', ' ', ' '],
             ['X', 'D', 'D', ' ']]))
  
        self.assertEqual(5, s.distanceDFS(
            [[' ', ' ', ' ', ' ', ' '],
             [' ', 'D', 'D', ' ', 'X'],
             [' ', 'D', ' ', ' ', ' '],
             [' ', 'D', ' ', 'D', ' '],
             [' ', 'D', ' ', 'D', ' '],
             [' ', 'D', ' ', 'D', ' ']]))
  
        self.assertEqual(14, s.distanceDFS(
            [[' ', ' ', ' ', ' ', ' '],
             [' ', 'D', 'D', 'D', ' '],
             [' ', 'D', ' ', 'D', ' '],
             [' ', 'D', ' ', 'D', ' '],
             [' ', ' ', ' ', 'D', ' '],
             ['D', 'D', 'D', 'D', ' '],
             ['X', ' ', ' ', ' ', ' ']]))

        # Deep first won't work here, the longer path is found
        self.assertEqual(19, s.distanceDFS(
            [[' ', ' ', ' ', ' ', ' ', ' ', 'D', 'X'],
             [' ', 'D', 'D', 'D', 'D', ' ', 'D', ' '],
             [' ', 'D', ' ', ' ', ' ', ' ', 'D', ' '],
             [' ', 'D', ' ', 'D', 'D', ' ', 'D', ' '],
             [' ', ' ', ' ', 'D', 'D', ' ', ' ', ' ']]))
  
    def testBFSDist(self):
        s = Solution()
        self.assertEqual(5, s.distanceBFS(
            [[' ', ' ', ' ', ' '],
             ['D', ' ', 'D', ' '],
             [' ', ' ', ' ', ' '],
             ['X', 'D', 'D', ' ']]))
 
        self.assertEqual(5, s.distanceBFS(
            [[' ', ' ', ' ', ' ', ' '],
             [' ', 'D', 'D', ' ', 'X'],
             [' ', 'D', ' ', ' ', ' '],
             [' ', 'D', ' ', 'D', ' '],
             [' ', 'D', ' ', 'D', ' '],
             [' ', ' ', ' ', 'D', ' ']]))

        self.assertEqual(14, s.distanceBFS(
            [[' ', ' ', ' ', ' ', ' '],
             [' ', 'D', 'D', 'D', ' '],
             [' ', 'D', ' ', ' ', ' '],
             [' ', 'D', ' ', 'D', ' '],
             [' ', ' ', ' ', 'D', ' '],
             ['D', 'D', 'D', 'D', ' '],
             ['X', ' ', ' ', ' ', ' ']]))

        # Deep first won't work here, the longer path is found
        self.assertEqual(15, s.distanceBFS(
            [[' ', ' ', ' ', ' ', ' ', ' ', 'D', 'X'],
             [' ', 'D', 'D', 'D', 'D', ' ', 'D', ' '],
             [' ', 'D', ' ', ' ', ' ', ' ', 'D', ' '],
             [' ', 'D', ' ', 'D', 'D', ' ', 'D', ' '],
             [' ', ' ', ' ', 'D', 'D', ' ', ' ', ' ']]))

    def testAstar(self):
        s = AStarFinder()
        tiles = [[' ', ' ', ' ', ' ', ' ', ' ', 'D', 'X'],
                 [' ', 'D', 'D', 'D', 'D', ' ', 'D', ' '],
                 [' ', 'D', ' ', ' ', ' ', ' ', 'D', ' '],
                 [' ', 'D', ' ', 'D', 'D', ' ', 'D', ' '],
                 [' ', ' ', ' ', 'D', 'D', ' ', ' ', ' ']]
        pth = s.findpath(tiles)
        printiles(tiles, pth[1])
        self.assertEqual(15, pth[0])
        self.assertEqual([(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (4, 6), (4, 5), (3, 5), (2, 5), (1, 5), (0, 5), (0, 4), (0, 3), (0, 2), (0, 1)],
                         pth[1])

        print()
        tiles = [[' ', ' ', ' ', ' ', ' '],
                 [' ', 'D', 'D', 'D', ' '],
                 [' ', 'D', ' ', ' ', ' '],
                 [' ', 'D', ' ', 'D', ' '],
                 [' ', ' ', ' ', 'D', ' '],
                 ['D', 'D', 'D', 'D', ' '],
                 ['X', ' ', ' ', ' ', ' ']]
        pth = s.findpath(tiles)
        printiles(tiles, pth[1])
        self.assertEqual(14, pth[0])
        self.assertEqual([(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (5, 4), (4, 4), (3, 4), (2, 4), (1, 4), (0, 4), (0, 3), (0, 2), (0, 1)],
                         pth[1])
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()