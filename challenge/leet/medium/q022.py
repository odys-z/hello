'''
Created on 12 Jan 2021

https://leetcode.com/problems/generate-parentheses/
generate parenthesis

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

@author: Odys Zhou
'''
import unittest
from typing import List

class Solution:
    '''
    (((   (((   (((
    )))    ))     )
    '''
    def generateParenthesis(self, n: int) -> List[str]:
        if n <= 0: return []

        l, r = n, n # l: ['('] * n, r: [')'] * n
        stack = []
        res = {}
        
        stack.append('(')
        l -= 1
        
        
        def generate(stack, l, r) -> None:
            stack = stack.copy()

            if l == 0 and r == 0:
                res[stack.pop()] = None
                return

            if l > 0:
                l -= 1
                stack.append('(')
                generate(stack, l, r)
            
            if r > 0:
                r -= 1
                tmp = stack.pop()
                if len(stack) == 0:
                    res[tmp + ')'] = None
                else:
                    prev = stack.pop()
                    stack2 = stack.copy()
                    stack3 = stack.copy()
                    stack4 = stack.copy()
                    stack.append(prev + ')' + tmp)
                    generate(stack, l, r)

                    stack2.append(prev + tmp + ')')
                    generate(stack2, l, r)

                    stack3.append(tmp + prev + ')')
                    generate(stack3, l, r)

                    stack4.append(tmp + ')' + prev)
                    generate(stack4, l, r)
        generate(stack, l, r)
        return list(res.keys())

if __name__ == "__main__":
    
    t = unittest.TestCase()
    s = Solution()
    t.assertEqual([], s.generateParenthesis(0))
    t.assertEqual(['()'], s.generateParenthesis(1))
    t.assertCountEqual(['()()', '(())'], s.generateParenthesis(2))
    t.assertCountEqual(['(())()', '((()))', '()(())', '(()())', '()()()'], s.generateParenthesis(3))

    print(s.generateParenthesis(4))
    # First has 1, Second has 0:  '((()))()'
    t.assertCountEqual(["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"],
                       s.generateParenthesis(4))
   
    print('OK!')
