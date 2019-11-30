'''
Created on 27 Nov 2019

@author: odys-z@github.com
'''
import unittest
from ext.heapk import Heapk


class Test(unittest.TestCase):


    def testHeapk(self):
        h = Heapk([1, 1, 3, 5])
        h.push(4)
        self.assertEqual(1, h.pop())
        self.assertEqual(1, h.pop())
        self.assertEqual(3, h.pop())
        self.assertEqual(4, h.pop())
        self.assertEqual(5, h.pop())
        try:
            self.assertEqual(None, h.pop())
            self.fail("Can't pop")
        except IndexError:
            pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testHeapk']
    unittest.main()