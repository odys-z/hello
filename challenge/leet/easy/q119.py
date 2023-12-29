'''
q 119 Pascal's Triangle II
https://leetcode.com/problems/pascals-triangle-ii/description/
'''
import unittest
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def genrow(rx: int):
            if rx == 0:
                return [1]
            elif rx == 1:
                return [1, 1]
            else:
                row0 = genrow(rx - 1)
                for cx, v in enumerate(row0[:-1]):
                    row0[cx + 1] += v
                row0.append(1)
                return row0

        return genrow(rowIndex)


class Solution2:
    def getRow(self, rx: int) -> List[int]:
        if rx == 0:
            return [1]
        elif rx == 1:
            return [1, 1]
        else:
            row0 = [1, 1]
            for cx in range(1, rx): # 2, ...
                row0 = [1 if jx == 0 else row0[jx - 1] + row0[jx] for jx in range(len(row0))]
                row0.append(1)
            return row0


class Solution3:

    def getRow(self, rx: int) -> List[int]:
        ans = 1
        res = [ans]
        for r in range(rx // 2):
            ans *= (rx - r) / (r + 1)
            res.append(round(ans))

        res = res + list(reversed(res[0:-1] if rx % 2 == 0 else res))
        # print(res)
        return res

class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution3()
        # s.getRow(9)
        # s.getRow(1)
        # s.getRow(2)
        # s.getRow(3)
        # s.getRow(4)
        # s.getRow(5)
        # s.getRow(11)
        self.assertEqual([1], s.getRow(0))
        self.assertEqual([1,1], s.getRow(1))
        self.assertEqual([1,2,1], s.getRow(2))
        self.assertEqual([1,3,3,1], s.getRow(3))
        self.assertEqual([1,9,36,84,126,126,84,36,9,1], s.getRow(9))
        self.assertEqual([1,11,55,165,330,462,462,330,165,55,11,1], s.getRow(11))


if __name__ == '__main__':
    unittest.main()
