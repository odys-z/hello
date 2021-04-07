'''
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
 
https://leetcode.com/problems/combination-sum-ii/
'''
from unittest import TestCase
from typing import List
from _collections import defaultdict
from utils.assertHelper import assertIntsEqual
from _functools import reduce
from collections import Counter

class Solution39:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def combines(curtaget, curBegin):
            dp = defaultdict(list)

            if curtaget <= 0:
                return dp

            for i in range(curBegin, len(candidates)):
                c = candidates[i]
                if c == curtaget :
                    dp[curtaget].append([c])
                elif c < curtaget:
                    dp_ = combines(curtaget - c, i)
                    if (curtaget - c) in dp_:
                        for cmb in dp_[curtaget-c]:
                            if cmb:
                                dp[curtaget].append(cmb + [c])
                else: # c > curaget & sorted
                    break
            return dp

        candidates.append(target)
        candidates.sort()
        dp = combines(target, 0)
        # print(dp)
        return dp[target][:-1]

class SolutionBad:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def plumb(numss):
            s = set()
            for nums in numss:
                nums.sort()
                nums[0] = str(nums[0])
                k = reduce(lambda x,y : x +  ',' + str(y), nums)
                s.add(k)

            s = list(s)
            for x in range(len(s)):
                s[x] = s[x].split(',')
                s[x] = list(map(lambda i: int(i), s[x]))
            print(s)
            return s
        
        def checkCount(nums):
            ncount = Counter(nums)
            for k in ncount:
                if counts[k] < ncount[k]:
                    return False
            return True

                
        def combines(candidates, curtaget):
            while len(candidates) > 0:
                if candidates[0] > curtaget:
                    break
                c = candidates.pop(0)
                if c == curtaget :
                    dp[curtaget].append([c])
                else: # if len(dp[curtaget-c]) == 0:
                    combines(candidates[:], curtaget - c)
                    for cmb in dp[curtaget-c]:
                        if checkCount(cmb + [c]):
                            dp[curtaget].append(cmb + [c])

        counts = Counter(candidates)
        dp = defaultdict(list)
        candidates.append(target)
        candidates.sort()
        combines(candidates, target)

        print(dp[target])
        return plumb(dp[target][:-1])

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        Use backtracking to keep substract the current number until target is 0.

        Sort the number and check the adjacent number to solve the duplicate issue.
        The number can be used only when it's equal to start or it's not equal to
        previous number
        '''
        
        # use dp table:
        dp = [set() for _ in range(target+1)]
        dp[0].add(())
        
        candidates.sort()
        
        for num in candidates:
            for t in range(target, num-1, -1):
                for prev in dp[t-num]:
                    dp[t].add(prev + (num,))
        
        return dp[-1]

if __name__ == "__main__":
    t = TestCase()
    s = Solution()

    assertIntsEqual([[3,5]], s.combinationSum([2,3,5], 8))
    assertIntsEqual([[3, 5]], s.combinationSum([3, 5], 8))
    assertIntsEqual([], s.combinationSum([1,1], 3))
    assertIntsEqual([], s.combinationSum([1,1,1,1,1,1,1], 8))
    assertIntsEqual([], s.combinationSum([1,1,1,1, 1,1,1,1, 1,1,1,1, 1,1,1,1, 1,1,1,1, ], 27))
    assertIntsEqual([], s.combinationSum([1,1,1,1, 1,1,1,1, 1,1,1,1, 1,1,1,1, 1,1,1,1, 1,1,1,1, 1], 27))
    assertIntsEqual([[1,1,3,4],[1,1,7], [2,3,4],[2,7]], s.combinationSum([1,1,2,3,4,7], 9))
    assertIntsEqual([[1,1,2]], s.combinationSum([1,1,2], 4))
    assertIntsEqual([[1,5,6,7,10]], s.combinationSum([1,1,2,5,6, 7,10], 29))

     
    assertIntsEqual([[7]], s.combinationSum([2,3,6,7], 7))

    assertIntsEqual([[1,2,2], [5]], s.combinationSum([2,5,2,1,2], 5))

    assertIntsEqual([[1,2,2,2], [2, 5]], s.combinationSum([2,5,2,1,2], 7))

    assertIntsEqual([], s.combinationSum([1,1,1,1, 1,1,1,1, 1,1,1,1, 1,1,1,1, 1,1,1,1, 1,1,1,1, 1], 27))
    print('OK!')
    