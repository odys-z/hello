import unittest

from q1404 import Solution

class Test(unittest.TestCase):
    def q1404(self):
        s = Solution()
        self.assertEqual(0, s.numSteps('1'))
        self.assertTrue(5 == s.numSteps('1111'))

t = Test()
t.q1404()
