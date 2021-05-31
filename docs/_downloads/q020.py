'''
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

'''
from unittest import TestCase

class Solution:
    '''
        95.88%
    '''
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c == ' ': continue # for string readable
            if c in ('(', '{', '['):
                stk.append(c)
            elif len(stk) > 0:
                if ( stk[-1] == '(' and c == ')'
                   or stk[-1] == '{' and c == '}'
                   or stk[-1] == '[' and c == ']'):
                    stk.pop()
                else:
                    return False
            else: return False
        return len(stk) == 0

if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    
    t.assertTrue(s.isValid(''))
    t.assertTrue(s.isValid('()'))
    t.assertTrue(s.isValid('()[]{}'))
    t.assertTrue(s.isValid('()[{}]'))
    t.assertTrue(s.isValid('([{}])'))
    t.assertTrue(s.isValid('() [{}] [] [[[]]]'))
    t.assertFalse(s.isValid('(( [{}] [] [[[]]]'))
    t.assertFalse(s.isValid('(( [{}] [] [[[]]] )'))
    t.assertTrue(s.isValid('(( [{}] [] [[[]]] ))'))
    t.assertFalse(s.isValid('([{])'))
    t.assertFalse(s.isValid('([{]})'))

    print('OK!')