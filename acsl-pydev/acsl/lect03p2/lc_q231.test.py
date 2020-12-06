import unittest

from lc_q231 import Solution, Solution2, Solution3

class Test(unittest.TestCase):
    def q231(self, s):
        self.assertFalse(s.isPowerOfTwo(0))

        self.assertFalse(s.isPowerOfTwo(9))

        for i in range(32):
            self.assertTrue(s.isPowerOfTwo(2 ** i))
            self.assertFalse(s.isPowerOfTwo( -(2 ** i) ))

            if i > 1:
                self.assertFalse(s.isPowerOfTwo( 2 ** i + 1 ))
                self.assertFalse(s.isPowerOfTwo( 2 ** i - 1 ))
                self.assertFalse(s.isPowerOfTwo( 2 ** i + 3 ))

        self.assertFalse(s.isPowerOfTwo( -(2 ** 32) ))

        print('OK!')

t = Test()
s = Solution()
t.q231(s)

s = Solution2()
t.q231(s)

s = Solution3()
t.q231(s)
