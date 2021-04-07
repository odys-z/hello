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
Runtime: 100 ms, faster than 94.58% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Longest Palindromic Substring.
'''
class Solution:
    def longestPalindrome(self, t: str) -> str:
        cnt = 0
        s = '#' + '#'.join(t) + '#'
        p = [0] * len(s)
        slen = len(s)
        # maxL, mxl, mxr = 0, 0, 0
        maxL, mxl = 0, 0
        c, R = 0, 0
        for i in range(slen):
            mirror = 2 * c - i
            p[i] = min(p[mirror] if mirror >= 0 else 0, R - i - 1)
            li, ri = i - p[i] - 1, i + p[i] + 1
            while (0 <= li and ri < slen and s[li] == s[ri]):
                cnt += 1
                p[i] += 1
                li, ri = li - 1, ri + 1
            if (i + p[i] >= R - 1):
                c = i
                R = i + p[i] + 1
            if maxL < p[i]:
                maxL, mxl = p[i], li + 1 if li > 0 else 0
        print(slen, cnt)
        mxr = maxL * 2 + 1 + mxl
        mxr = slen if mxr > slen else mxr
        return t[mxl // 2 : mxr // 2]

'''
Runtime: 136 ms, faster than 92.98% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Longest Palindromic Substring.
'''
class Solution2:
    def longestPalindrome(self, raws: str) -> str:
        polin = polindromeString(raws)
        # s = '#' + '#'.join(t) + '#'
        slen = polin.len()

        cnt = 0
        p = [0] * slen

        maxL, mxl = 0, 0
        c, R = 0, 0
        for i in range(slen):
            mirror = 2 * c - i
            if mirror < 0: mirror = 0
            p[i] = min(p[mirror], R - i)
            l, r = i - p[i] - 1, i + p[i] + 1
            while (0 <= l and r < slen and polin.at(l) == polin.at(r)):
                cnt += 1
                p[i] += 1
                l, r = l - 1, r + 1
            if (i + p[i] >= R):
                c = i
                R = i + p[i]
            if maxL < p[i]:
                maxL, mxl = p[i], l + 1 if l > 0 else 0 #, r - 1 if r < slen else slen
        print(slen, cnt)
        mxr = maxL * 2 + 1 + mxl
        if mxr > slen:
            mxr = slen
        return polin.sub(mxl // 2, mxr // 2)

class polindromeString:
    def __init__(self, rawstr):
        self.raws = rawstr
    
    def len(self):
        return len(self.raws) * 2 + 1
    
    def sub(self, l, r):
        return self.raws[l : r]
    
    def at(self, ix):
        if ix % 2 == 0:
            return '#'
        else:
            return self.raws[ix // 2]
    

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

class SolutionM:
    def longestPalindrome(self, s: str) -> str:
        st = '$#' + '#'.join(s) + '#%'
        
        cnt = 0

        P = [0]*len(st)
        C,R = 0, 0
        for i in range(1, len(st)-1):
            mirr = 2*C-i
            
            # update already expanded palindrome
            if i < R:
                P[i] = min(R-i, P[mirr])
            
            while st[i+(1+P[i])] == st[i-(1+P[i])]:
                cnt += 1
                P[i] += 1
            
            if i+P[i] > R:
                C = i
                R = i + P[i]
        
        length = max(P)
        index = P.index(length)
        string = st[index-length:index+length]
        
        print(len(st), cnt)
        return string.replace('#','')

class Test(unittest.TestCase):
    def testName(self):
        s = Solution2()
        self.assertEqual('a', s.longestPalindrome('a'))
        self.assertEqual('a', s.longestPalindrome('ab'))
        self.assertEqual('bb', s.longestPalindrome('bb'))
        self.assertEqual('a', s.longestPalindrome('abc'))
        self.assertEqual('a', s.longestPalindrome('abcd'))
        self.assertEqual('', s.longestPalindrome(''))
        self.assertEqual('aba', s.longestPalindrome('aba'))
        self.assertEqual('bab', s.longestPalindrome('babad'))
        self.assertEqual('babab', s.longestPalindrome('bababd'))
        self.assertEqual('bab', s.longestPalindrome('babad'))
        self.assertEqual('adada', s.longestPalindrome('babadada'))
        self.assertEqual("cccccc fdfdfebbbbbbbbbbefdfdf cccccc",
                         s.longestPalindrome('babadbbcdfavvedf feescsefcv   svsvscxseretv dfhbdsvfdgbhyn  bbrdherrvgerg  svsgr54yurrtjk6fgfbfhtgsgtcccccc fdfdfebbbbbbbbbbefdfdf ccccccdededde'))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()