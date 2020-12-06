'''
    https://leetcode.com/problems/power-of-two/submissions/

	Given an integer n, return true if it is a power of two. Otherwise, return false.
	An integer n is a power of two, if there exists an integer x such that n == 2x.
'''
import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        for i in range(32):
            if n & 1:
                n >>= 1
                if n > 0:
                    return False
                else:
                    return True
            else:
                n >>= 1

class Solution2:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        a = [[0x0000FFFF, 0xFFFF0000],
             [0xFF00FF00, 0x00FF00FF],
             [0xF0F0F0F0, 0X0F0F0F0F],
             [0xcccccccc, 0x33333333],
             [0xaaaaaaaa, 0x55555555]]

        for i in range(len(a)):
            x = 1 if a[i][0] & n > 0 else 0
            x += 1 if a[i][1] & n > 0 else 0
            if x > 1:
               return False
        return True

class Solution3:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return n == 2 ** int(math.log(n, 2))
