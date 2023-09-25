'''
455. Assign Cookies
https://leetcode.com/problems/assign-cookies/


Created on 10 Dec 2021

@author: Odys Zhou
'''

from typing import List
from unittest import TestCase

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        gx, sx, chd = 0, 0, 0
        
        while gx < len(g) and sx < len(s):
            if s[sx] < g[gx]:
                sx += 1
            else:
                chd += 1
                gx += 1
                sx += 1 
        return chd
        
t = TestCase()
s = Solution()
t.assertEqual(1, s.findContentChildren([1, 2, 3], [1, 1]))
t.assertEqual(2, s.findContentChildren([1, 2], [1, 2, 3]))
t.assertEqual(0, s.findContentChildren([1, 2], []))
t.assertEqual(0, s.findContentChildren([], []))
t.assertEqual(0, s.findContentChildren([], [1]))
t.assertEqual(0, s.findContentChildren([3, 2, 5], [1, 1, 1]))
t.assertEqual(1, s.findContentChildren([3, 2, 5], [2, 2, 1]))
t.assertEqual(2, s.findContentChildren([3, 2, 5], [1, 3, 2]))

print('OK')