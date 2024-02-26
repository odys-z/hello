'''
1828. Queries on Number of Points Inside a Circle
https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/description/
'''

import unittest
from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        sqrt2 = 1.414
        res = [0] * len(queries)
        for qx, q in enumerate(queries):
            m0 = sqrt2 * q[2]
            r2 = q[2] * q[2]
            for p in points:
                dx, dy = abs(q[0] - p[0]), abs(q[1] - p[1])
                if dx + dy <= m0 and dx * dx + dy * dy <= r2:
                    res[qx] += 1

        return res


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()

        self.assertEqual([3,2,2], s.countPoints(points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]))


if __name__ == '__main__':
    unittest.main()

'''
[82,61,74,53,13,20,28,80,2,24,19,58,45,50,83,70,43,60,28,37,26,48,84,83,18,19,19,39,38,42,87,46,9,14,53,11,54,48,40,14,18,20,5,34,68,37,51,6,20,62,72,8,64,2,8,27,77,49,77,23,26]
[82,61,74,53,13,20,28,80,2,24,19,58,45,50,83,70,43,60,28,37,26,48,84,83,18,19,19,39,38,42,87,46,9,14,53,11,54,48,40,14,18,20,5,34,68,37,51,6,20,62,73,8,64,2,8,27,77,49,77,23,26]
'''
