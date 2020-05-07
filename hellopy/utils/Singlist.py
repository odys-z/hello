from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, nxt = None):
        self.val = val
        self.next = nxt

class Eq(object):
    @staticmethod
    def assertStrArr(a: List[str], b : ListNode):
        if a is None and b is None:
            return
        if a is not None and len(a) != 0 and b is None or a is None and b is not None:
            raise AssertionError('a != b')
            
        p, ax = b, 0
        while p:
            if a[ax] != p.val:
                raise AssertionError('a[{0}] {1} != b.val {2}'.format(ax, a[ax], b.val))
            ax += 1
            p = p.next
            if ax >= len(a) and p:
                raise AssertionError('a.len < b.len')

        if ax != len(a):
            raise AssertionError('a.len > b.len')
        