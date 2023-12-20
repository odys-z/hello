'''
2261. K Divisible Elements Subarrays
https://leetcode.com/problems/k-divisible-elements-subarrays/description/
'''
import unittest
from typing import List


class Solution:
    def printv(self, nums, s, e):
        for v in range(s, e+1):
            print(nums[v], end=",")
        print("")
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:

        n = len(nums)
        p0 = 1 if nums[0]%p == 0 else 0
        countp, exp = [p0] * n, [1] * n
        for i in range(1, n):
            countp[i] = countp[i-1] + (1 if nums[i] % p == 0 else 0)
            exp[i] = exp[i-1] * 200

        k0, dedup = 0, set()
        for s in range(n):
            hash = 0
            for e in range(s, n):
                if countp[e] - k0 > k: break
                hash += nums[e] * 200 ** (e - s)
                # self.printv(nums, s, e)
                dedup.add(hash)
            k0 = countp[s]
        return len(dedup)


class MyTestCase(unittest.TestCase):
    def test_2261(self):
        s = Solution()
        self.assertEqual(20, s.countDistinct([2, 3, 3, 4, 4, 5, 6, 7], 1, 3))
        self.assertEqual(3, s.countDistinct([3, 3, 4], 1, 3))
        self.assertEqual(11, s.countDistinct([2, 3, 3, 2, 2], 2, 2))
        self.assertEqual(10, s.countDistinct([1, 2, 3, 4], 4, 1))


if __name__ == '__main__':
    unittest.main()
