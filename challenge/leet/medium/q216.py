'''
216. Combination Sum III
https://leetcode.com/problems/combination-sum-iii/

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

2 <= k <= 9
1 <= n <= 60
'''
from unittest import TestCase
from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        dp = [set()] * (n + 1)
        
        def combine(k, target):
            for i in range((target+1)//2): 
                for j in range(0, i):
                    combine(k, j)
                    if n - j in dp[1]
                        pass # to be continued

if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    t.assertCountEqual([1,2,4], s.combinationSum3(3, 7))