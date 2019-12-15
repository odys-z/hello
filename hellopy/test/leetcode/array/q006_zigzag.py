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
    v = 0,    1            2        ...    l + (k-2) / (k-1)
u=0    0    [ ]            2(k-1)
u=1    1    2(k-1) + k-2
    
            k-1 + 1
u=k-1  [ ]  k-1 + 0
    '''
    def convert(self, s: str, k: int) -> str:
        return "PAHNAPLSIIGYIR"
        

class Test(unittest.TestCase):


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()