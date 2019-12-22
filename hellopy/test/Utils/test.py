'''
Created on 22 Dec 2019

@author: ody
'''
import unittest
from test.Utils.Assrt import Eq, AssrtError


class Test(unittest.TestCase):


    def testName(self):
        eq = Eq()
        try: 
            eq.int2dArr([[]], [[1]])
            self.fail("Error not checked")
        except AssrtError as e:
            print(e)
        
        try: 
            eq.int2dArr([[]], [])
            self.fail("Error not checked")
        except AssrtError as e:
            print(e)
        
        try:
            eq.int2dArr([[1]], [[]])
            self.fail("Error not checked")
        except AssrtError as e:
            # [] not in [[1]]
            print(e)

        try:
            eq.int2dArr([[2]], [[1]])
            self.fail("Error not checked")
        except AssrtError as e:
            print(e)

        try:
            eq.int2dArr([[2], [1]], [[1], [3]])
            self.fail("Error not checked")
        except AssrtError as e:
            print(e)

        try:
            eq.int2dArr([[1]], [[1, 2]])
            self.fail("Error not checked")
        except AssrtError as e:
            print(e)

        try:
            eq.int2dArr([[1, 2], [2, 1], [1, 3, 5]], [[2, 1], [1, 2], [3, 1, 6]])
            self.fail("Error not checked")
        except AssrtError as e:
            print(e)

        try:
            eq.int2dArr([[1, 2], [2, 1], [1, 3, 6], [0]], [[2, 1], [1, 2], [3, 1, 6]])
            self.fail("Error not checked")
        except AssrtError as e:
            print(e)

        try:
            eq.int2dArr([[1, 2], [2, 1], [1, 3, 6], [0]], [[2, 1], [1, 2], [3, 1, 6], [1]])
            self.fail("Error not checked")
        except AssrtError as e:
            print(e)

        eq.int2dArr([], [])
        eq.int2dArr([[]], [[]])
        eq.int2dArr([[1, 2]], [[2, 1]])
        eq.int2dArr([[1, 2], [2, 1]], [[2, 1], [1, 2]])
        eq.int2dArr([[1, 2], [2, 1], [1, 3, 4]], [[2, 1], [1, 2], [3, 1, 4]])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()