'''
23. Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6


Created on 27 Nov 2019

@author: odys-z@github.com
'''
import unittest
from typing import List
# from heapq import heapify, heappush, heappop
from ext.heapk import Heapk

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return []

        h = Heapk(key = lambda n : n.val)
        for n0 in lists:
            if n0:
                # heappush(h, (n0.val, n0))
                h.push(n0)

        # heapify(h)
        # _, ending = heappop(h)
        ending = h.pop()
        ans = [ending]

        while h.len():
            # _, e = heappop(h)
            e = h.pop()
            if e.next:
                # heappush(h, (e.val, e.next))
                h.push(e)
            ending.next = e
            ans.append(e)
            ending = e

        return ans


class Test(unittest.TestCase):


    def testHeap(self):
        s = Solution()

        self.assertEqual([1, 1, 2, 3, 4, 4, 5, 6],
             toOutput(s.mergeKLists(buildInput([[1, 4, 5], [0, 3, 4], [2, 6]]))))

def toOutput(lst: List[ListNode]) -> List[int]:
    out = []
    for n in lst:
        out.append(n.val)
    return out

def buildInput(nums: List[List[int]]) -> List[ListNode]:
    reslt = [None for _ in nums]

    for lx, lst in enumerate(nums):
        if lst:
            for v in reversed(lst):
                prevn = ListNode(v)
                if reslt[lx]:
                    prevn.next = reslt[lx]
                reslt[lx] = prevn

    print(reslt)
    return reslt

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()