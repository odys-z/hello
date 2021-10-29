'''
1863. Sum of All Subset XOR Totals
https://leetcode.com/problems/sum-of-all-subset-xor-totals/
'''

from unittest import TestCase
from typing import List
from itertools import combinations

'''
    A good answer: https://leetcode.com/problems/sum-of-all-subset-xor-totals/discuss/1242073/Java-Backtracking-approach-with-explanation
    All subsets combinations are actually all possibles of each element presented or not.

    ... 3 , 0 , 1
       [3]                -> 1
               [1]        -> 3
       [3       1]        -> 2 (0101 -> ...10)
    
    ... 6 5 0 0 0 1
         [5]               -> 5 (...10000 -> 101 = 101 )
                 [1]       -> 1 (...00001 -> 001 = 1 )
         [5       1]       -> 4 (...10001 -> 100 = 101 ^ 1)
       [6         1]       -> 7 (..100001 -> 111 = 110 ^ 1)
'''
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = []
        def comb(nums):
            for x in range(len(nums)):
                res.extend(map(lambda tup: list(tup), combinations(nums, x+1)))
        
        def xor(nums):
            s = nums[0]
            for n in nums[1:]:
                s ^= n
            return s

        comb(nums)
        s = 0
        for n in res:
            s += xor(n)

        return s

if __name__ == '__main__':
    t = TestCase()
    s = Solution()

    t.assertEqual( 28, s.subsetXORSum([5, 1, 6]))
    t.assertEqual(  6, s.subsetXORSum([1, 3]))
    t.assertEqual(480, s.subsetXORSum([3,4,5,6,7,8]))

    print('OK!')
