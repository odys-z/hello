'''
6. ZigZag Conversion
https://leetcode.com/problems/zigzag-conversion/

See java version leetcode.array.q006_zigzag.Solution

Created on 15 Dec 2019

@author: odys-z@github.com
'''
import unittest

class Solution:
    '''
    v = 0,  v = 1          v = 2        ...    l + (k-2) / (k-1)
u=0    0    [ ]            2(k-1)
u=1    1    k-1 + k-2
    
            k-1 + 1
u=k-1  [ ]  k-1 + 0

    z is max(k-1, maxv), where maxv = l + (k-1) // (k-1)
    z(u, v) = v(k-1) + u, v is even
    z(u, v) = v(k-1) - u + k-1, v is odd
    
    Runtime: 60 ms, faster than 79.40% of Python3 online submissions for ZigZag Conversion.
    Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for ZigZag Conversion.
    '''
    def convert(self, s: str, k: int) -> str:
        if s is None or len(s) <= k or k < 2:
            return s

        l = len(s)
        res = ''
        k_1 = k - 1
        maxv = (l + k-2) // (k_1)
        for u in range(k):
            for v in range(maxv):
                if v % 2 == 0: # even
                    at = v * (k_1) + u
                    if at >= l:
                        break;
                    elif u % k != k_1:
                        res = res + s[at]
                else: # odd
                    at = v * k_1 - u + k_1
                    if at >= l:
                        break;
                    elif u % k != 0:
                        res = res + s[at]
        return res
        

class Test(unittest.TestCase):


    def testName(self):
        s = Solution()
        self.assertEqual("", s.convert("", 1))
        self.assertEqual("1", s.convert("1", 1))
        self.assertEqual("", s.convert("", 1))
        self.assertEqual("12", s.convert("12", 4))
        self.assertEqual("12", s.convert("12", 1))
        self.assertEqual("12", s.convert("12", 2))
        self.assertEqual("ABCDEFGHIJKLMNOPQRSTUVW", s.convert("ABCDEFGHIJKLMNOPQRSTUVW", 1))
        self.assertEqual("PINALSIGYAHRPI", s.convert("PAYPALISHIRING", 4))
        self.assertEqual("PAHNAPLSIIGYIR", s.convert("PAYPALISHIRING", 3))
        self.assertEqual("PINALSIGYAHRPI", s.convert("PAYPALISHIRING", 4))
        ''' P      H
            A   S  I
            Y   I  R
            P L    I G
            A      N
            "PHASIYIRPLIGAN"
        '''
        self.assertEqual("PHASIYIRPLIGAN", s.convert("PAYPALISHIRING", 5))
        self.assertEqual("AHBHGACGFBDFECED", s.convert("ABCDEFGHHGFEDCBA", 5))
        self.assertEqual("ABACBDCEDFEGFHGH", s.convert("ABCDEFGHHGFEDCBA", 9))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()