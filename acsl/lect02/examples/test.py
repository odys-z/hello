import unittest

from jr2019_contest1 import Solution

class Test(unittest.TestCase):
    def testNumTrans(self):
        s = Solution()
        self.assertEqual('7145010', s.numTrans('7145032 2 8'))
        self.assertEqual('1540400', s.numTrans('1540670 3 54'))

t = Test()
t.testNumTrans()
