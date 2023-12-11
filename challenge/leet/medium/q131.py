'''
https://leetcode.com/problems/palindrome-partitioning/solutions/3085104/most-optimized-python-solution/
'''
from typing import List
from unittest import TestCase


class Solution:
    def __init__(self):
        self.lst = None

    def dp(self, i, s, st):
        if i >= len(s):
            self.lst.append(tuple(st))
            return
        for j in range(i, len(s)):
            if s[i:j+1] == ''.join(reversed(s[i:j+1])):
                st.append(s[i:j+1])
                self.dp(j+1, s, st)
                st.pop()
        return

    def partition(self, s: str) -> List[List[str]]:
        self.lst = []
        self.dp(0, s, [])
        return self.lst


if __name__ == '__main__':
    s = Solution()
    t = TestCase()
    s = Solution()
    t.assertEqual([('a', 'a', 'b'), ('aa', 'b')], s.partition("aab"))
    t.assertEqual([('e',)], s.partition("e"))

    print('OK')
