'''
350. Intersection of Two Arrays II
https://leetcode.com/problems/intersection-of-two-arrays-ii/
'''
import unittest
from collections import defaultdict
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        bits = defaultdict(lambda : 0)
        for n in nums2:
            bits.update({n: bits[n] + 1})

        ans = []
        for m in nums1:
            if bits[m] > 0:
                ans.append(m)
                bits.update({m: bits[m] - 1})
        return ans


class Solution2:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = defaultdict(lambda : 0)
        for n in nums1:
            s1.update({n: s1[n] + 1})

        s2 = defaultdict(lambda : 0)
        for n in nums2:
            s2.update({n: s2[n] + 1})

        ans = []
        for m in s1:
            if m in s2:
                ans.extend([m] * min(s1[m], s2[m]))
        return ans


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution2()
        self.assertEqual([1,2], s.intersect([1,2,2,1], [1,2]))
        self.assertEqual([2,2], s.intersect([1,2,2,1], [2,2]))
        self.assertEqual([4,9], s.intersect([4,9,5], [9,4,9,8,4]))


if __name__ == '__main__':
    unittest.main()
