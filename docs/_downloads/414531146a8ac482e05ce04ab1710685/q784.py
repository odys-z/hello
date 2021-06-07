'''
784. Letter Case Permutation
https://leetcode.com/problems/letter-case-permutation/

Given a string S, we can transform every letter individually to be lowercase or uppercase to create
another string.

Return a list of all possible strings we could create. You can return the output in any order.

Example 1:
Input: S = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Example 2:
Input: S = "3z4"
Output: ["3z4","3Z4"]

Example 3:
Input: S = "12345"
Output: ["12345"]

Example 4:
Input: S = "0"
Output: ["0"]
 

Constraints:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.

Created on 23 Feb 2021

@author: Odys Zhou
'''
from unittest import TestCase
from typing import List

class Solution:
    ''' 88.03%
    '''
    def letterCasePermutation(self, S: str) -> List[str]:
        def btracking(s: str) -> List[str]:
            if len(s) == 0: return []
            elif len(s) == 1: return [s] if s.isdigit() else [s.lower(), s.upper()]

            res = []
            tracks = btracking(s[:-1])
            for t in tracks:
                if (s[-1].isdigit()):
                    res.append(t + s[-1])
                else:
                    res.append(t + s[-1].lower())
                    res.append(t + s[-1].upper())
            return res
        
        return btracking(S)

if __name__ == '__main__':
    t = TestCase()
    s = Solution()

    t.assertCountEqual(['a1b2', 'a1B2', 'A1b2', 'A1B2'], s.letterCasePermutation('a1b2'))
    t.assertCountEqual(['3z4', '3Z4'], s.letterCasePermutation('3z4'))
    t.assertCountEqual(['3z4', '3Z4'], s.letterCasePermutation('3Z4'))
    t.assertCountEqual(['12345'], s.letterCasePermutation('12345'))
    t.assertCountEqual(['0'], s.letterCasePermutation('0'))
    t.assertCountEqual(['a', 'A'], s.letterCasePermutation('A'))
    
    print('OK!')