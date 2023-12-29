'''
q 118 Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/description/
'''
import unittest
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = [[1]]
        for r in range(1, numRows):
            c0 = len(tri[-1])
            row = [1] * (c0 + 1)
            for c in range(1, c0):
                row[c] = tri[-1][c-1] + tri[-1][c]
            tri.append(row)
        return tri;


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()
        self.assertEqual([[1]], s.generate(1))
        self.assertEqual([[1],[1,1]], s.generate(2))
        self.assertEqual([[1],[1,1],[1,2,1]], s.generate(3))


if __name__ == '__main__':
    unittest.main()
