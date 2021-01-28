'''
    62. Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the
 diagram below).

The robot can only move either down or right at any point in time. The robot is
trying to reach the bottom-right corner of the grid (marked 'Finish' in the
diagram below).

How many possible unique paths are there?

Input: m = 3, n = 7
Output: 28
'''

class Solution:
    '''
    6%
    '''
    def uniquePaths(self, m: int, n: int) -> int:
        mn = [[0] * (n)] * (m)
        mn[m-1][n-1] = 1
        for c in range(n-2, -1, -1):
            mn[m-1][c] = 1
        for r in range(m-2, -1, -1):
            mn[r][n-1] = 1

        for r in range(m-2, -1, -1):
            for c in range(n-2, -1, -1):
                mn[r][c] = mn[r+1][c] + mn[r][c+1]

        # print(mn)
        return mn[0][0]
