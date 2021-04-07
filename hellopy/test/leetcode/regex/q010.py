import unittest

'''
10. Regular Expression Matching
https://leetcode.com/problems/regular-expression-matching/

Runtime: 1548 ms, faster than 7.77% of Python3 online submissions for Regular Expression Matching.
Memory Usage: 13.8 MB, less than 5.55% of Python3 online submissions for Regular Expression Matching.
'''
class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        plen = len(p) if p is not None else 0
        slen = len(s) if s is not None else 0
        if p is None or plen == 0:
            return s is None or slen == 0

        m0 = slen > 0 and (p[0] == s[0] or p[0] == '.')

        if plen > 1 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (m0 and self.isMatch(s[1:], p))
        else:
            return m0 and self.isMatch(s[1:], p[1:])

slen = 0
plen = 0
'''
Runtime: 1156 ms, faster than 26.37% of Python3 online submissions for Regular Expression Matching.
Memory Usage: 13.8 MB, less th
'''
class Solution3:
    def isMatch(self, s: str, p: str) -> bool:
        global plen, slen
        plen = len(p) if p is not None else 0
        slen = len(s) if s is not None else 0
        if plen == 0:
            return slen == 0

        return self.match(s, 0, p, 0)

    def match(self, s: str, sx: int, p: str, px: int):
        global plen, slen
        if px >= plen:
            return sx >= slen
        
        m0 = slen > sx and (p[px] == s[sx] or p[px] == '.')

        if px < plen-1 and p[px+1] == '*':
            return self.match(s, sx, p, px+2) or (m0 and self.match(s, sx+1, p, px))
        else:
            return m0 and self.match(s, sx+1, p, px+1)

ij = None;
'''
Runtime: 36 ms, faster than 94.87% of Python3 online submissions for Regular Expression Matching.
Memory Usage: 13.6 MB, less than 5.55% of Python3 online submissions for Regular Expression Matching.
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        global plen, slen, ij
        plen = len(p) if p is not None else 0
        slen = len(s) if s is not None else 0
        if plen == 0:
            return slen == 0
        ij = [None] * (slen+1)
        return self.matchDp(s, 0, p, 0)

    def matchDp(self, s: str, sx: int, p: str, px: int):
        global plen, slen, ij
        if px >= plen:
            return sx >= slen
        
        if (ij[sx] is None):
            ij[sx] = [None] * (plen+1)
            
        if (ij[sx][px] is None):
            m0 = slen > sx and (p[px] == s[sx] or p[px] == '.')

            if px < plen-1 and p[px+1] == '*':
                ij[sx][px] = self.matchDp(s, sx, p, px+2) or (m0 and self.matchDp(s, sx+1, p, px))
            else:
                ij[sx][px] = m0 and self.matchDp(s, sx+1, p, px+1)
        return ij[sx][px]

class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        self.assertTrue(s.isMatch(None, None))
        self.assertTrue(s.isMatch("", None))
        self.assertTrue(s.isMatch("", ""))
        self.assertTrue(s.isMatch("", ".*"))
        self.assertTrue(s.isMatch(None, ".*"))
        self.assertTrue(s.isMatch('', '.*'))
        self.assertFalse(s.isMatch("", "a"))
        self.assertTrue(s.isMatch("", "a*"))
        self.assertTrue(s.isMatch("", "c*c*"))
        self.assertFalse(s.isMatch("a", ""))
        self.assertTrue(s.isMatch('a', '.'))
        self.assertTrue(s.isMatch("a", "a"))
        self.assertFalse(s.isMatch("aa", "a"))
        self.assertTrue(s.isMatch("ab", ".b"))
        self.assertTrue(s.isMatch("ab", ".*"))
        self.assertTrue(s.isMatch("aaa", ".*"))
        self.assertTrue(s.isMatch("aab", "c*a*b"))
        self.assertFalse(s.isMatch("mississippi", "mis*is*p*."))
        self.assertTrue(s.isMatch( "mississippi", "mis*is*ip*."))
        self.assertTrue(s.isMatch( "mississi", "mis*is*i*"))
        self.assertFalse(s.isMatch("mississi", "mis*is*i."))
        self.assertTrue(s.isMatch( "mississi", "mis*is*i.*"))
        self.assertTrue(s.isMatch( "mississi", "mis*is*i"))
        self.assertTrue(s.isMatch("{\"\":\"ississ123}", "{\"\":\"is*is*123}"))
        self.assertTrue(s.isMatch("{\"\":  123}", "{\"\": *123}"))
        self.assertTrue(s.isMatch("mississi", "...*is*i"))
        self.assertTrue(s.isMatch("mississi", ".*i.*i.*i.*"))
        self.assertTrue(s.isMatch("iii", ".*i.*i.*i.*"))
        self.assertTrue(s.isMatch("1i2ii4", ".*i.*i.*i.*"))
        self.assertTrue(s.isMatch("1i2i i", ".*i.*i.*i.*"))
        self.assertTrue(s.isMatch("i i iss", ".*i.*i.*i.*"))
        self.assertFalse(s.isMatch("i", ".*i.*i"))
