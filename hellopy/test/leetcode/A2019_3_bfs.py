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
                        dis += 1
                        nxtile[2] = min(dis, nxt[2])
                        edge.append(tuple(nxtile))

        return dis

class Test(unittest.TestCase):


    def testBFSDist(self):
        s = Solution()
        self.assertEqual(5, s.distanceDFS(
            [[' ', ' ', ' ', ' '],
             ['D', ' ', 'D', ' '],
             [' ', ' ', ' ', ' '],
             ['X', 'D', 'D', ' ']]))
#  
#         self.assertEqual(5, s.distanceBFS(
#             [[' ', ' ', ' ', ' ', ' '],
#              [' ', 'D', 'D', ' ', 'X'],
#              [' ', 'D', ' ', ' ', ' '],
#              [' ', 'D', ' ', 'D', ' '],
#              [' ', ' ', ' ', 'D', ' '],
#              [' ', 'D', 'D', 'D', ' ']]))
#  
#         self.assertEqual(14, s.distanceBFS(
#             [[' ', ' ', ' ', ' ', ' '],
#              [' ', 'D', 'D', 'D', ' '],
#              [' ', 'D', ' ', ' ', ' '],
#              [' ', 'D', ' ', 'D', ' '],
#              [' ', ' ', ' ', 'D', ' '],
#              ['D', 'D', 'D', 'D', ' '],
#              ['X', ' ', ' ', ' ', ' ']]))

        # Deep first won't work here, the longer path is found
        self.assertEqual(19, s.distanceDFS(
            [[' ', ' ', ' ', ' ', ' ', ' ', 'D', 'X'],
             [' ', 'D', 'D', 'D', 'D', ' ', 'D', ' '],
             [' ', 'D', ' ', ' ', ' ', ' ', 'D', ' '],
             [' ', 'D', ' ', 'D', 'D', ' ', 'D', ' '],
             [' ', ' ', ' ', 'D', 'D', ' ', ' ', ' ']]))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()