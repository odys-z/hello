'''
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted linked lists and return it as a sorted list.
The list should be made by splicing together the nodes of the first two lists.
'''
from unittest import TestCase

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    '''
    49.93%
    '''
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        a, b, h = l1, l2, ListNode(None)
        h0 = h

        while a and b:
            least = b
            if a.val <= b.val:
                least = a
                a = a.next
            else:
                b = b.next

            h.next = ListNode(least.val)
            h = h.next

        h.next = a if a else b
        return h0.next


if __name__ == '__main__':
    t = TestCase()
    s = Solution()

    # 1 -> 2
    # 2 -> 3
    a = ListNode(2)
    a = ListNode(1, a)
    b = ListNode(3)
    b = ListNode(2, b)
    l = s.mergeTwoLists(a, b)
    t.assertEqual(1, l.val)
    t.assertEqual(2, l.next.val)
    t.assertEqual(2, l.next.next.val)
    t.assertEqual(3, l.next.next.next.val)

    print('OK!')
