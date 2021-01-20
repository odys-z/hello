from unittest import TestCase

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def assert6(s):
    t = TestCase()

    h = ListNode(6)
    h = ListNode(5, h)
    h = ListNode(4, h)
    h = ListNode(3, h)
    h = ListNode(2, h)
    h = ListNode(1, h)
    h = s.reverseBetween(h, 2, 5)

    t.assertEqual(1, h.val)
    h = h.next
    t.assertEqual(5, h.val)
    h = h.next
    t.assertEqual(4, h.val)
    h = h.next
    t.assertEqual(3, h.val)
    h = h.next
    t.assertEqual(2, h.val)
    h = h.next
    t.assertEqual(6, h.val)

def assert5(s):
    t = TestCase()

    h = ListNode(5)
    h = ListNode(4, h)
    h = ListNode(3, h)
    h = ListNode(2, h)
    h = ListNode(1, h)
    h = s.reverseBetween(h, 2, 5)

    t.assertEqual(1, h.val)
    h = h.next
    t.assertEqual(5, h.val)
    h = h.next
    t.assertEqual(4, h.val)
    h = h.next
    t.assertEqual(3, h.val)
    h = h.next
    t.assertEqual(2, h.val)


def assert4(s):
    t = TestCase()

    h = ListNode(4)
    h = ListNode(3, h)
    h = ListNode(2, h)
    h = ListNode(1, h)
    h = s.reverseBetween(h, 1, 4)

    t.assertEqual(4, h.val)
    h = h.next
    t.assertEqual(3, h.val)
    h = h.next
    t.assertEqual(2, h.val)
    h = h.next
    t.assertEqual(1, h.val)
