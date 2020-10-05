import unittest

from conv64 import conv_64

class Test(unittest.TestCase):
    def ex1(self):
        self.assertEqual('0', conv_64('0'))
        self.assertEqual('1', conv_64('1'))
        self.assertEqual('A', conv_64('10'))
        self.assertEqual('Z', conv_64('35'))
        self.assertEqual('a', conv_64('36'))
        self.assertEqual('z', conv_64('61'))
        self.assertEqual('+', conv_64('62'))
        self.assertEqual('-', conv_64('63'))

        self.assertEqual('10', conv_64('64'))
        self.assertEqual('100', conv_64(str(64 * 64)))
        self.assertEqual('201', conv_64(str(64 * 64 * 2 + 1)))
        self.assertEqual('1001', conv_64(str(64 * 64 * 64 + 1)))

t = Test()
t.ex1()
print('Test finished successfully!')
