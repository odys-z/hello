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
    ''' I like this but slow: 92 ms '''
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None

        h = Heapk(key = lambda n : n.val)
        for n0 in lists:
            if n0:
                h.push(n0)
        if h.len() == 0:
            return None

        ending = h.pop()
        if ending.next:
            h.push(ending.next)
        first = ending

        while h.len():
            e = h.pop()
            if e.next:
                h.push(e.next)
            ending.next = e
            ending = e

        return first

class Solupy:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        srtlist = []
        for n in lists:
            while n:
                srtlist.append(n)
                n = n.next
        
        allist = sorted(srtlist, key = lambda n : n.val)
        
        if not allist:
            return None

        # brutal 84 ms
        first = allist[0]
        prev = first
        for nx in allist[1:]:
            prev.next = nx
            prev = nx
        
        # another way is reduce - but slower, 88 ms:
        # reduce(linkup, allist)

        return first

def linkup(p, n):
    p.next = n
    return n

class Test(unittest.TestCase):


    def testHeap(self):
        s = Solution()

        self.assertEqual([],
             toOutput(s.mergeKLists(buildInput([[], []]))))

        self.assertEqual([1, 1, 2, 3, 4, 4, 5, 6],
             toOutput(s.mergeKLists(buildInput([[1, 4, 5], [1, 3, 4], [2, 6]]))))
        
    def testPylist(self):
        s = Solupy()
        self.assertEqual([],
             toOutput(s.mergeKLists(buildInput([[], []]))))

        self.assertEqual([],
             toOutput(s.mergeKLists(buildInput([[]]))))

        self.assertEqual([1, 1, 2, 3, 4, 4, 5, 6],
             toOutput(s.mergeKLists(buildInput([[1, 4, 5], [1, 3, 4], [2, 6]]))))

def toOutput(lst: List[ListNode]) -> List[int]:
    out = []
    n = lst
    while n:
        out.append(n.val)
        n = n.next
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

    for res in reslt:
        while res:
            print(res.val, end = ', ')
            res = res.next
        print('')

    return reslt

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()