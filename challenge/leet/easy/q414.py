'''
414. Third Maximum Number
https://leetcode.com/problems/third-maximum-number/
'''
import unittest
from heapq import heappush, heappop
from typing import List


class Solution:
    """
    110ms
    """
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        def partition(k: int, l: int, r: int) -> int:
            p = nums[r]
            for i in range(l, r):
                if nums[i] > p: # 1, 4, 2, 3 -> 4, 1, 2, 3 -> 4, 1, 2, 3
                    if l < i:
                        nums[l], nums[i] = nums[i], nums[l]
                    l += 1

            nums[l], nums[r] = nums[r], nums[l]
            return l

        def kthMax(k:int, l: int, r: int) -> int:
            p = partition(k, l, r)
            if p-l == k-1:
                return nums[p]
            elif p-l < k-1: # k in (p, r)
                return kthMax(k-1-p+l, p+1, r)
            else: # k in (l, p)
                return kthMax(k, l, p-1)

        ln = len(nums)
        if ln == 1:
            return nums[0]
        elif ln == 2:
            return max(nums)
        else:
            return kthMax(3, 0, ln - 1)


class Solution2:
    """
    67ms 13%
    """
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) <= 2:
            return max(nums)
        else:
            s = set(nums)
            if len(s) == 1:
                return nums[0]
            elif len(s) <= 2:
                return max(s)
            nums = sorted(s)
            return nums[-3]


class Solution3:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        hq = []
        for n in nums:
            heappush(hq, -n)

        s = set()
        while len(s) < 3 and len(hq) > 0:
            h = heappop(hq)
            s.add(h)

        return -h if len(s) == 3 else - min(s)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution3()
        self.assertEqual(1, s.thirdMax([1]))
        self.assertEqual(1, s.thirdMax([1, 0]))
        self.assertEqual(1, s.thirdMax([1, 2, 3]))
        self.assertEqual(1, s.thirdMax([1, 2, 2, 3]))
        self.assertEqual(1, s.thirdMax([1, 1, 1]))


if __name__ == '__main__':
    unittest.main()

