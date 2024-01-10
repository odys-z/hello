'''
 * 575. Distribute Candies
 * https://leetcode.com/problems/distribute-candies/description/
'''
import unittest
from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        p = 0
        n = 0
        for t in candyType:
            if t >= 0:
                p |= 1 << t
            else:
                n |= 1 << -t
        # python 3.10
        return min(p.bit_count() + n.bit_count(), len(candyType)//2)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()
        self.assertEqual(3, s.distributeCandies([1,1,2,2,3,3]))
        self.assertEqual(1, s.distributeCandies([6,6,6,6]))
        self.assertEqual(7, s.distributeCandies([ 1, -2, 3, -4, -5, -6, -7, -8, -9, -10, 100000, 0, -100000, 99999]))


if __name__ == '__main__':
    unittest.main()

