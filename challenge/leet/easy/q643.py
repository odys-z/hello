import unittest
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        mx, sm = -float('inf'), sum(nums[0:k])

        for x, n in enumerate(nums[k:]):
            mx = max(mx, sm)
            sm += n - nums[x]

        mx = max(mx, sm)
        return mx / k


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()

        self.assertEqual(12.75, s.findMaxAverage([1,12,-5,-6,50,3], 4))
        self.assertEqual(-1, s.findMaxAverage([-1], 1))


if __name__ == '__main__':
    unittest.main()
