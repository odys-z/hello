'''
1282. Group the People Given the Group Size They Belong To
https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description/
'''
import unittest
from collections import defaultdict
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = defaultdict(lambda : [[]])
        for i, s in enumerate(groupSizes):
            if len(d[s][0]) == s:
                d[s].insert(0, [])
            d[s][0].append(i)

        res = []
        for v in d.values():
            res.extend(v)
        return res


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()

        self.assertEqual([[3,4,6],[0,1,2],[5]], s.groupThePeople([3,3,3,3,3,1,3]))


if __name__ == '__main__':
    unittest.main()

