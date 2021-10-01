'''
13. Roman to Integer

https://leetcode.com/problems/roman-to-integer/

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Example 4:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 
Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
'''

from unittest import TestCase

class Solution:
    '''
    99.59% 
    '''
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000, ' ': 0 }
        ix, vi = 0, 0
        s += ' '
        while ix < len(s):
            if s[ix:ix+2] in d:
                vi += d[s[ix:ix+2]]
                ix += 2
            else:
                vi += d[s[ix]]
                ix += 1
        return vi
          

if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    t.assertEqual(3, s.romanToInt('III'))
    t.assertEqual(4, s.romanToInt('IV'))
    t.assertEqual(9, s.romanToInt('IX'))
    t.assertEqual(58, s.romanToInt('LVIII'))
    t.assertEqual(1994, s.romanToInt('MCMXCIV'))
    t.assertEqual(3045, s.romanToInt('MMMXLV'))
    
    print('OK!')