'''
168. Excel Sheet Column Title
https://leetcode.com/problems/excel-sheet-column-title/

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"

Created on 8 Feb 2021

@author: odys-z@github.com
'''
from unittest import TestCase

class Solution:
    '''
    80.93%
	
    A    Z     AA    AZ  BA   ZZ      ZZZ           AAZZ
         A@          B@       AA@     AAA@          ABA@ -> AB@Z   -> AAZZ
    1    26+0        2*26     26^2+26 26^3+26^2+26  26^3+2*26^2+26

    ZZZ + 1 = 26^3+26^2+26 + 1 = AAA@ + A

    26       2*26       2*26+1  3*26        3*26+1  25*26+1  25*26+25  26^2
    A@ -> Z  B@ -> AZ   BA      C@ -> BZ    CA      YA       YY        A@@  -> YZ (Y@ + Z)
                              = BY + 1                               = YY + 1 = YZ  <==> 25 * 26 + 26
                                                                 A@A = YZ + 1 = A@@ + 2 = ZA  <==> 26^2 + 1 = (26) * 26 + 1
                                                                                                   A@A         ZA

    0 1 2 3 4 5 6 7 8 9 10                            25
    @ A B C D E F G H I J K L M N O P Q R S T U V W X Y
    Z

    26 = A@ (Z)
    '''
    def convertToTitle(self, n: int) -> str:
        d = 'ZABCDEFGHIJKLMNOPQRSTUVWXY'
        s = ''
        while n > 0:
            r = n % 26
            n = n // 26
            if r == 0: n -= 1
            s = d[r] + s
        return s

if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    t.assertEqual('A', s.convertToTitle(1))
    t.assertEqual('B', s.convertToTitle(2))
    t.assertEqual('Y', s.convertToTitle(25))
    t.assertEqual('Z', s.convertToTitle(26))
    t.assertEqual('AA', s.convertToTitle(27))
    t.assertEqual('AY', s.convertToTitle(51))
    t.assertEqual('AZ', s.convertToTitle(52))
    t.assertEqual('BA', s.convertToTitle(53))
    t.assertEqual('BZ', s.convertToTitle(53 + 25))
    t.assertEqual('ZZ', s.convertToTitle(26**2 + 26))
    t.assertEqual('ZZZ', s.convertToTitle(26**3 + 26**2 + 26))
    t.assertEqual('AAZZ', s.convertToTitle(26**3 + 2 * 26**2 + 26))

    print('OK!')
