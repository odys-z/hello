'''
Created on 10 Nov 2019

@author: ody
'''
import unittest
from realpython.itool import ITool

class Test(unittest.TestCase):


    def testIt(self):
        i = ITool()
        # i.simple_acc(5)
        i.topKFreq([1, 3, 5, 1, 22, 2], 3)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()