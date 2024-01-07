'''
496. Next Greater Element I
https://leetcode.com/problems/next-greater-element-i/description/
'''
import unittest
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {n: -1 for n in nums1}

        stack, res = [-1], []

        def push(n: int):
            if n in dic:
                dic.update({n: stack[-1]})
            stack.append(n)

        for n in reversed(nums2):
            if n < stack[-1]:
                push(n)
            else:
                while 0 <= stack[-1] < n:
                    stack.pop()
                push(n)

        for v in nums1:
            res.append(dic[v])
        return res


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()
        self.assertEqual([-1,3,-1], s.nextGreaterElement([4,1,2], [1,3,4,2]))
        self.assertEqual([2,-1], s.nextGreaterElement([1,11], [1,2,3,4,5,6,7,8,9,18,17,16,15,14,13,12,11,10]))
        self.assertEqual([3,9,4,-1,-1], s.nextGreaterElement([1,2,3,5,7], [1,3,4,2,9,7,5]))
        self.assertEqual([3,4,9,-1,9,-1,-1], s.nextGreaterElement([1,3,4,7,2,5,9], [1,3,4,2,9,7,5]))
        self.assertEqual([3,4,9,22,9,22,22,23,23,23,24,26,-1,29,32,19,-1,14,13,32],
             s.nextGreaterElement([1,3,4,7,2,5,9,20,21,22,23,24,32,26,29,18,14,13,12,11],
                                  [1,3,4,2,9,7,5,22,21,20,18,17,15,19,23,24,26,29,11,32,12,13,14]))


if __name__ == '__main__':
    unittest.main()
