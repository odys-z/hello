'''
 * 2610. Convert an Array Into a 2D Array With Conditions
 * https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description/
'''

import unittest
from collections import defaultdict
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        m = dict()
        c = defaultdict(lambda : 0)
        res = []
        for n in nums:
            ix = c[n]
            c[n] += 1
            if ix not in m:
                m.update({ix: len(res)})
                res.append([n])
            else:
                res[ix].append(n)
        return res


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()

        self.assertEqual([[1,3,4,2], [1,3], [1]], s.findMatrix([1,3,4,1,2,3,1]))


if __name__ == '__main__':
    unittest.main()
