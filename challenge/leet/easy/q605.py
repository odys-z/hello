import unittest
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            return n == 0 or flowerbed[0] == 0

        res, cnt = 0, 2 if flowerbed[0] == 0 else 0
        for plot in flowerbed[1:]:
            if plot > 0:
                res += (cnt - 1) // 2
                cnt = 0
            else:
                cnt += 1

        res += cnt // 2
        return res >= n


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()
        self.assertEqual(True, s.canPlaceFlowers([1,0,1,0,0], 1))  # add assertion here


if __name__ == '__main__':
    unittest.main()
