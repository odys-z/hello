'''
 * 2. Add Two Numbers
 * https://leetcode.com/problems/add-two-numbers/
 * 
 * You are given two non-empty linked lists representing two non-negative integers.
 * The digits are stored in reverse order and each of their nodes contain a single
 * digit. Add the two numbers and return it as a linked list.
 * You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 * Example:
 * Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 * Output: 7 -> 0 -> 8
 * Explanation: 342 + 465 = 807.
 
Created on 4 Dec 2019

@author: ody
'''
import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
Runtime: 64 ms, faster than 94.71% of Python3 online submissions for Add Two Numbers.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Add Two Numbers.
'''
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        h1 = l1
        c = 0
        r1 = None
        while l1 and l2:
            l1.val += l2.val + c;
            c = l1.val // 10
            l1.val %= 10
            
            r1 = l1
            l1, l2 = l1.next, l2.next
        
        if not l1 and r1:
            r1.next = l2
            l1 = l2
        
        while l1 and c > 0:
            l1.val += c;
            c = l1.val // 10
            l1.val %= 10
            r1 = l1
            l1 = l1.next
        
        if c > 0:
            r1.next = ListNode(c)
            
        return h1
            

class Test(unittest.TestCase):


    def test002(self):
        s = Solution()
        self.assertListNodes(toList(""), s.addTwoNumbers(toList(""), toList("")))
        self.assertListNodes(toList("1"), s.addTwoNumbers(toList("1"), toList("")))
        self.assertListNodes(toList("0"), s.addTwoNumbers(toList("0"), toList("0")))
        self.assertListNodes(toList("1"), s.addTwoNumbers(toList("0"), toList("1")))
        self.assertListNodes(toList("2"), s.addTwoNumbers(toList("1"), toList("1")))
        self.assertListNodes(toList("9"), s.addTwoNumbers(toList("0"), toList("9")))
        self.assertListNodes(toList("10"), s.addTwoNumbers(toList("9"), toList("1")))
        self.assertListNodes(toList("20"), s.addTwoNumbers(toList("19"), toList("1")))
        self.assertListNodes(toList("20000"), s.addTwoNumbers(toList("19999"), toList("1")))
        self.assertListNodes(toList("807"), s.addTwoNumbers(toList("342"), toList("465")))


    def assertListNodes(self, l1, l2):
        while l1 and l2:
            self.assertEqual(l1.val, l2.val)
            l1 = l1.next
            l2 = l2.next

        self.assertEqual(None, l1)
        self.assertEqual(None, l2)

def toList(s):
    h = None
    r = None
    for c in reversed(s):
        l = ListNode(int(c))
        if not h:
            h = l
        if r:
            r.next = l
        r = l
    return h


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()