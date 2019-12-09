'''
5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad" Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd" Output: "bb"

Created on 9 Dec 2019

@author: ody
'''
import unittest

'''
This article is far more clearer (succinct and laconic) than of GeeksForGeeks:
[Manacher’s Algorithm Explained— Longest Palindromic Substring](https://medium.com/hackernoon/manachers-algorithm-explained-longest-palindromic-substring-22cb27a5e96f)

And [Hacker Rank, Manacher's Algorithm](https://www.hackerrank.com/topics/manachers-algorithm)
'''

'''
Runtime: 2124 ms, faster than 45.57% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Longest Palindromic Substring.
'''
class Solution:
    def longestPalindrome(self, t: str) -> str:
        cnt = 0
        s = '#' + '#'.join(t) + '#'
        p = [0 for _ in s]
        slen = len(s)
        maxL, mxl, mxr = 0, 0, 0
        c, r = 0, 0
        for i in range(slen):
            c = i
            p[i] = min(p[2 * c - i], r - i)
            l, r = i - p[i] - 1, i + p[i] + 1
            while (0 <= l and r < slen and s[l] == s[r]):
                cnt += 1
                p[i] += 1
                l, r = l - 1, r + 1
            if maxL < p[i]:
                maxL, mxl, mxr = p[i], l + 1 if l > 0 else 0, r - 1 if r < slen else slen
        # return re.sub('#', '', s[mxl : mxr])
        print(slen, cnt)
        return t[mxl // 2 : mxr // 2]

'''
Runtime: 52 ms, faster than 99.77% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Longest Palindromic Substring.
'''
class SolutionRef:
    # LC 5 - Medium
    # Iterative
    # Space:    O(n^2)
    # Time:     O(n^2)
    def longestPalindrome(self, s: str) -> str:
        cnt = 0
        start, maxLen = 0, 1
        for i in range(1, len(s)):
            cnt += 1
            im = i-maxLen
            if im >= 1 and s[im-1:i+1] == s[im-1:i+1][::-1]:
                start = im-1
                maxLen += 2
            elif im >= 0 and s[im:i+1] == s[im:i+1][::-1]:
                start = im
                maxLen += 1
        print(len(s), cnt)
        return s[start:start+maxLen]

    # Brute force
    # Space:    O(n^3)
    # Time:     O(n^3)
    def longestPalindrome2(self, s: str) -> str:
        n, ans = len(s), ""
        isPalindrome = lambda s: s == s[::-1]

        for i in range(n):
            for j in range(n, i, -1):
                cand = s[i:j]
                ans = cand if len(cand) > len(ans) and isPalindrome(cand) else ans
        return ans

class Test(unittest.TestCase):
    def testName(self):
        s = Solution()
        self.assertEqual('a', s.longestPalindrome('a'))
        self.assertEqual('a', s.longestPalindrome('ab'))
        self.assertEqual('bb', s.longestPalindrome('bb'))
        self.assertEqual('a', s.longestPalindrome('abc'))
        self.assertEqual('a', s.longestPalindrome('abcd'))
        self.assertEqual('', s.longestPalindrome(''))
        self.assertEqual('aba', s.longestPalindrome('aba'))
        self.assertEqual('bab', s.longestPalindrome('babad'))
        self.assertEqual('bab', s.longestPalindrome('babad'))
        self.assertEqual("cccccc fdfdfebbbbbbbbbbefdfdf cccccc",
                         s.longestPalindrome('babadbbcdfavvedf feescsefcv   svsvscxseretv dfhbdsvfdgbhyn  bbrdherrvgerg  svsgr54yurrtjk6fgfbfhtgsgtcccccc fdfdfebbbbbbbbbbefdfdf ccccccdededde'))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()