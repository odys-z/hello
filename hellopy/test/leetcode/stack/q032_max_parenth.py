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

@author: odys-z@github.com
'''
import unittest

class Solution20ms:
    ''' actually 44ms '''
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        
        stack = []
        stack.append(-1)
        max_len = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                max_len = max(max_len, i - stack[-1])
        
        return max_len

class Solution2:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        
        stack = [-1]
        # import re
        # s = re.sub(r'^\)+', '', s)
        
        maxlen = 0
        for ix, c in enumerate(s):
            if c == '(':
                stack.append(ix)
            else:
                stack.pop() 
                if not stack:
                    stack.append(ix)
                maxlen = max(maxlen, ix - stack[-1])
        return maxlen
    
class SolutionDp:
    ''' see solution 2 of https://leetcode.com/problems/longest-valid-parentheses/solution/
    '''
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        
        ix = 0
        while ix < len(s) and s[ix] == ')': 
            ix += 1
        s = s[ix:]

        # dp = [-1 for _ in s] 
        dp = [-1] * len(s)
        maxl = 0
 
        for ix, c in enumerate(s):
            if c == ')':
                c0 = s[ix - 1]
                if c0 == '(':
                    dp[ix] = 2
                    prevIx = ix - 2
                    if prevIx >= 0 and dp[prevIx] > 0:
                        dp[ix] += dp[prevIx]
                elif dp[ix - 1] > 0: # c0 == ')' and valid
                    prevIx = ix - dp[ix - 1] - 1
                    if prevIx >= 0 and s[prevIx] == '(':
                        dp[ix] = dp[ix - 1] + 2
                        if prevIx > 0:
                            prevlen = dp[prevIx - 1]
                            dp[ix] += prevlen if prevlen > 0 else 0
                if maxl < dp[ix]:
                    maxl = dp[ix]
            else:
                dp[ix] = 0
        return maxl
        

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk = list()
        maxlen = 0
        for c in s:
            if c == ')':
                if len(stk) > 0:
                    if stk[-1][0] == '(':
                        # pop and push
                        stk[-1] = ('x', 2)
                        if maxlen < 2:
                            maxlen = 2
                    else:
                        leng = 0
                        top = stk.pop() if stk else None
                        while top and top[0] != '(':
                            leng += top[1]
                            top = stk.pop() if stk else None
                        if top and top[0] == '(':
                            stk.append(('x', 2 + leng))
                            if maxlen < 2 + leng:
                                maxlen = 2 + leng
                        # wrong ')' triggering valid matched popping, remember what's popped
                        elif maxlen < leng:
                            maxlen = leng
            else:
                stk.append(('(', 0)) # 0 not used

        leng = 0
        while stk:
            while stk and stk[-1][0] == '(':
                stk.pop()

            leng = 0
            while stk and stk[-1][0] == 'x':
                leng += stk.pop()[1]
            if maxlen < leng:
                maxlen = leng
            
        return maxlen
        
class Test(unittest.TestCase):
    def testName(self):
        # s = Solution()
        # s = Solution20ms()
        # s = Solution2()
        s = SolutionDp()
        self.assertEqual(0, s.longestValidParentheses(''))
        self.assertEqual(0, s.longestValidParentheses('('))
        self.assertEqual(0, s.longestValidParentheses(')'))
        self.assertEqual(0, s.longestValidParentheses(')('))
        self.assertEqual(2, s.longestValidParentheses('()'))
        self.assertEqual(0, s.longestValidParentheses('))'))
        self.assertEqual(0, s.longestValidParentheses('(('))
        self.assertEqual(2, s.longestValidParentheses(')()'))
        self.assertEqual(2, s.longestValidParentheses('(()('))
        self.assertEqual(2, s.longestValidParentheses(')())('))
        self.assertEqual(4, s.longestValidParentheses('(()()'))
        self.assertEqual(6, s.longestValidParentheses('(()())'))
        self.assertEqual(2, s.longestValidParentheses(')()))('))
        self.assertEqual(4, s.longestValidParentheses(')()()'))
        self.assertEqual(4, s.longestValidParentheses('(()))())('))

        self.assertEqual(2, s.longestValidParentheses('(()(((()'))
        self.assertEqual(4, s.longestValidParentheses(')()())'))
        self.assertEqual(10, s.longestValidParentheses(')()(((())))('))
        self.assertEqual(6, s.longestValidParentheses('(())()('))
        self.assertEqual(6, s.longestValidParentheses('(())()(()(('))
        self.assertEqual(16, s.longestValidParentheses('(((()())))(()())'))
        self.assertEqual(16, s.longestValidParentheses('(((()()))(()()))'))
        self.assertEqual(16, s.longestValidParentheses('((()())((()())))'))
        self.assertEqual(16, s.longestValidParentheses('((()((()())())))'))

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