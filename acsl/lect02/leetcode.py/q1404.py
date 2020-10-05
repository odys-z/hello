import unittest

'''
    LeetCode 1404
    =============

    Question:
    ---------

    Number of Steps to Reduce a Number in Binary Representation to One

    https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

    Runtime: 32 ms, faster than 68.68% of Python3 online submissions.
    Memory Usage: 14.2 MB, less than 5.52% of Python3 online submissions.
'''
class Solution:
    def numSteps(self, s: str) -> int:
        c = 0
        v = int(s, base=2)
        while v != 1:
            if (v & 1) == 1:
                v += 1
            else:
                v = v >> 1
            c += 1
        return c


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        self.assertEqual(0, s.numSteps('1'))

t = Test()
t.test1()
