'''
https://leetcode.com/problems/swap-nodes-in-pairs/
24. Swap Nodes in Pairs
Medium

Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.

@author: odys-z@github.com
'''
import unittest
from utils.Singlist import ListNode, Eq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
Runtime: 32 ms, faster than 52.65% of Python3 online submissions for Swap Nodes in Pairs.
Memory Usage: 13.8 MB, less than 6.06% of Python3 online submissions for Swap Nodes in Pairs.
'''
class Solution:
    def swapPairs(self, h: ListNode) -> ListNode:
        if not h or not h.next:
            return h
        
        hh = None
        h0, h1 = h, h.next
        hx = h1
        while h0 and h1:
            h0.next = h1.next
            h1.next = h0
            if hh:
                hh.next = h1

            hh = h0
            h0 = h0.next if h0 else None
            h1 = h0.next if h0 else None
        return hx
        

class Test(unittest.TestCase):

    def testName(self):
        s = Solution()
        
        a = None
        Eq.assertStrArr([], s.swapPairs(a));

        b = ListNode('b')
        a = ListNode('a', b)
        Eq.assertStrArr(['b', 'a'], s.swapPairs(a));

        c = ListNode('c')
        b = ListNode('b', c)
        a = ListNode('a', b)
        Eq.assertStrArr(['b', 'a', 'c'], s.swapPairs(a));

        c = ListNode('c')
        Eq.assertStrArr(['c'], s.swapPairs(c));
        
        d = ListNode('d')
        c = ListNode('c', d)
        b = ListNode('b', c)
        a = ListNode('a', b)
        Eq.assertStrArr(['b', 'a', 'd', 'c'], s.swapPairs(a));

