'''
141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/

'''
from unittest import TestCase

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, nxt = None):
        self.val = x
        self.next = nxt

def assert1(s):
    t = TestCase()

    r = ListNode(-4)
    h = ListNode(0, r)
    h = ListNode(2, h)
    r.next = h
    h = ListNode(3, h)

    t.assertTrue(s.hasCycle(h))

def assert2(s):
    t = TestCase()

    r = ListNode(2)
    h = ListNode(1, r)
    r.next = h

    t.assertTrue(s.hasCycle(h))


class Solution:
    ''' 32.37%
    '''
    def hasCycle(self, head: ListNode) -> bool:
        tortois, hare = head, head
        while tortois and hare:
            tortois = tortois.next
            if not tortois or not hare.next or not hare.next.next:
                return False
            hare = hare.next.next
            if tortois == hare:
                return True
        return False

if __name__ == "__main__":
	s = Solution()
	assert1(s)
	assert2(s)

	print("OK!")
