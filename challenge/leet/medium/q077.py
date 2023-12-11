'''
https://leetcode.com/problems/combinations/
'''
from unittest import TestCase
from typing import List

class Solution:
    def __init__(self):
        self.res = None

    def comb(self, n: int, k: int, buf: [int], start: int, depth: int):
        if k == 0:
            self.res.append(buf.copy())
            return
        if start == n:
            return

        for x in range(start, n):
            buf[depth] = x+1
            self.comb(n, k-1, buf, x+1, depth+1)

        return self.res

    def combine(self, n: int, k: int) -> List[List[int]]:
        buf = [0 for k in range(k)]
        self.res = []
        self.comb(n, k, buf, 0, 0)
        return self.res


if __name__ == "__main__":
    t = TestCase()
    s = Solution()
    t.assertEqual([[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]],
                  s.combine(4, 2))
    
    print('OK!')