'''
Created on 16 Nov 2019

@author: ody
'''
import unittest

class Solution:
    '''
        (()(
        ))())
    '''
    def minAddToMakeValid(self, S: str) -> int:
        res = 0
        balance = 0
        for p in S:
            if p == ')':
                if balance > 0 :
                    balance -= 1
                elif balance == 0:
                    res += 1
            else: # '('
                balance += 1
        return res + balance

class Test(unittest.TestCase):


    def testName(self):
        s = Solution()
        self.assertEqual(1, s.minAddToMakeValid('('))
        self.assertEqual(1, s.minAddToMakeValid(')'))
        self.assertEqual(1, s.minAddToMakeValid(')()'))
        self.assertEqual(2, s.minAddToMakeValid('))'))
        self.assertEqual(2, s.minAddToMakeValid(')('))
        self.assertEqual(2, s.minAddToMakeValid('(('))
        self.assertEqual(2, s.minAddToMakeValid('(()('))
        self.assertEqual(2, s.minAddToMakeValid(')()('))
        self.assertEqual(3, s.minAddToMakeValid('((('))
        self.assertEqual(4, s.minAddToMakeValid(')((('))
        self.assertEqual(14,s.minAddToMakeValid("())())())(())())())((())()))())())))()))())())"))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()