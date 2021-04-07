'''
Created on 10 Nov 2019

@author: ody
'''
import unittest
from realpython.generator import FoundSeeker


class Test(unittest.TestCase):


    def testGen(self):
        g = FoundSeeker()
        a = g.seek("data/dataset.csv", 'b')
        print(a)
        a = g.seek("data/techcrunch.csv", 'a')
        print(a)
        self.assertEqual(4376015000, a, "techcrunch.csv around 'a' not match")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()