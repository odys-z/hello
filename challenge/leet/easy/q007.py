'''
7. Reverse Integer
https://leetcode.com/problems/reverse-integer/

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0

'''

from unittest import TestCase

class Solution:
    '''
    89.51%
    '''
    def reverse(self, x: int) -> int:
        if x > 2**31 -1 or x < -(2**31):
            return 0
        
        posi, x, y = x >= 0, abs(x), 0
        while x > 0:
            x, r = x // 10, x % 10
            y = y * 10 + r
            if posi and y > 2**31 - 1 or not posi and y > 2 ** 31:
                return 0
        return y if posi else -y
    
if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    t.assertEqual(321, s.reverse(123))
    t.assertEqual(21, s.reverse(120))
    t.assertEqual(0, s.reverse(1534236469))
    t.assertEqual(0, s.reverse(-1534236469))
    
    print('OK!')