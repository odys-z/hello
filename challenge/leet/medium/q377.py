'''
377. Combination Sum IV
https://leetcode.com/problems/combination-sum-iv/

Given an integer array with all positive numbers and no duplicates,
find the number of possible combinations that add up to a positive
integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
'''
from unittest import TestCase
from typing import List

class SolutionDebug:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def sumto(T):
            # dp[T].append([T])
            
            for n in nums:
                if T < n:
                    break
                if not du[T - n]:
                    sumto(T - n)
                    du[T - n] = True
                for combo in dp[T - n]:
                    dp[T].append(combo + [n])

        dp = [list() for _ in range(target + 1)]
        dp[0].append([])
        du = [False] * (target + 1)
        du[0] = True
        nums.sort()
        
        sumto(target)
        # print(dp[-1])
        return len(dp[-1])
        
class Solution:
    '''
    87.69%
    '''
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def sumto(T):
            for n in nums:
                if T < n:
                    break
                if not du[T - n]:
                    sumto(T - n)
                    du[T - n] = True
                dp[T] += dp[T - n]

        dp = [0] * (target + 1)
        dp[0] = 1
        du = [False] * (target + 1)
        du[0] = True
        nums.sort()
        
        sumto(target)
        # print(dp)
        return dp[-1]
        
if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    t.assertEqual(7, s.combinationSum4([1, 2, 3], 4))
    t.assertEqual(31, s.combinationSum4([4,2,1], 7))
    t.assertEqual(700647, s.combinationSum4([1,5,7,14,3,11], 30))
    t.assertEqual(12950466, s.combinationSum4([4,2,1], 30))
    t.assertEqual(39882198, s.combinationSum4([4,2,1], 32))
    
    print('OK!')
