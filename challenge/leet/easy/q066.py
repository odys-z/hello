import unittest
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c, i = 1, len(digits) - 1;
        while c > 0 and 0 <= i:
            c, digits[i] = (c + digits[i]) // 10, (c + digits[i]) % 10
            i -= 1

        if c > 0:
            digits.insert(0, c)
        return digits


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()
        self.assertEqual([1,0], s.plusOne([9]))
        self.assertEqual([1,2,4], s.plusOne([1,2,3]))


if __name__ == '__main__':
    unittest.main()
