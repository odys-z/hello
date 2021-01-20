'''
https://leetcode.com/problems/reverse-linked-list-ii/

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

Created on 19 Jan 2021

@author: Odys Zhou
'''
from unittest import TestCase
from medium.q092_helper import assert6, assert5, assert4

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

class Solution:
    '''
    63.80%

    1 ->  2  ->  3  ->  4 ->  5

    1   m                n   5
    h1  r0      follow  h0  cut
    1 x 2   <-  3   <-  4  x 5
    1   2   <-  3   <-  4    5
    \---+---------------^    ^
        |--------------------|
    '''
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or not head.next or m >= n: # so won't changed
            return head

        head = ListNode(None, head)

        r0, h1 = head.next, head
        p = 1

        while p < m and r0:
            p += 1
            r0, h1 = r0.next, r0

        if not r0:
            return head.next

        h0, follow, cut = r0, h1, r0.next

        while p < n and h0:
            p += 1
            follow, h0 = h0, cut
            cut = h0.next if h0 else None
            h0.next = follow

        h1.next, r0.next = h0, cut

        return head.next


if __name__ == '__main__':
    s = Solution()
    assert4(s)
    assert6(s)
    assert5(s)
    print('OK!')
