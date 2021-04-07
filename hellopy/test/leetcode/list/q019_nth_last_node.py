'''
19. Remove Nth Node From End of List
Medium

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

'''

from typing import List
import unittest

from utils import Assrt
from utils.Singlist import ListNode
from utils.Singlist import Eq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next = None):
#         self.val = val
#         self.next = nxt

'''
Runtime: 32 ms, faster than 65.47% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 13.8 MB, less than 6.06% of Python3 online submissions for Remove Nth Node From End of List.
'''
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # n = n_ - 1
        if head is None or head.next is None and n > 1:
            return head

        monkey = head
        monkeyStep = 0
        
        # monkey go ahead of n step
        while monkey and monkeyStep < n:
            monkey = monkey.next
            monkeyStep += 1
        if monkey is None and monkeyStep < n:
            return head

        master = head
        chaperone = None
        while monkey: 
            monkey = monkey.next
            chaperone = master
            master = master.next

        # has chaperone means head must kept, remove last n-th
        if chaperone:
            chaperone.next = master.next
            return head
        # no follower
        elif master:
            # master == head (moved master but not chaperone)
            return head.next
        else:
            # master == monkey (step = 0)
            head.next = None
            return head
        
eq = Assrt.Eq()
class Test(unittest.TestCase):

    def testName(self):
        Eq.assertStrArr(['a'], ListNode('a'))
        c = ListNode('c')
        b = ListNode('b', c)
        a = ListNode('a', b)
        Eq.assertStrArr(['a', 'b', 'c'], a)

        s = Solution()
        Eq.assertStrArr([], s.removeNthFromEnd(None, 1))
        Eq.assertStrArr(None, s.removeNthFromEnd(None, 1))
        Eq.assertStrArr(['a', 'b', 'c'], a)
        Eq.assertStrArr(['a', 'c'], s.removeNthFromEnd(a, 2))
        Eq.assertStrArr(['a'], s.removeNthFromEnd(a, 1))

        a = ListNode('z', a)
        a = ListNode('x', a)
        Eq.assertStrArr(['x', 'a'], s.removeNthFromEnd(a, 2))

        a = ListNode('0', a)
        a = ListNode('1', a)
        a = ListNode('2', a)
        Eq.assertStrArr(['2', '1', 'x', 'a'], s.removeNthFromEnd(a, 3))

        a = ListNode('3', a)
        a = ListNode('', a)
        Eq.assertStrArr(['', '3', '2', '1', 'x', 'a'], a)
        a = s.removeNthFromEnd(a, 7)
        Eq.assertStrArr(['', '3', '2', '1', 'x', 'a'], a)

        a = s.removeNthFromEnd(a, 6)
        Eq.assertStrArr(['3', '2', '1', 'x', 'a'], a)
        a = s.removeNthFromEnd(a, 5)
        Eq.assertStrArr(['2', '1', 'x', 'a'], a)
        Eq.assertStrArr(['2', '1', 'x'], s.removeNthFromEnd(a, 1))

