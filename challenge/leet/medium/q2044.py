'''
https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/
'''
from unittest import TestCase
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        counter = dict({0: 1})
        maxor = 0
        for n in nums:
            shadow = counter.copy()
            for p in counter:
                k = p | n
                if k not in shadow:
                    shadow[k] = 0
                shadow[k] += counter[p]
                maxor = max(k, maxor)
            counter = shadow
        return counter[maxor]


if __name__ == "__main__":
    t = TestCase()
    s = Solution()
    t.assertEqual(6, s.countMaxOrSubsets([3, 5, 1, 2]))
    
    print('OK!')