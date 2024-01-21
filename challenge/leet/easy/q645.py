import unittest
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup, sum, n = -1, 0, len(nums)
        for v in nums:
            v = abs(v)
            if nums[v-1] > 0:
                nums[v-1] *= -1
                sum += v
            else:
                dup = v

        return [dup, n * (n+1) // 2 - sum]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()
        self.assertEqual([3,1], s.findErrorNums([3,2,3,4,6,5]))
        self.assertEqual([2,3], s.findErrorNums([1,2,2,4]))


if __name__ == '__main__':
    unittest.main()
