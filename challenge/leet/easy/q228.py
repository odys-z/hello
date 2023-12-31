'''
228. Summary Ranges
https://leetcode.com/problems/summary-ranges/description/
'''

import unittest
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l, u = [nums[0], nums[0]]
        ranges = []

        for n in nums[1:]:
            if n == u + 1:
                u = n
            else:
                ranges.append(f"{l}" if l == u else f"{l}->{u}")
                l, u = [n, n]
        ranges.append(f"{l}" if l == u else f"{l}->{u}")
        return ranges


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()
        self.assertEqual(["-2147483649"], s.summaryRanges([-2147483649]))
        self.assertEqual(["->-1"], s.summaryRanges([-1]))
        self.assertEqual(["-2->0"], s.summaryRanges([-2,-1,0]))
        self.assertEqual(["1->2"], s.summaryRanges([1,2]))
        self.assertEqual(["1->2","4->5"], s.summaryRanges([1,2,4,5]))
        self.assertEqual(["1->2","4->5"], s.summaryRanges([1,2,4,5]))


if __name__ == '__main__':
    unittest.main()
