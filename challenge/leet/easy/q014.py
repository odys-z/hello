'''
13. Roman to Integer
https://leetcode.com/problems/longest-common-prefix/


Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow", "flight"]
Output: "fl"
'''

from unittest import TestCase
from typing import List

class Solution:
    ''' BFS
    55.94%
    '''
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cl = 0
        common = ''
        if not strs or len(strs) == 0 or len(strs[0]) == 0:
            return common
        while True:
            if len(strs[0]) <= cl: return common
            common += strs[0][cl]
            for w in strs:
                if len(w) < cl:
                    return common[:-1]
                elif w[0:cl+1] != common:
                    return common[:-1]
            cl += 1
        return common # shouldn't happen
            
if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    t.assertEqual('fl', s.longestCommonPrefix(['flower', 'flow', 'flight']))
    t.assertEqual('flow', s.longestCommonPrefix(['flower', 'flow']))
    t.assertEqual('', s.longestCommonPrefix(["dog","racecar","car"]))
    t.assertEqual('', s.longestCommonPrefix([]))
    t.assertEqual('', s.longestCommonPrefix([""]))
    t.assertEqual('a', s.longestCommonPrefix(["a"]))
    
    print('OK!')