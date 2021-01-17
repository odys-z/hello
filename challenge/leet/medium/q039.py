from unittest import TestCase
from typing import List
from _collections import defaultdict
from utils.assertHelper import assertIntsEqual

class Solution2:
    '''
    1 <= candidates[i] <= 200
    '''
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target+1)]
        for c in candidates:                 # O(N): for each candidate
            for i in range(c, target+1):     # O(M): for each possible value <= target
                if i == c:
                    dp[i].append([c])
                for comb in dp[i-c]:         # O(M)
                    dp[i].append(comb + [c])
        return dp[-1]

class Solution:
    '''
    DP + backtrack, 99.02%
    '''
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

if __name__ == "__main__":
    t = TestCase()
    s = Solution()
    assertIntsEqual([[3, 5]], s.combinationSum([3, 5], 8))

    assertIntsEqual([[2,2,2,2],[2,3,3],[3,5]],
                       s.combinationSum([2,3,5], 8))
    
    assertIntsEqual([[2,2,3],[7]],
                       s.combinationSum([2,3,6,7], 7))
    print('OK!')