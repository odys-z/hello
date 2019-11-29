'''
32. Longest Valid Parentheses
https://leetcode.com/problems/longest-valid-parentheses/

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

Created on 29 Nov 2019

@author: ody
'''
import unittest

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        balance = 0
        maxlen = 0
        l = -1
        prevLen = 0
        for ix, p in enumerate(s):
            if p == ')':
                if balance > 0:
                    balance -= 1

                    length = ix - l + 1 - balance
                    if balance == 0:
                        length += prevLen
                        prevLen = length

                    if maxlen < length:
                        maxlen = length
                else: # balance broken
                    prevLen = 0

            else: # '('
                balance += 1
                if balance == 1:
                    l = ix
        return maxlen
        
class Test(unittest.TestCase):
    def testName(self):
        s = Solution()
        self.assertEqual(0, s.longestValidParentheses(''))
        self.assertEqual(0, s.longestValidParentheses('('))
        self.assertEqual(0, s.longestValidParentheses(')'))
        self.assertEqual(2, s.longestValidParentheses(')()'))
        self.assertEqual(0, s.longestValidParentheses('))'))
        self.assertEqual(0, s.longestValidParentheses(')('))
        self.assertEqual(0, s.longestValidParentheses('(('))
        self.assertEqual(2, s.longestValidParentheses('(()('))
        self.assertEqual(2, s.longestValidParentheses(')())('))
        self.assertEqual(4, s.longestValidParentheses(')()()'))
        self.assertEqual(2, s.longestValidParentheses('(()(((()'))
        self.assertEqual(0, s.longestValidParentheses('((('))
        self.assertEqual(0, s.longestValidParentheses(')((('))
        self.assertEqual(2,s.longestValidParentheses("())()"))
        self.assertEqual(10,s.longestValidParentheses("((())())()"))
        self.assertEqual(8,s.longestValidParentheses("((())())("))
        self.assertEqual(10,s.longestValidParentheses(")((())())()"))
        self.assertEqual(8,s.longestValidParentheses("())())())(())())())((())()))())())))()))())())"))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()