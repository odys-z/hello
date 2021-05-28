'''
172. Factorial Trailing Zeroes
https://leetcode.com/problems/factorial-trailing-zeroes/

Given an integer n, return the number of trailing zeroes in n!.

Follow up: Could you write a solution that works in logarithmic time complexity?
'''
class Solution:
    '''
    53.52%
    '''
    def trailingZeroes(self, n: int) -> int:
        zeros, p2, exp = 0, 5, 1
        while p2 <= n:
            zeros += n // p2
            exp += 1
            p2 = 5 ** exp
        return zeros
