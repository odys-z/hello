'''
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Created on 4 Dec 2019

@author: ody
'''
import unittest
from collections import deque

'''
Runtime: 76 ms, faster than 48.21% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Longest Substring Without Repeating Characters.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dct = dict();
        que = deque([]);
        p, maxlen = -1, 0
        for ix, c in enumerate(s):
            if c in dct:
                p = -1
                cx = dct.pop(c)
                while p < cx:
                    p, t = que.popleft()
                    if t in dct:
                        dct.pop(t)

            dct.update({c: ix})
            que.append((ix, c));
            
            maxlen = max(maxlen, ix - p)
        
        return maxlen
        
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        m = []
        for c in s:
            t = -1
            try: t = m.index(c)
            except: pass
            if t >= 0:
                m = m[t+1:] + [c]
            else:
                m.append(c)
                maxlen = max(maxlen, len(m))
        return maxlen

class Test(unittest.TestCase):

    def testQ3(self):
        s = Solution2()
        self.assertEqual(0, s.lengthOfLongestSubstring(''))
        self.assertEqual(1, s.lengthOfLongestSubstring('1'))
        self.assertEqual(1, s.lengthOfLongestSubstring('00'))
        self.assertEqual(1, s.lengthOfLongestSubstring('00000000'))
        self.assertEqual(2, s.lengthOfLongestSubstring('bab'))
        self.assertEqual(1, s.lengthOfLongestSubstring('bbbbbb'))
        self.assertEqual(3, s.lengthOfLongestSubstring('pwwkew'))
        self.assertEqual(5, s.lengthOfLongestSubstring('pwwkewab'))
        self.assertEqual(3, s.lengthOfLongestSubstring('abcabcbb'))
        self.assertEqual(3, s.lengthOfLongestSubstring("abcabcbb"))
        self.assertEqual(12, s.lengthOfLongestSubstring("abcabc #%$RDVZXDRV^F  bb"))
        self.assertEqual(2, s.lengthOfLongestSubstring("mmz"))
        self.assertEqual(3, s.lengthOfLongestSubstring("mmzu"))
        self.assertEqual(4, s.lengthOfLongestSubstring("tmzut"))
        self.assertEqual(4, s.lengthOfLongestSubstring("tmmzut"))
        self.assertEqual(5, s.lengthOfLongestSubstring("tmmzuxt"))
        self.assertEqual(4, s.lengthOfLongestSubstring("tmmzux"))
        self.assertEqual(5, s.lengthOfLongestSubstring("tmmzuxy"))
        self.assertEqual(5, s.lengthOfLongestSubstring("tmmzuxyy"))
        self.assertEqual(6, s.lengthOfLongestSubstring("tmmzuxys"))
        self.assertEqual(5, s.lengthOfLongestSubstring("tmmzuxyu"))
        self.assertEqual(12, s.lengthOfLongestSubstring("tmmzuxts123456"))
        self.assertEqual(3, s.lengthOfLongestSubstring("x110111011110x"))
        self.assertEqual(3, s.lengthOfLongestSubstring("1101110x011110"))
        print('OK!')

if __name__ == "__main__":
    t = Test()
    t.testQ3()