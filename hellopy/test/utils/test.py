'''
Created on 22 Dec 2019

@author: ody
'''
import unittest
from utils.Assrt import Eq, AssertErr, XdArrParser

class Test(unittest.TestCase):

    def testArrEq(self):
        eq = Eq()
        try: 
            eq.int2dArr([[]], [[1]])
            self.fail("Error not checked")
        except AssertErr as e:
            print(e)
        
        try: 
            eq.int2dArr([[]], [])
            self.fail("Error not checked")
        except AssertErr as e:
            print(e)
        
        try:
            eq.int2dArr([[1]], [[]])
            self.fail("Error not checked")
        except AssertErr as e:
            # [] not in [[1]]
            print(e)

        try:
            eq.int2dArr([[2]], [[1]])
            self.fail("Error not checked")
        except AssertErr as e:
            print(e)

        try:
            eq.int2dArr([[2], [1]], [[1], [3]])
            self.fail("Error not checked")
        except AssertErr as e:
            print(e)

        try:
            eq.int2dArr([[1]], [[1, 2]])
            self.fail("Error not checked")
        except AssertErr as e:
            print(e)

        try:
            eq.int2dArr([[1, 2], [2, 1], [1, 3, 5]], [[2, 1], [1, 2], [3, 1, 6]])
            self.fail("Error not checked")
        except AssertErr as e:
            print(e)

        try:
            eq.int2dArr([[1, 2], [2, 1], [1, 3, 6], [0]], [[2, 1], [1, 2], [3, 1, 6]])
            self.fail("Error not checked")
        except AssertErr as e:
            print(e)

        try:
            eq.int2dArr([[1, 2], [2, 1], [1, 3, 6], [0]], [[2, 1], [1, 2], [3, 1, 6], [1]])
            self.fail("Error not checked")
        except AssertErr as e:
            print(e)

        eq.int2dArr([], [])
        eq.int2dArr([[]], [[]])
        eq.int2dArr([[1, 2]], [[2, 1]])
        eq.int2dArr([[1, 2], [2, 1]], [[2, 1], [1, 2]])
        eq.int2dArr([[1, 2], [2, 1], [1, 3, 4]], [[2, 1], [1, 2], [3, 1, 4]])

    def testPasrsArr(self): 
        eq = Eq()
        
        parse2d = XdArrParser(2)
        a2d = parse2d.parseInt("[[1,2],[3]]")
        print(a2d)
        eq.int2dArr([[1,2], [3]], a2d)

        a2d = parse2d.parseInt("[[1],[3]]")
        eq.int2dArr([[1], [3]], a2d)

        a2d = parse2d.parseInt("[[1],[3,1]]")
        eq.int2dArr([[1], [3,1]], a2d)

        a2d = parse2d.parseInt("[[1],[3,1]]")
        eq.int2dArr([[1], [1,3]], a2d)

        a2d = parse2d.parseInt("[[1,3],[3,1]]")
        eq.int2dArr([[1,3], [1,3]], a2d)

        a2d = parse2d.parseInt("[[1,3],[]]")
        eq.int2dArr([[1,3], []], a2d)

        a2d = parse2d.parseInt("[[],[]]")
        eq.int2dArr([[], []], a2d)

        a2d = parse2d.parseInt("[[1],[2], [3]]")
        eq.int2dArr([[1], [2], [3]], a2d)

        a2d = parse2d.parseInt("[[1], [2, 3, 4, 5, 6, 7], [3]]")
        eq.int2dArr([[1], [3], [2, 3, 4, 5, 6, 7]], a2d)

        a2d = parse2d.parseInt("[[1], [2, 3, 4, 5, 6, 7], [10, 12]]")
        eq.int2dArr([[1], [10, 12], [2, 3, 4, 5, 6, 7]], a2d)

    def testParse3d(self):
        eq = Eq()
        parse3d = XdArrParser(3)
        a3d = parse3d.parseInt("[[[1],[3,1]]]")
        print(a3d)
        eq.int2dArr([[1], [1,3]], a3d[0])

class TestFile(unittest.TestCase):
    def testAssertFile(self):
        eq = Eq()
        eq.int2dArrFile('data/case01.txt', 2)

        eq.int2dArrFile('data/case02.txt', 2)

        eq.int2dArrFile('data/case03.txt', 2)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()