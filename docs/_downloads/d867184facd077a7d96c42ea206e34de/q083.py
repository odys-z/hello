'''
83. Remove Duplicates from Sorted List
https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Given the head of a sorted linked list, delete all duplicates such that
each element appears only once. Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]
'''

from unittest import TestCase

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        v = None
        h = ListNode(v, head)
        while h and h.next:
            if v == h.next.val:
                h.next = h.next.next
            else:
                h = h.next 
                v = h.val
        return head
        
if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    
    h = ListNode(2)
    h = ListNode(1, h)
    h = ListNode(1, h)
    h = s.deleteDuplicates(h)
    t.assertEqual(1, h.val)
    t.assertEqual(2, h.next.val)
    
    h = ListNode(3)
    h = ListNode(3, h)
    h = ListNode(2, h)
    h = ListNode(1, h)
    h = ListNode(1, h)
    h = s.deleteDuplicates(h)
    t.assertEqual(1, h.val)
    t.assertEqual(2, h.next.val)
    t.assertEqual(3, h.next.next.val)
    
    print('OK!')