'''
q2063 Vowels of All Substrings
https://leetcode.com/problems/vowels-of-all-substrings/
'''
from unittest import TestCase

class Solution2:
    '''
        time exceed
    '''
    def countVowels(self, word: str) -> int:
        dp = {}

        def countV(s):
            if s in dp:
                return dp[s]

            cnt = 0
            for c in s:
                if c in {'a', 'e', 'i', 'o', 'u'}:
                    cnt += 1
            
            dp.update({s: cnt})
            return cnt

        l, vowels = len(word), 0
        
        for i in range(l):
            for sub in range(1, l - i + 1):
                vowels += countV(word[i : i+sub])
        return vowels

class Solution3:
    '''
    5.28%
    Number of substrings of a string:
    https://www.geeksforgeeks.org/number-substrings-string/
    '''

    def countVowels(self, word: str) -> int:
        def countSub(l, r):
            return 0 if l >= r else (r - l) * (r - l + 1) // 2

        L = len(word)
        dp = [0] * L
        for i in range(L):
            dp[i] = ( 0 if word[i] not in {'a', 'e', 'i', 'o', 'u'}
                        else countSub(0, L) - countSub(0, i) - countSub(i+1, L))
        
        return sum(dp)

class Solution:
    '''
    97.4%
    
    0     i     n
    . ... . ...
    
    i-th used count (exluding way):
    n * (n+1) /2 - i * (i+1) /2 - (n-i-1)(n-i) /2
    = 1/2 [ n^2 + n - i^2 - i - (n-i)^2 + (n-i) ]
    = 1/2 [ n^2 + n - i^2 - i - n^2 + 2ni - i^2 + n - i ]
    = 1/2 [     + n - i^2 - i       + 2ni - i^2 + n - i ]
    = ni - i^2 + n - i
    = (n - i) i + (n - i)
    = (n - i) (i + 1)
    
    i-th used (2 steps multiple principal)
    i choice from the first i units, including i-th, at least 1;
    n - i choice form the following n - i units, joining i-th.
    (i + 1) (n - i)
    '''
    def countVowels(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            if s[i] in 'aeiou':
                res += (i + 1) * (n - i)
        return res
    
if __name__ == '__main__':
    t = TestCase()
    s = Solution()

    t.assertEqual(6, s.countVowels('aba'))
    t.assertEqual(3, s.countVowels('abc'))
    t.assertEqual(0, s.countVowels('ltcd'))

    print('OK!')
