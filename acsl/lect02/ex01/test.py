import unittest

from parse_color import parseColor

class Test(unittest.TestCase):
    def ex1(self):
        self.assertEqual((0, 0, 0), parseColor('000000'))
        self.assertEqual((0, 0, 0), parseColor('1'))
        self.assertEqual((0, 0, 0), parseColor('#000000'))
        self.assertEqual((1, 2, 3), parseColor('#010203'))

t = Test()
t.ex1()
print('Test finished successfully!')
