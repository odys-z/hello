'''
1314. Matrix Block Sum
https://leetcode.com/problems/matrix-block-sum/

Given a m * n matrix mat and an integer K, return a matrix answer where each answer[i][j] is
the sum of all elements mat[r][c] for i - K <= r <= i + K, j - K <= c <= j + K, and (r, c)
is a valid position in the matrix.
 
Example 1:
    Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
    Output: [[12,21,16],[27,45,33],[24,39,28]]

Example 2:
    Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
    Output: [[45,45,45],[45,45,45],[45,45,45]]
 

Constraints:
    m == mat.length
    n == mat[i].length
    1 <= m, n, K <= 100
    1 <= mat[i][j] <= 100

Hint 1:
How to calculate the required sum for a cell (i,j) fast ?

Hint 2:
Use the concept of cumulative sum array.

Hint 3:
Create a cumulative sum matrix where dp[i][j] is the sum of all cells in the rectangle
from (0,0) to (i,j), use inclusion-exclusion idea.
'''
from unittest import TestCase
from typing import List

class Solution:
    '''
    70.85% 
    '''
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        # dp
        m, n = len(mat), len(mat[0])
        dp = [[0] * (n+K) for _ in range(m+K)]

        for r in range(m):
            dp[r][0] = mat[r][0]
            for c in range(1, n+K):
                if c < n:
                    dp[r][c] = mat[r][c] + dp[r][c-1] 
                else:
                    dp[r][c] = dp[r][c-1] 

        for c in range(n+K):
            for r in range(1, m+K):
                if r < m:
                    dp[r][c] += dp[r-1][c]
                else:
                    dp[r][c] = dp[r-1][c]
        
        for r in range(m):
            for c in range(n):
                mat[r][c] = dp[r+K][c+K]
                if 0 <= r - K - 1:
                    mat[r][c] -= dp[r-K-1][c+K]
                if 0 <= c - K - 1:
                    mat[r][c] -= dp[r+K][c-K-1]
                if 0 <= r - K - 1 and 0 <= c - K - 1:
                    mat[r][c] += dp[r-K-1][c-K-1]
        return mat

if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    t.assertCountEqual([[12,21,16],[27,45,33],[24,39,28]],
                       s.matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]], 1))
    t.assertCountEqual([[45,45,45],[45,45,45],[45,45,45]],
                       s.matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]], 2))
    print("OK!")