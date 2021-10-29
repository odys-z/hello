'''
1863. Sum of All Subset XOR Totals
https://leetcode.com/problems/sum-of-all-subset-xor-totals/
'''

from unittest import TestCase
from typing import List

'''
    100%
'''
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = []
        def bt(nums):
            if len(nums) <= 1:
                res.add(nums)

            for i in range(len(nums) - 1):
                n = nums[:1] + nums[i+1:]
                res.add(n)
                bt(n)

            n = nums[:-1]
            bt(nums[:-1])


        bt(nums)
        xor = res[0]
        for n in res[1:]:
            xor ^= n

        return xor

if __name__ == '__main__':
    t = TestCase()
    s = Solution()

    t.assertEqual(5, s.subsetXORSum([1, 3]))
    t.assertEqual(28, s.subsetXORSum([5, 1, 6]))

    print('OK!')
