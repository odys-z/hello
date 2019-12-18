'''
8. String to Integer (atoi)

https://leetcode.com/problems/string-to-integer-atoi/

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace
character is found. Then, starting from this character, takes an optional initial plus or minus sign
followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored
and have no effect on the behavior of this function.
If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such
sequence exists because either str is empty or it contains only whitespace characters, no conversion
is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer
range: [−2^31,  2^31 − 1]. If the numerical value is out of the range of representable values, INT_MAX (2^31 − 1)
or INT_MIN (−2^31) is returned.

Example 1:
Input: "42"
Output: 42

Example 2:
Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.

Example 3:
Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Example 4:
Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.

Example 5:
Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
             
Created on 18 Dec 2019

@author: odys-z@github.com
'''
import unittest

class Solution():
    def myAtoi(self, digts: str) -> int:
        # s, i, i2, i8 = 0, 0, 0, 0
        s, i = 0, 0
        maxi = 2 ** 31
        for c in digts:
            if s == 0 and c == ' ':
                continue
            elif s == 0:
                if c == '-':
                    s = -1
                    continue
                elif s == 0 and c == '+':
                    s = 1
                    continue
                else: # s == 0:
                    s = 1

            if c < '0' or c > '9':
                return s * i
                
            # i2, i8 = i << 1, i << 3
            # i = int(c) + i2 + i8
            i = int(c) + i * 10
            if s == 1 and maxi <= i:
                return maxi - 1
            elif s == -1 and maxi < i:
                return - maxi

        return s * i
            

class Test(unittest.TestCase):


    def testName(self):
        s = Solution()
        self.assertEqual(0, s.myAtoi(" "))
        self.assertEqual(0, s.myAtoi(" -"))
        self.assertEqual(0, s.myAtoi(" +"))
        self.assertEqual(0, s.myAtoi("+"))
        self.assertEqual(0, s.myAtoi(""))
        self.assertEqual(0, s.myAtoi("0"))
        self.assertEqual(0, s.myAtoi("+0"))
        self.assertEqual(0, s.myAtoi("-0"))
        self.assertEqual(-1, s.myAtoi("-01"))
        self.assertEqual(42, s.myAtoi("42"))
        self.assertEqual(-1, s.myAtoi("-1"))
        self.assertEqual(1, s.myAtoi("+1"))
        self.assertEqual(0, s.myAtoi("+00000"))
        self.assertEqual(20, s.myAtoi("+0000020"))
        self.assertEqual(-20, s.myAtoi("-0000020"))
        self.assertEqual(0, s.myAtoi("----0000020"))
        self.assertEqual(0, s.myAtoi("+-2"))
        self.assertEqual(0, s.myAtoi("+++-2"))
        self.assertEqual(0, s.myAtoi("-++-2"))
        self.assertEqual(0, s.myAtoi("-+++2"))
        self.assertEqual(0, s.myAtoi("-++ 2"))
        self.assertEqual(-2, s.myAtoi("-2 ++ 4"))
        self.assertEqual(0, s.myAtoi("--2"))
        self.assertEqual(0, s.myAtoi(" + + 2 2 0"))
        self.assertEqual(0, s.myAtoi("+.2 2 0"))
        self.assertEqual(-2, s.myAtoi(" -2 ++ 3"))
        self.assertEqual(0, s.myAtoi("- 2 ++ 3"))
        self.assertEqual(0, s.myAtoi("-00000"))
        self.assertEqual(0, s.myAtoi("0"))
        self.assertEqual(-42, s.myAtoi("-42"))
        self.assertEqual(0, s.myAtoi("words and 987"))
        self.assertEqual(4193, s.myAtoi("4193 with words"))
        self.assertEqual(4193, s.myAtoi("4193-with-words"))
        self.assertEqual(419, s.myAtoi("+419-3-with-words"))
        self.assertEqual(41, s.myAtoi("41-9+3-with-words"))
        self.assertEqual(41, s.myAtoi("+41-9+3-with-words"))
        self.assertEqual(-4193, s.myAtoi("-4193 "))
        self.assertEqual(0x3FFFFFFF , s.myAtoi(" 1073741823 "))
        self.assertEqual(0x40000000 , s.myAtoi(" 1073741824 "))
        self.assertEqual(0x40000001 , s.myAtoi(" 1073741825 "))
        self.assertEqual(0x40000002 , s.myAtoi(" 1073741826 "))
        self.assertEqual(-1073741823 , s.myAtoi("-1073741823 "))
        self.assertEqual(-1073741824 , s.myAtoi("-1073741824 "))
        self.assertEqual(-1073741825 , s.myAtoi("-1073741825 "))
        self.assertEqual(0x7FFFFFFE , s.myAtoi(" 2147483646 "))
        self.assertEqual(0x7FFFFFFF , s.myAtoi(" 2147483647 "))
        self.assertEqual(0x7FFFFFFF , s.myAtoi(" 2147483648 "))
        self.assertEqual(-2147483647 , s.myAtoi(" -2147483647 "))
        self.assertEqual(-2147483648 , s.myAtoi(" -2147483648 "))
        self.assertEqual(-2147483648 , s.myAtoi(" -2147483649 "))
        self.assertEqual(-2147483648 , s.myAtoi(" -4294967296 "))
        self.assertEqual(0x7FFFFFFF, s.myAtoi(" 4294967295 "))
        #                1852516352              2147483648
        self.assertEqual(-2147483648, s.myAtoi(" -2147483649 "))
        self.assertEqual(-2147483648, s.myAtoi(" -2347483648 "))
        self.assertEqual(-2147483648, s.myAtoi(" -2447483648 "))
        self.assertEqual(-2147483648, s.myAtoi(" -2847483648 "))
        self.assertEqual(-2147483648, s.myAtoi(" -3147483648 "))
        self.assertEqual(-2147483648, s.myAtoi(" -4147483648 "))
        self.assertEqual(-2147483648, s.myAtoi("-6147483648"))
        self.assertEqual(-2147483648, s.myAtoi("-91283472332"))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()