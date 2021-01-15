'''
rotate matrix
'''
from unittest import TestCase
from typing import List
from utils.assertHelper import assertIntsEqual

class Transform():
    def __init__(self, m, n):
        self.m, self.n = m, n
        self.r05, self.c05 = m // 2, (n + 1) //2

    def quad(self, x, y):
        # x, y must in the upper left part
        def rot(r, c):
            r, c = c, self.n - 1 - r
            return r, c

        res = [(x, y)] 
        for _ in range(3):
            x, y = rot(x, y)
            res.append((x, y))
        return res

class Solution2:
    '''
    Runtime: 36 ms, faster than 60.27% of Python3 online submissions for Rotate Image.
    Memory Usage: 14.4 MB, less than 29.44% of Python3 online submissions for Rotate Image.
    '''
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
          [0, 0] --|--  [0,   c-1]
                   |
        -----------|-----------
                   |
          [r-1,0]--|--  [r-1, c-1]

         [r-1, 0]--|--  [0, 0]
                   |
        -----------|-----------
                   |
        [r-1,c-1]--|--  [0, c-1]
        """
        def rotate(m, q):
            # rotate quadruple elements in matrix
            x0, y0 = q[0]
            x1, y1 = q[1]
            x2, y2 = q[2]
            x3, y3 = q[3]
            m[x1][y1], m[x2][y2], m[x3][y3], m[x0][y0] = m[x0][y0], m[x1][y1], m[x2][y2], m[x3][y3]

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 

        rows, cols = len(matrix), len(matrix[0])
        trans = Transform(rows, cols)
        # r05, c05 = (rows + 1) // 2, (cols + 1) // 2
        for r in range(trans.r05):
            for c in range(trans.c05):
                q = trans.quad(r, c)
                rotate(matrix, q)
        return matrix
        
class Solution:
    '''
    Runtime: 32 ms, faster than 83.55% of Python3 online submissions for Rotate Image.
    Memory Usage: 14.3 MB, less than 58.13% of Python3 online submissions for Rotate Image.
    '''
    def rotate(self, matrix: List[List[int]]) -> None:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 

        m, n = len(matrix), len(matrix[0])
        for r in range(m // 2):
            for c in range((n + 1) // 2):
                r0, c0 = c, n - 1 - r
                r1, c1 = c0, n - 1 - r0
                r2, c2 = c1, n - 1 - r1
                r3, c3 = c2, n - 1 - r2
                matrix[r1][c1], matrix[r2][c2], matrix[r3][c3], matrix[r0][c0] = matrix[r0][c0], matrix[r1][c1], matrix[r2][c2], matrix[r3][c3]

        return matrix
 
if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    
    assertIntsEqual([[7,4,1],[8,5,2],[9,6,3]],
                    s.rotate([[1,2,3],[4,5,6],[7,8,9]]))
    assertIntsEqual([[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]],
                    s.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
    
    print("OK!")