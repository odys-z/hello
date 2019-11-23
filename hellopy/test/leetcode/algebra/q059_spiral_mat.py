'''
Created on 10 Nov 2019

https://leetcode.com/problems/spiral-matrix-ii/
26ms

@author: ody
'''
import unittest

def odds(n):
    odds = [2 * n + 1 for n in range(n ** 2)]
    n2 = 0
    for odd in odds:
        n2 += odd
        yield n2

def inc(n):
    n = 0
    while True:
        n += 1
        yield n
        
def peelMat(n, mat, sqrs, u, d, l, r):
    if (u == d and l == r):
        mat[u * n + l] = next(sqrs)
        return

    for cx in range(l, r):
        # print('up row', (u, cx))
        # mat[u][cx] = next(sqrs)
        mat[u * n + cx] = next(sqrs)
        
    for rx in range(u, d):
        # print('right col', (rx, r))
        # mat[rx][r] = next(sqrs)
        mat[rx * n + r] = next(sqrs)

    for cx in range(r, l, -1):
        # print('dow row', (d, cx))
        # mat[d][cx] = next(sqrs)
        mat[d * n + cx] = next(sqrs)
        
    for rx in range(d, u, -1):
        # print('left col', (rx, l))
        # mat[rx][l] = next(sqrs)
        mat[rx * n + l] = next(sqrs)
    
    if l + 1 < r:
        peelMat(n, mat, sqrs, u + 1, d - 1, l + 1, r -1)
       

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
                
        # mat = [[0 for _ in range(n)] for _ in range(n)]
        mat = [0 for _ in range(n ** 2)]
        
        l = u = 0  # left up
        r = d = n - 1 # right down
        peelMat(n, mat, odds(n), u, d, l, r)
        
        # print(mat)
        return [mat[i : i + n] for i in range(0, len(mat),  n)]



class Test(unittest.TestCase):

    def test059(self):
        s = Solution()
        self.assertEqual([[ 1,  4,  9],
                          [64, 81, 16],
                          [49, 36, 25]],
                          s.generateMatrix(3))
