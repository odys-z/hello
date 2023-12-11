'''
2375. Construct Smallest Number From DI String
https://leetcode.com/problems/construct-smallest-number-from-di-string/description/
'''
from unittest import TestCase
from typing import List


class Solution:
    def smallestNumberWrong(self, pattern: str) -> str:
        low, up, cur = 1, 0, 0
        v = [cur]
        for n in pattern:
            if n == 'I':
                cur = up + 1
                up = max(up, cur)
            elif n == 'D':
                cur = low - 1
                low = min(low, cur)
            v.append(cur)
        res = ''
        for n in v:
            res += str(n - low + 1)
        return res

    def smallestNumber(self, pattern: str) -> str:
        cur = 0
        qv, digits = [999, 1], [i for i in range(2, 10)]
        stk = []

        for c in pattern:
            d = digits.pop(0)
            if c == 'I':
                while len(stk) > 0:
                    qv.append(stk.pop())
                qv.append(d)
            else:   # D
                c = qv.pop()
                stk.append(c)
                qv.append(d)

        while len(stk) > 0:
            qv.append(stk.pop())

        s = ''
        for i in qv[1:]:
            s += str(i)
        return s


if __name__ == "__main__":
    t = TestCase()
    s = Solution()
    t.assertEqual('123549876',  # '0 1 2 3 -1 4 -2 -3 -4', min, max, delta = -4, 4, 5,
                  s.smallestNumber('IIIDIDDD'))
    
    print('OK!')