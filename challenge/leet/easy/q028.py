'''
28. Implement strStr()
https://leetcode.com/problems/implement-strstr/

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to
C's strstr() and Java's indexOf().

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Example 3:
Input: haystack = "", needle = ""
Output: 0
 
Constraints:
0 <= haystack.length, needle.length <= 5 * 104
haystack and needle consist of only lower-case English characters.
'''
from unittest import TestCase

class Solution:
    '''
    73.07%
    '''
    def strStr(self, haystack: str, needle: str) -> int:
        nl = len(needle)
        if nl == 0:
            return 0
        for x in range(len(haystack) - nl + 1):
            if needle == haystack[x : x + nl]:
                return x
        return -1
        
if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    
    t.assertEqual(0, s.strStr('a', 'a'))
    t.assertEqual(2, s.strStr('hello', 'll'))
    t.assertEqual(-1, s.strStr('aaaaa', 'baa'))
    t.assertEqual(0, s.strStr('aaaaa', 'aa'))
    t.assertEqual(4, s.strStr('ababaa', 'aa'))
    t.assertEqual(0, s.strStr('', ''))
    
    print('OK!')