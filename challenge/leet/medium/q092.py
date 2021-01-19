'''
https://leetcode.com/problems/reverse-linked-list-ii/

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

Created on Jan 19, 2021

@author: ody
'''
from unittest import TestCase

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        p, h, h0 = 1, head, ListNode(-float('inf'))
        h0.next, r = head, h0

        while p < m and h:
            p += 1
            h, r = h.next, h
        
        if not h: return h0.next

        prev, cutoff = None, None
        # h = ListNode(h.val)
        while p < n and h:
            p += 1
            cutoff = h.next 
            prev, h, h.next = h, h.next, prev
        
        if not h and prev:
            # back step in case n > len
            h = prev
        
        if cutoff:
            r.next.next = cutoff
            
        if h:
            r.next, r.next.next = h, h.next
        
        return h0.next
            
 
if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    r = ListNode(5)
    h = ListNode(4, r)
    h = ListNode(3, h)
    h = ListNode(2, h)
    h = ListNode(1, h)
    
    h = s.reverseBetween(h, 2, 4)
    t.assertEqual(1, h.val)
    h = h.next
    t.assertEqual(4, h.val)
    h = h.next
    t.assertEqual(3, h.val)
    h = h.next
    t.assertEqual(2, h.val)
    h = h.next
    t.assertEqual(5, h.val)
    
    print('OK!')
