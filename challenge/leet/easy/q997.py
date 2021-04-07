'''
997. Find the Town Judge
https://leetcode.com/problems/find-the-town-judge/submissions/
'''
from unittest import TestCase
from typing import List

class Solution:
    ''' 91.75% '''
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trusting = [0] * (N+1)
        for t, tee in trust:
            if t != tee and trusting[tee] >= 0:
                trusting[tee] += 1
            trusting[t] = -1
        
        for i in range(1, N+1):
            if trusting[i] >= N-1:
                return i
        return -1
            
 
if __name__ == '__main__':
    t = TestCase()
    s = Solution()

    t.assertEqual(-1, s.findJudge(2, [[1,2], [2, 1]]))
    t.assertEqual(1, s.findJudge(1, []))
    t.assertEqual(-1, s.findJudge(3, [[1,2]]))
    t.assertEqual(2, s.findJudge(2, [[1,2]]))
    t.assertEqual(-1, s.findJudge(3, [[1,2], [2, 3]]))
    t.assertEqual(-1, s.findJudge(3, [[1,3],[2,3],[3,1]]))
    
    print('OK!')