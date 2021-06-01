'''
67. Add Binary
https://leetcode.com/problems/add-binary/

Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
 
Constraints:
1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

Created on 8 Feb 2021

@author: odys-z@github.com
'''

from unittest import TestCase

class Solution:
    # 27.75% 
    def addBinary(self, a: str, b: str) -> str:
        if len(b) > len(a):
            a, b = b, a # a > b
        c, res = 0, []
        for x in range(len(a)):
            a_, b_ = int(a[-x - 1]), int(b[-x - 1]) if x < len(b) else 0
            res.insert(0, str((a_ + b_ + c) % 2))
            c = (a_ + b_ + c) // 2
        if c > 0: # can only be 1
            res.insert(0, str(c))
        return ''.join(res)

if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    t.assertEqual('0', s.addBinary('0', '0'))
    t.assertEqual('1', s.addBinary('1', '0'))
    t.assertEqual('10', s.addBinary('1', '1'))
    t.assertEqual('100', s.addBinary('11', '1'))
    t.assertEqual('10101', s.addBinary('1010', '1011'))
    
    print('OK!')
