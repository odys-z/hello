'''
2125. Number of Laser Beams in a Bank
https://leetcode.com/problems/number-of-laser-beams-in-a-bank
'''
import unittest
from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        lo, res = 0, 0

        for r in list(map(lambda c: c.count('1'), bank)):
            if r > 0:
                res += lo * r
                lo = r

        return res


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()

        self.assertEqual(8, s.numberOfBeams(["011001","000000","010100","001000"]))
        self.assertEqual(0, s.numberOfBeams(["000000","010100","000000"]))


if __name__ == '__main__':
    unittest.main()
