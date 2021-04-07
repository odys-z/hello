'''
Treasure Island II
https://leetcode.com/discuss/interview-question/356150

Created on 15 Nov 2019

@author: odys-z@github.com
'''
import unittest
from typing import List
from _collections import deque

# class Solution(object):

#     def distanceBFS(self, tiles: List[List[int]]):
#         r = len(tiles)
#         c = len(tiles[0])
#         dis = 0
#         tiles[0][0] = 'D'
#         dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#         edge = deque([(0, 0, 0)]) # searching tiles x, y, dist
#         while edge:
#             x, y, dis = edge.popleft() # pop first, breadth first
#             for dx, dy in dirs:
#                 nxt = (x + dx, y + dy, dis + 1)
#                 if 0 <= nxt[0] < r and 0 <= nxt[1] < c:
#                     if tiles[nxt[0]][nxt[1]] == 'X':
#                         return dis + 1
#                     elif tiles[nxt[0]][nxt[1]] == ' ':
#                         tiles[nxt[0]][nxt[1]] = 'D'
#                         nxtile = list(nxt)
#                         nxtile[2] = min(dis + 1, nxt[2])
#                         edge.append(tuple(nxtile))
# 
#         return dis

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
        
        # O(m * n)
        # Find first X to start
        start = None
        for rx in range(len(tiles)):
            for cx in range(len(tiles[rx])):
                if tiles[rx][cx] == 'X':
                    start = Pathpoint(rx, cx).pathto(rx, cx, 0)
                    tiles[rx][cx] = start
        if start == None:
            # no start?
            return 'What is happening?'
            
        # O(m * n)
        # BFS build distance
        edge = deque([start]) # searching tiles x, y, dist
        while edge:
            p = edge.popleft() # pop first, breadth first
            for dx, dy in dirs:
                if 0 <= p.x + dx < r and 0 <= p.y + dy < c:
                    nxtp = Pathpoint(p.x + dx, p.y + dy).pathto(p.x, p.y, p.cost + 1)
                    if tiles[nxtp.x][nxtp.y] == 'S':
                        tiles[nxtp.x][nxtp.y] = nxtp
                        endpoint = nxtp
                        edge.clear()
                        break
                    elif tiles[nxtp.x][nxtp.y] == 'D':
                        # not a path point
                        pass
                    elif tiles[nxtp.x][nxtp.y] == 'X':
                        # found another treasure point, let's update searching queue
                        tiles[nxtp.x][nxtp.y] = Pathpoint(nxtp.x, nxtp.y).pathto(nxtp.x, nxtp.y, 0)
                        if p.cost > 1: # 0 + 1
                            p.pathto(nxtp.x, nxtp.y, 1)
                            edge.append(p)
                    elif isinstance(tiles[nxtp.x][nxtp.y], Pathpoint): # visited point
                        if p.cost + 1 < tiles[nxtp.x][nxtp.y].cost:
                            tiles[nxtp.x][nxtp.y].pathto(p.x, p.y, p.cost + 1)
                    else:
                        tiles[nxtp.x][nxtp.y] = nxtp
                        edge.append(nxtp)

        path = []
        p = endpoint
        dis = p.cost
        while p:
            path.append((p.x, p.y))
            if p.to == (p.x, p.y):
                p = None
            else:
                p = tiles[p.to[0]][p.to[1]]
        
        return (dis, path)


def printiles(tiles, path):
    for row in tiles:
        for p in row:
            if isinstance(p, str):
                print('   ' + p, end = '   ')
            else:
                print((p.x, p.y), end = ' ')
        print('')
    
    print(*path, sep = ' -> ')


class Test(unittest.TestCase):

    def testAstar(self):
        s = AStarFinder()
        tiles = [['S', ' '],
                 [' ', 'X']]
        pth = s.findpath(tiles)
        printiles(tiles, pth[1])
        self.assertEqual(2, pth[0])
        self.assertEqual([(0, 0), (1, 0), (1, 1)], pth[1])
        
        print('-------------------------------------------')
        tiles = [['S', ' ', ' ', ' ', ' ', ' ', 'D', 'X'],
                 [' ', 'D', 'D', 'D', 'D', ' ', 'D', ' '],
                 [' ', 'D', ' ', ' ', ' ', ' ', 'D', ' '],
                 [' ', 'D', ' ', 'D', 'D', ' ', 'D', ' '],
                 [' ', ' ', ' ', 'D', 'D', ' ', ' ', ' ']]
        pth = s.findpath(tiles)
        printiles(tiles, pth[1])
        self.assertEqual(15, pth[0])
        self.assertEqual([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (4, 6), (4, 7), (3, 7), (2, 7), (1, 7), (0, 7)],
                         pth[1])

        print('-------------------------------------------')
        tiles = [['S', ' ', ' ', ' ', ' '],
                 [' ', 'D', 'D', 'D', ' '],
                 [' ', 'D', ' ', ' ', ' '],
                 [' ', 'D', ' ', 'D', ' '],
                 [' ', ' ', ' ', 'D', ' '],
                 ['D', 'D', 'D', 'D', ' '],
                 ['X', ' ', ' ', ' ', ' ']]
        pth = s.findpath(tiles)
        printiles(tiles, pth[1])
        self.assertEqual(14, pth[0])
        p = [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (5, 4), (4, 4), (3, 4), (2, 4), (1, 4), (0, 4), (0, 3), (0, 2), (0, 1), (0, 0)]
        p.reverse(),
        self.assertEqual(p, pth[1])
        
        print('-------------------------------------------')
        tiles = [['S', ' ', ' ', ' ', ' '],
                 [' ', 'D', 'S', 'D', ' '],
                 [' ', 'D', ' ', ' ', ' '],
                 [' ', 'D', ' ', 'D', ' '],
                 [' ', ' ', ' ', 'D', ' '],
                 ['D', 'D', 'D', 'D', ' '],
                 ['X', ' ', ' ', ' ', ' ']]
        pth = s.findpath(tiles)
        printiles(tiles, pth[1])
        self.assertEqual(11, pth[0])
        self.assertEqual([(1, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0)],
                         pth[1])
        
        print('-------------------------------------------')
        tiles = [['X', ' ', ' ', ' ', ' '],
                 [' ', 'D', 'D', 'D', ' '],
                 [' ', 'D', ' ', ' ', ' '],
                 [' ', 'D', ' ', 'D', ' '],
                 [' ', ' ', ' ', 'D', ' '],
                 ['D', 'D', 'D', 'X', ' '],
                 ['S', ' ', ' ', ' ', ' ']]
        pth = s.findpath(tiles)
        printiles(tiles, pth[1])
        self.assertEqual(4, pth[0])
        self.assertEqual([(6, 0), (6, 1), (6, 2), (6, 3), (5, 3)],
                         pth[1])
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()