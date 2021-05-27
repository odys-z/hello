'''
204. Count Primes
https://leetcode.com/problems/count-primes/

Count the number of prime numbers less than a non-negative number, n.
'''

from unittest import TestCase

class Solution:
    '''
         11.01%
    '''
    def countPrimes(self, n: int) -> int:
        if n <= 1: return 0

        prims = [1] * n   # 1, 2, ... n
        prims[0] = 0      # 1 is neither prime nor composite 

        for i in range(2, n+1):
            for j in range(2, i + 1):
                if i * j - 1 >= n:
                    break
                prims[i * j - 1] = 0
        prims[-1] = 0     # not n
        return sum(prims)

if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    
    t.assertEqual(4, s.countPrimes(10))
    t.assertEqual(0, s.countPrimes(1))
    t.assertEqual(0, s.countPrimes(0))
    t.assertEqual(2, s.countPrimes(5))
    t.assertEqual(8, s.countPrimes(20))
    t.assertEqual(8, s.countPrimes(21))
    t.assertEqual(8, s.countPrimes(23))
    t.assertEqual(9, s.countPrimes(24))
    t.assertEqual(1499, s.countPrimes(12548))
    
    print('OK!')