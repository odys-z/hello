'''
216. Combination Sum III
https://leetcode.com/problems/combination-sum-iii/

Find all valid combinations of k numbers that sum up to n such that the following
conditions are true:

- Only numbers 1 through 9 are used.
- Each number is used at most once.

Return a list of all possible valid combinations. The list must not contain the
same combination twice, and the combinations may be returned in any order.

2 <= k <= 9
1 <= n <= 60
'''
from unittest import TestCase
from typing import List

class SolutionStep1:
    '''
    This will produce duplicated solutions
    k, n == 2, 5
    dp:
    [{()}, {(1,)}, {(2,), (1, 1)}, {(1, 2), (1, 1, 1), (3,)}, {(1, 3), (2, 2), (1, 1, 2), (1, 1, 1, 1), (4,)}, {(1, 1, 3), (1, 2, 2), (1, 4), (5,), (2, 3), (1, 1, 1, 2), (1, 1, 1, 1, 1)}]
    dp[5]:
    {(1, 1, 3), (1, 2, 2), (1, 4), (5,), (2, 3), (1, 1, 1, 2), (1, 1, 1, 1, 1)}
    '''
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # Good example for python lecture:
        # dp = [set()] * (n + 1) - all elements sharing a common Set object
        dp = [set() for _ in range(n+1)]
        dp[0].add(())
        
        def combine(k, target):
            dp[target].add((target,))

            for ni in range(1, target):
                combine(k, target - ni)

                for combo in dp[target-ni]:
                    dp[target].add(tuple(sorted(combo + (ni,))))
        
        combine(k, n)
        print(k, n)
        print(dp)
        print(dp[-1])
        return dp[-1]

class SolutionStep2():
    '''
    Time Limit Exceeded
    '''
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        dp = [set() for _ in range(n+1)]
        dp[0].add(())
        
        def combine(k, target):
            dp[target].add((target,))

            for ni in range(1, target):
                combine(k, target - ni)

                for combo in dp[target-ni]:
                    if ni not in combo:
                        dp[target].add(tuple(sorted(combo + (ni,))))
    
        combine(k, n)
        print(k, n)
        print(dp)
        print(dp[-1])

        '''
        almost but len != k 
        return list(map(lambda i: list(i) if len(i), list(dp[-1])))
        '''
        res = []
        for t in dp[-1]:
            if len(t) == k:
                res.append(list(t))
        return res

class Solution():
    '''
    5.49%
    '''
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        dp = [set() for _ in range(n+1)]
        du = [False] * (n + 1)
        dp[0].add(())
        du[0] = True
        def combine(k, target):
            dp[target].add((target,))

            for ni in range(1, min(target, 10)):
                if not du[target-ni]:
                    combine(k, target-ni)
                    du[target-ni] = True

                for combo in dp[target-ni]:
                    if ni not in combo and ni < 10:
                        dp[target].add(tuple(sorted(combo + (ni,))))
    
        combine(k, n)
#         print(k, n)
#         print(dp)
#         print(dp[-1])

        '''
        almost but len != k 
        return list(map(lambda i: list(i) if len(i), list(dp[-1])))
        '''
        res = []
        for t in dp[-1]:
            if len(t) == k and max(t) < 10:
                res.append(list(t))
        return res


if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    t.assertCountEqual([[1,4],[2,3]], s.combinationSum3(2, 5))
    t.assertCountEqual([[1,2,4]], s.combinationSum3(3, 7))
    t.assertCountEqual([[1,2,6],[1,3,5],[2,3,4]], s.combinationSum3(3, 9))
    t.assertCountEqual([], s.combinationSum3(4, 1))
    t.assertCountEqual([], s.combinationSum3(3, 2))
    t.assertCountEqual([[1,2,3,4,5,6,7,8,9]], s.combinationSum3(9, 45))
    t.assertCountEqual([[1,5,9],[1,6,8],[2,4,9],[2,5,8],[2,6,7],[3,4,8],[3,5,7],[4,5,6]],
                       #[1,3,11],[1,4,10],[1,2,12],[2,3,10] has number grater than 9
                       s.combinationSum3(3, 15))
    '''
    3
    15
    
    output
    [[1,5,9],[1,6,8],[2,4,9],[2,5,8],[2,6,7],[3,4,8],[3,5,7],[4,5,6],[1,3,11],[1,4,10],[1,2,12],[2,3,10]]

    expected
    [[1,5,9],[1,6,8],[2,4,9],[2,5,8],[2,6,7],[3,4,8],[3,5,7],[4,5,6]]
    '''
    print('OK!')
