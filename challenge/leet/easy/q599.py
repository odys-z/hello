import unittest
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dp = dict(map(lambda x: (x[1], x[0]), enumerate(list1)))
        res, low = [], float('inf')
        for x, v in enumerate(list2):
            if v in dp:
                lo = x + dp[v]
                if lo < low:
                    low = lo
                    res = [v]
                elif lo == low:
                    res.append(v)
        return res


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()

        self.assertEqual(["Shogun"],
           s.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],
                            ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))


if __name__ == '__main__':
    unittest.main()
