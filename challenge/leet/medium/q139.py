'''
'''

from unittest import TestCase
from typing import List

class SolutionError:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def wordBrakeAt(s, at, dic):
            l, r = at, at + 1
            while r <= len(s):
                if s[l:r] in wordDict:
                    if r == len(s) or wordBrakeAt(s, r, dic):
                        return True
                r += 1
            return False

        return wordBrakeAt(s, 0, wordDict)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(s) == 0: return True
        d = dict.fromkeys(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in d:
                    dp[i] = True
                    break
        
        return dp[len(s)]
    
if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    t.assertEqual(True, s.wordBreak("leetcode", ["leet", "code"]))
    t.assertEqual(True, s.wordBreak("applepenapple", ["apple", "pen"]))
    t.assertEqual(False, s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    t.assertEqual(True, s.wordBreak("catsanddog", ["cats", "dog", "sand", "and", "cat"]))
    t.assertEqual(True, s.wordBreak("1234abcdede", ["1234", "abcd", "abcde", "de"]))
    t.assertEqual(False, s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
                                    ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))

    print('OK!')