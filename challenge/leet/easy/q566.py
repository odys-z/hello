'''
566. Reshape the Matrix
https://leetcode.com/problems/reshape-the-matrix/description/
'''
import unittest
from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat

        return [[mat[(y * c + x) // n][(y * c + x) % n] for x in range(c)] for y in range(r)]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()
        self.assertEqual([[1,2],[3,3],[4,5]], s.matrixReshape([[1,2,3],[3,4,5]], 3, 2))
        self.assertEqual([[1,2],[3,4]], s.matrixReshape([[1,2],[3,4]], 2, 3))
        self.assertEqual([[1,2],[5,5],[7,11],[23,4],[3,4]], s.matrixReshape([[1,2,5,5,7],[11, 23, 4, 3,4]], 5, 2))


if __name__ == '__main__':
    unittest.main()
