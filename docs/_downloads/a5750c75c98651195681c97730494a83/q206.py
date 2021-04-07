'''
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/

Reverse a singly linked list.
'''
from unittest import TestCase

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head and head.next:
            h2 = ListNode(head.val)
            head = head.next
            while head is not None:
                h2, h2.next, head = head, h2, head.next
            return h2
        return head

if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    r = ListNode(1)
    h = ListNode(2, r)
    h = ListNode(3, h)
    h = s.reverseList(h)
    t.assertEqual(1, h.val)
    r = h.next
    t.assertEqual(2, r.val)
    r = r.next
    t.assertEqual(3, r.val)

    print('OK!')

'''
    r         h -> none
    1    2    3

    p->none  h -> next
    3        2    1

    next <-  p        h
    3        2        1
'''
