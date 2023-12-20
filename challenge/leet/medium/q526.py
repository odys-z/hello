import unittest
from itertools import permutations

# 1: 1, 2: 2, 3: 3, ...
dp0 = [1, 1, 2, 3, 8, 10, 36, 41, 132, 250, 700, 750, 4010, 4237, 10680, 24679, 87328]
dp = [0, 1, 2, 3]


class Solution:
    def countArrangement(self, n: int) -> int:

        self.res = 0
        nums = [i for i in range(1, n + 1)]

        def dfs(nums: list, i: int = 1):
            if i == n + 1:
                self.res += 1
                return

            for j, num in enumerate(nums):
                if not (num % i and i % num):
                    dfs(nums[:j] + nums[j + 1:], i + 1)

        dfs(nums)
        return self.res

class Solution2:
    res = 0

    def countArrangement(self, n: int) -> int:

        def countArr(nums: [int], depth: int):
            if n + 1 == depth:
                self.res += 1
                return

            # for x in range(len(nums) - 1, -1, -1):
            # for x in range(len(nums)):
            for x, v in enumerate(nums):
                # v = nums[x]    - Why this single access will increase 8.1 seconds to 9.4 seconds?
                if v % depth == 0 or depth % v == 0:
                    countArr(nums[:x] + nums[x + 1:], depth + 1)

        nums = [i for i in range(1, n+1)]
        self.res = 0
        countArr(nums, 1)
        return self.res


class MyTestCase(unittest.TestCase):
    def test_q526(self):
        s = Solution2()
        self.assertEqual(3, s.countArrangement(3))
        self.assertEqual(1, s.countArrangement(1))
        self.assertEqual(2, s.countArrangement(2))
        self.assertEqual(8, s.countArrangement(4))
        self.assertEqual(10, s.countArrangement(5))
        self.assertEqual(36, s.countArrangement(6))
        self.assertEqual(41, s.countArrangement(7))
        self.assertEqual(132, s.countArrangement(8))
        self.assertEqual(250, s.countArrangement(9))
        self.assertEqual(700, s.countArrangement(10))
        self.assertEqual(750, s.countArrangement(11))
        self.assertEqual(4010, s.countArrangement(12))
        self.assertEqual(4237, s.countArrangement(13))
        self.assertEqual(10680, s.countArrangement(14))
        self.assertEqual(24679, s.countArrangement(15))
        self.assertEqual(87328, s.countArrangement(16))


if __name__ == '__main__':
    unittest.main()
