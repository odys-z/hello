'''
12. Integer to Roman
https://leetcode.com/problems/integer-to-roman/

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:
Input: 3 Output: "III"

Example 2:
Input: 4 Output: "IV" Example 3:
Input: 9 Output: "IX" Example 4:
Input: 58 Output: "LVIII" Explanation: L = 50, V = 5, III = 3.

Example 5:
Input: 1994 Output: "MCMXCIV" Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

@see: Java Solution: leetcode.tree.q012_int2roman.*

Created on 30 Nov 2019

@author: odys-z@github.com
'''
import unittest

class SolutionBs:
    def intToRoman(self, num: int) -> str:
        romans = ''
        maxr = len(nums) - 1
        while num > 0:
            ix, maxr = bins(num, 0, maxr)
            num -= nums[ix]
            romans += roms[ix]
        return romans

#         0     1    2     3    4    5    6     7    8     9    10    11   12
nums = [  1,    4,   5,    9,  10,   40,  50,   90, 100,  400, 500,  900, 1000 ]
roms = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']

def bins(target, l, r):
    if l == r:
        return l, r

    # if target in between n[l : l+1], l is the ix
    # so use ceiling?
    m = (l + r + 1) // 2

    if nums[m] == target:
        return m, r
    elif target < nums[m]:
        return bins(target, l, m - 1)
    else: return bins(target, m, r) # m is ceilinged, m + 1 may leak some value

class Solution28ms:
    ''' actually 52ms '''
    def intToRoman(self, num: int) -> str:
        roman_num = ''
        while(num > 999):
            num -= 1000
            roman_num += 'M'
        while(num > 899):
            num -= 900
            roman_num += 'CM'
        while(num > 499):
            num -= 500
            roman_num += 'D'
        while(num > 399):
            num -= 400
            roman_num += 'CD'
        while(num > 99):
            num -= 100
            roman_num += 'C'
        while(num > 89):
            num -= 90
            roman_num += 'XC'
        while(num > 49):
            num -= 50
            roman_num += 'L'
        while(num > 39):
            num -= 40
            roman_num += 'XL'
        while(num > 9):
            num -= 10
            roman_num += 'X'
        while(num > 8):
            num -= 9
            roman_num += 'IX'
        while(num > 4):
            num -= 5
            roman_num += 'V'
        while(num > 3):
            num -= 4
            roman_num += 'IV'
        while(num > 0):
            num -= 1
            roman_num += 'I'
        return roman_num
    
rnums = [1000, 900,  500, 400,  100, 90,   50,  40,   10,  9,    5,   4,    1]
#       ['M',  'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'x', 'IX', 'V', 'IV', 'I']
rroms = [['M', 'MM', 'MMM'],
         ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
         ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
         ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        ]

class SolutionWeightable():
    def intToRoman(self, num: int) -> str:
        romans = []
        mod = 1000
        crank = -1 # rank compliment
        while num > 0:
            k = num // mod
            num %= mod
            mod //= 10
            crank += 1
            if k > 0:
                romans.append(rroms[crank][k - 1])

        return ''.join(romans)

class SolutionRank():
    def intToRoman(self, num: int) -> str:
        romans = '' ## str '+': 48ms; ''.join(romans:List[str]): 52ms
        w = num // 1000
        if w > 0:
            romans = rroms[0][w - 1]
        num %= 1000
        w = num // 100
        if w > 0:
            romans += rroms[1][w - 1]
        num %= 100
        w = num // 10
        if w > 0:
            romans += rroms[2][w - 1]
        num %= 10
        if num > 0:
            romans += rroms[3][num - 1]

        return romans



class Test(unittest.TestCase):

    def test012(self):
        # s = SolutionBs()
        # s = Solution28ms()
#         s = SolutionWeightable()
        s = SolutionRank()
        self.assertEqual("I", s.intToRoman(1));
        self.assertEqual("III", s.intToRoman(3));
        self.assertEqual("IV", s.intToRoman(4));
        self.assertEqual("V", s.intToRoman(5));
        self.assertEqual("VI", s.intToRoman(6));
        self.assertEqual("IX", s.intToRoman(9));
        self.assertEqual("X", s.intToRoman(10));
        self.assertEqual("XI", s.intToRoman(11));
        self.assertEqual("XIV", s.intToRoman(14));
        self.assertEqual("XV", s.intToRoman(15));
        self.assertEqual("XVI", s.intToRoman(16));
        self.assertEqual("XIX", s.intToRoman(19));
        self.assertEqual("XX", s.intToRoman(20));
        self.assertEqual("XXIV", s.intToRoman(24));
        self.assertEqual("XXXIX", s.intToRoman(39));
        self.assertEqual("LVIII", s.intToRoman(58));
        self.assertEqual("XCIX", s.intToRoman(99));
        self.assertEqual("C", s.intToRoman(100));
        self.assertEqual("CI", s.intToRoman(101));
        self.assertEqual("CCI", s.intToRoman(201));
        self.assertEqual("CD", s.intToRoman(400));
        self.assertEqual("CDI", s.intToRoman(401));
        self.assertEqual("DCCCLXXVI", s.intToRoman(876));
        self.assertEqual("CMLXXXVII", s.intToRoman(987));
        self.assertEqual("MMMCDXXXII", s.intToRoman(3432));
        self.assertEqual("MMMCDXXXIX", s.intToRoman(3439));
        self.assertEqual("MMMCDXCIX", s.intToRoman(3499));
        self.assertEqual("M", s.intToRoman(1000));
        self.assertEqual("MI", s.intToRoman(1001));
        self.assertEqual("MCMXCIV", s.intToRoman(1994));

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()