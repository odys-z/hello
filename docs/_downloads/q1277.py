'''
1277. Count Square Submatrices with All Ones
https://leetcode.com/problems/count-square-submatrices-with-all-ones/

Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]

Output: 15

Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.


  [0,1,2, 3],
  [1,3,5, 7],
  [1,4,7, 10]
'''

from unittest import TestCase
from typing import List

class Solution1:
    '''
    Time Limit Exceeded
    '''
    def countSquares(self, matrix: List[List[int]]) -> int:
        sqr = sum(matrix[0])
        # sum up
        for x in range(len(matrix[0])):
            for y in range(1, len(matrix)):
                if matrix[y][x] == 1:
                    sqr += 1
                matrix[y][x] += matrix[y-1][x]
        for y in range(len(matrix)):
            for x in range(1, len(matrix[y])):
                matrix[y][x] += matrix[y][x-1]

        # find all 0 - i, 0 - j for (i, j)
        for y in range(1, len(matrix)):
            for x in range(1, len(matrix[y])):
                for gap in range(1, min(x + 1, y + 1)):
                    side = gap + 1
                    count1 = matrix[y][x]
                    r, c = y - side, x - side 
                    if 0 <= r and 0 <= c:
                        count1 += matrix[r][c]
                    if 0 <= r:
                        count1 -= matrix[r][x]
                    if 0 <= c:
                        count1 -= matrix[y][c]
                    if count1 == side * side:
                        sqr += 1
        return sqr

class Solution:
    '''
    95.88%
    '''
    def countSquares(self, matrix: List[List[int]]) -> int:
        res = sum(matrix[0])
        for y in range(1, len(matrix)):
            res += matrix[y][0]
            for x in range(1, len(matrix[y])):
                if matrix[y][x] == 1:
                    matrix[y][x] = min(matrix[y-1][x-1], matrix[y][x-1], matrix[y-1][x]) + 1
                res += matrix[y][x]
                
        return res

if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    t.assertEqual(15, s.countSquares([[0,1,1,1], [1,1,1,1], [0,1,1,1]])) 
    t.assertEqual(7, s.countSquares([[1,0,1], [1,1,0], [1,1,0]]))
    
    print('OK!')