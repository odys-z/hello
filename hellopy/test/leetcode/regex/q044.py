import unittest

'''
44. Wildcard Matching
https://leetcode.com/problems/wildcard-matching/

Runtime: 564 ms, faster than 73.63% of Python3 online submissions for Wildcard Matching.
Memory Usage: 22.8 MB, less than 50.00% of Python3 online submissions for Wildcard Matching.
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
            m0 = slen > sx and (p[px] == s[sx] or p[px] == '?' or p[px] == "*")

            if px < plen and p[px] == '*':
                ij[sx][px] = self.matchDp(s, sx, p, px+1) or (m0 and self.matchDp(s, sx+1, p, px))
            else:
                ij[sx][px] = m0 and self.matchDp(s, sx+1, p, px+1)
        return ij[sx][px]

slen = 0
plen = 0
ij = None

class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        self.assertTrue(s.isMatch(None, None))
        self.assertTrue(s.isMatch("", None))
        self.assertTrue(s.isMatch("", ""))
        self.assertTrue(s.isMatch("", "*"))
        self.assertFalse(s.isMatch("", "a*"))
        self.assertFalse(s.isMatch("", "?*"))
        self.assertFalse(s.isMatch(None, "?*"))
        self.assertTrue(s.isMatch('', '*'))
        self.assertFalse(s.isMatch("", "a"))
        self.assertFalse(s.isMatch("", "c*c*"))
        self.assertTrue(s.isMatch("cc", "c*c*"))
        self.assertFalse(s.isMatch("a", ""))
        self.assertTrue(s.isMatch('a', '?'))
        self.assertTrue(s.isMatch('a', '*'))
        self.assertTrue(s.isMatch('aa', '*'))
        self.assertTrue(s.isMatch("a", "a"))
        self.assertFalse(s.isMatch("aa", "a"))
        self.assertTrue(s.isMatch("ab", "?b"))
        self.assertFalse(s.isMatch("cb", "?a"))
        self.assertTrue(s.isMatch("ab", "*"))
        self.assertTrue(s.isMatch("aaa", "?*"))
        self.assertTrue(s.isMatch("aab", "*a*b"))
        self.assertFalse(s.isMatch("acdcb", "a*c?b"))
        self.assertTrue(s.isMatch("adceb", "*a*b"))
        self.assertTrue(s.isMatch("mississippi", "mis*is*p*?"))
        self.assertTrue(s.isMatch("mississippi", "mi*i*?"))
        self.assertTrue(s.isMatch( "mississippi", "mis*is*ip*?"))
        self.assertTrue(s.isMatch( "mississi", "mis*is*i*"))
        self.assertFalse(s.isMatch("mississi", "mis*is*i?"))
        self.assertTrue(s.isMatch( "mississii", "mis*is*i?*"))
        self.assertFalse(s.isMatch( "mississi", "mis*is*i?*"))
        self.assertTrue(s.isMatch( "mississi", "mis*is*i*"))
        self.assertTrue(s.isMatch( "mississi", "mis*is*i"))
        self.assertTrue(s.isMatch("{\"\":\"ississ123}", "{\"\":\"is*is*123}"))
        self.assertTrue(s.isMatch("{\"\":  123}", "{\"\": *123}"))
        self.assertTrue(s.isMatch("mississi", "???*is*i"))
        self.assertTrue(s.isMatch("mississi", "*i*i*i*"))
        self.assertTrue(s.isMatch("iii", "*i*i*i*"))
        self.assertTrue(s.isMatch("1i2ii4", "*i*i*i*"))
        self.assertTrue(s.isMatch("1i2i i", "*i*i*i*"))
        self.assertTrue(s.isMatch("i i iss", "*i*i*i*"))
        self.assertFalse(s.isMatch("i", "*i*i"))
