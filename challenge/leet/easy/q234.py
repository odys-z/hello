'''
234. Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

'''
from unittest.case import TestCase

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        # f2(none) -> f1(none) -> f0(fake) -> fast(head)
        f0 = ListNode(0, head)
        f2, f1 = None, None
        fast, slow = f0, f0
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            f2, f1, f0 = f1, f0, fast

            if f0:
                f0.next = f1
            if f1:
                f1.next = f2
        
        if not fast:
            fast = f0
        
        while head != slow:
            if fast.val != head.val:
                return False 
            fast, head = fast.next, head.next 
        
        return True

         
if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    
    h = ListNode(4)
    h = ListNode(3, h)
    h = ListNode(4, h)
    t.assertCountEqual(True, s.isPalindrome(h))