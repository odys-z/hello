'''
202. Happy Number
https://leetcode.com/problems/happy-number/

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.


Example 1:
Input: n = 19
Output: true
Explanation:
    12 + 92 = 82
    82 + 22 = 68
    62 + 82 = 100
    12 + 02 + 02 = 1

Example 2:
Input: n = 2
Output: false
'''

from unittest import TestCase

class Solution:
    '''
    62.61%
    '''
    def isHappy(self, n: int) -> bool:
        dp = {1: True, 10: True, 100: True, 1000: True, 10000: True, 100000: True, 1000000: True}
        def tryHappy(dp, n):
            if n in dp:
                return dp[n]
            else:
                dp.update({n: None}) # unknown
                e2sum, n0 = 0, n
                while n > 9:
                    e2sum += (n % 10) ** 2
                    n //= 10
                e2sum += n ** 2

                if e2sum in dp and dp[e2sum] == None:
                    dp[e2sum] = False
                    return False

                happy = tryHappy(dp, e2sum)
                dp.update({n0: happy})
                return happy

        tryHappy(dp, n)
        return dp[n]

if __name__ == '__main__':
    t = TestCase()
    s = Solution()

    t.assertTrue(s.isHappy(1))
    t.assertFalse(s.isHappy(2))
    t.assertFalse(s.isHappy(3))
    t.assertFalse(s.isHappy(4))
    t.assertFalse(s.isHappy(6))
    t.assertTrue(s.isHappy(7))
    t.assertFalse(s.isHappy(9))
    t.assertFalse(s.isHappy(11))
    t.assertFalse(s.isHappy(12))
    t.assertFalse(s.isHappy(17))
    t.assertTrue(s.isHappy(19))
    t.assertFalse(s.isHappy(20))
    t.assertFalse(s.isHappy(22))
    t.assertTrue(s.isHappy(299999))

    print('OK!')
