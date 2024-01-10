import unittest
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()

        pre, cur, cnt, precnt, maxcnt = nums[0], nums[0], 0, 0, 0
        for nxt in nums:
            if cur != nxt:
                if pre + 1 == cur:
                    maxcnt = max(maxcnt, precnt + cnt)
                pre, precnt, cur, cnt = cur, cnt, nxt, 0

            cnt += 1
        return maxcnt if cur != pre + 1 else max(maxcnt, precnt + cnt)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()
        self.assertEqual(5, s.findLHS([1,3,2,2,5,2,3,7]))
        self.assertEqual(0, s.findLHS([1,1,1,1]))
        self.assertEqual(5, s.findLHS([1,1,1,1,2]))
        self.assertEqual(5, s.findLHS([3,3,2,1,1,1,1]))
        self.assertEqual(6, s.findLHS([3,3,2,1,1,1,1,2]))
        self.assertEqual(0, s.findLHS([-1,-3,-5,-7,-9,-11,-13,-15,-17,-19,-21,-23]))


if __name__ == '__main__':
    unittest.main()
