'''
942. DI String Match
https://leetcode.com/problems/di-string-match/

'''
from typing import List
from unittest.case import TestCase

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        res, h, r = [], 0, n
        for di in s:
            if di == 'D':
                res.append(r)
                r -= 1
            else:
                res.append(h)
                h += 1
        res.append((r + h) // 2)
        return res
            
            
t = TestCase()
s = Solution()

t.assertEqual([0, 4, 1, 3, 2], s.diStringMatch('IDID'));
t.assertEqual([0, 1, 2, 3], s.diStringMatch('III'));
t.assertEqual([3, 2, 0, 1], s.diStringMatch('DDI'));

print('OK')