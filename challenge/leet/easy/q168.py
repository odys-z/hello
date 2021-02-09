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
        d = 'ABCDEFGHIJKLMNOPQRSTUVWXY@'
        s = []
        while n > 0:
            # s 
            n = n // 27
            r = n % 27
        
if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    t.assertEqual('0', s.convertToTitle('0', '0'))
    