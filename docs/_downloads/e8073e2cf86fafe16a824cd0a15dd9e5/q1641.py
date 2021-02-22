'''
1641. Count Sorted Vowel Strings
https://leetcode.com/problems/count-sorted-vowel-strings/


n = 1
1 + 1 + 1 + 1 + 1

n = 2
5 + 4 + 3 + 2 + 1

n = 3
5 + 4 + 3 + 2 + 1  -- p(3, a) = 15 + p(3, e)
  + 4 + 3 + 2 + 1  -- p(3, e) = 10 + p(3, i)
      + 3 + 2 + 1  -- p(3, i) =  6 + p(3, o)
          + 2 + 1  -- p(3, o) =  3 + p(3, u)
              + 1  -- p(3, u)
                

  a      e      i      o      u
    
  1      1      1      1      1      n = 1
  5      4      3      2      1      n = 2
  p3,a   p3,e   p3,i   p3,o   p3,u   n = 3
  p4,a   p4,e   p4,i   p4,o   p4,u   n = 4
  p5,a   p5,e   p5,i   p5,o   p5,u   n = 5

  p6,a   p6,e   p6,i   p6,o   p6,u   n = 6

  p4,a = p3,a + p3,e + p3,i + p3,o + p3,u
  p4,e = p3,e + p3,i + p3,o + p3,u
  p4,i = p3,i + p3,o + p3,u
  p4,o = p3,o + p3,u
  p4,u = p3,u

  p5,a = p4,a + p4,e + p4,i + p4,o + p4,u
  p5,e = p4,e + p4,i + p4,o + p4,u
  p5,i = p4,i + p4,o + p4,u
  p5,o = p4,o + p4,u
  p5,u = p4,u

  p6,a = p5,a + p5,e + p5,i + p5,o + p5,u
  p6,e =        p5,e + p5,i + p5,o + p5,u
  p6,i =               p5,i + p5,o + p5,u
  p6,o =                      p5,o + p5,u
  p6,u =                             p5,u

  p7,a = p6,a + p6,e + p6,i + p6,o + p6,u
  p7,e =        p6,e + p6,i + p6,o + p6,u
  p7,i =               p6,i + p6,o + p6,u
  p7,o =                      p6,o + p6,u
  p7,u =                             p6,u
  
  pn,a = pn-1,a + pn-1,e + pn-1,i + pn-1,o + pn-1,u
  pn,e = pn-1,e + pn-1,i + pn-1,o + pn-1,u
  pn,i = pn-1,i + pn-1,o + pn-1,u
  pn,o = pn-1,o + pn-1,u
  pn,u = pn-1,u
'''
from unittest import TestCase

class Solution:
    '''
    78.62%
    '''
    def countVowelStrings(self, n: int) -> int:
        if n < 1: return 0
        elif n == 1: return 5
        else:
            pn_1 = [1] * 5
            pn = [0] * 5
            i = 2
            while i <= n:
                for vowel in range(5):
                    pn[vowel] = sum(pn_1[vowel:])

                pn_1 = pn
                i += 1
            return sum(pn)

if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    t.assertEqual(5, s.countVowelStrings(1));
    t.assertEqual(15, s.countVowelStrings(2));
    t.assertEqual(66045, s.countVowelStrings(33));
    
    print('OK!')
