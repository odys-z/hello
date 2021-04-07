'''
Q 29
https://leetcode.com/problems/divide-two-integers/

Created on 13 Jan 2021

@author: Odys Zhou
'''
import unittest

class Solution:
    def divide(self, x: int, y: int) -> int:
        # x = ak * 2**e + ak-1 * 2**(e-1) + ...
        # x = qy + r
        # x' = qy
        # k = qt 2^t + qt-1 2^t-1, ... q0 2^0
        # x' = ( (...( qt * 2 ) + qt-1 ) * 2 ) ... ) + q1) * 2 + q0 ) * y

        sign = 1 if x > 0 and y > 0 or x < 0 and y < 0 else -1
        y = y if y > 0 else -y
        x = x if x > 0 else -x

        y_ = y
        y0 = y
        while y0 <= x:
            y = y0
            y0 <<= 1
        
        q = 0
        while x >= 0 and y >= y_:
            q <<= 1
            if x >= y:
                q += 1
                x -= y
            y >>= 1
        # if sign * q in range(-2**31, 2**31):
        q *= sign
        if q >= -2**31 and q < 2**31:
            return q
        else: return 2**31 - 1



        
if __name__ == '__main__':

    t = unittest.TestCase()
    s = Solution()
    '''
    Note:
    Assume we are dealing with an environment that could only store integers within the 32-bit signed
    integer range: [−231,  231 − 1]. For this problem, assume that your function returns 231 − 1 when
    the division result overflows.
    '''
    t.assertEqual(-2147483648, s.divide(-2147483648, 1))
    t.assertEqual(2147483647, s.divide(-2147483648, -1))
    t.assertEqual(2, s.divide(2, 1))
    t.assertEqual(-2, s.divide(-2, 1))
    t.assertEqual(1, s.divide(1, 1))
    t.assertEqual(3, s.divide(10, 3))
    t.assertEqual(2, s.divide(5, 2))
    t.assertEqual(1, s.divide(5, 3))
    t.assertEqual(-1, s.divide(5, -3))
    t.assertEqual(-2, s.divide(7, -3))
    t.assertEqual(0, s.divide(0, -3))
    t.assertEqual(0, s.divide(0, 3333))
    
    print('OK!')