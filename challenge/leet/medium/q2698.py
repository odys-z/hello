'''
2698. Find the Punishment Number of an Integer
https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/
'''
import unittest


class Solution:
    def punishmentNumber(self, n: int) -> int:
        dp = []
        total, punished = 0, 0
        digits = []

        def punish(i: int, depth: int, subsum: int):
            nonlocal punished

            if depth >= len(digits):
                if subsum == i:
                    punished += i * i
                    raise Exception(i * i)
                return

            subi = 0
            for j in range(depth, len(digits)):
                subi = subi * 10 + int(digits[j])
                if subi <= n:
                    punish(i, j + 1, subi + subsum)
                elif subsum + subi > n:
                    break

        for i in range(1, n + 1):
            digits = []
            for x in str(int(i ** 2)):
                digits.append(int(x))

            try:
                punish(i, 0, 0)
            except Exception as e:
                total += punished
                punished = 0
        return total


class Solution2:

    dp = [
         (1, 1), (9, 82), (10, 182), (36, 1478), (45, 3503), (55, 6528), (82, 13252), (91, 21533), (99, 31334),
         (100, 41334), (235, 96559), (297, 184768), (369, 320929), (370, 457829), (379, 601470), (414, 772866),
         (657, 1204515), (675, 1660140), (703, 2154349), (756, 2725885), (792, 3353149), (909, 4179430), (918, 5022154),
         (945, 5915179), (964, 6844475), (990, 7824575), (991, 8806656), (999, 9804657), (1000, 10804657)]

    '''
    def __int__(self):
        self.dp = []
        self.gendp()
        print(self.dp)
    '''


    def gendp(self):
        punished = 0
        def punish(i: int, depth: int, subsum: int, digits: [int]):
            nonlocal punished

            if depth >= len(digits):
                if subsum == i:
                    punished += i * i
                    raise Exception(i * i)
                return

            subi = 0
            for j in range(depth, len(digits)):
                subi = subi * 10 + int(digits[j])
                if subi <= i:
                    punish(i, j + 1, subi + subsum, digits)
                elif subsum + subi > i:
                    break

        total = 0
        for i in range(1, 1000 + 1):
            digits = []
            for x in str(int(i ** 2)):
                digits.append(int(x))

            try:
                punish(i, 0, 0, digits)
            except Exception as e:
                total += punished
                punished = 0
                self.dp.append((i, total))

    def punishmentNumber(self, n: int) -> int:
        l, r, m = 0, len(self.dp) - 1, len(self.dp) // 2
        while l < r:
            if n < self.dp[m][0]:
                r = m - 1
            else:
                l = m
            m = (l + r + 1) // 2

        return self.dp[l][1]


class MyTestCase(unittest.TestCase):
    def test_q526(self):
        s = Solution2()
        # s.__int__()

        self.assertEqual(1, s.punishmentNumber(1))
        self.assertEqual(82, s.punishmentNumber(9))
        self.assertEqual(182, s.punishmentNumber(10))
        self.assertEqual(1478, s.punishmentNumber(36))
        self.assertEqual(3503, s.punishmentNumber(45))
        self.assertEqual(6528, s.punishmentNumber(55))
        self.assertEqual(13252, s.punishmentNumber(82))
        self.assertEqual(21533, s.punishmentNumber(91))
        self.assertEqual(31334, s.punishmentNumber(99))
        self.assertEqual(41334, s.punishmentNumber(100))
        self.assertEqual(96559, s.punishmentNumber(235))
        self.assertEqual(184768, s.punishmentNumber(297))
        self.assertEqual(320929, s.punishmentNumber(369))
        self.assertEqual(457829, s.punishmentNumber(370))
        self.assertEqual(601470, s.punishmentNumber(379))
        self.assertEqual(772866, s.punishmentNumber(414))
        self.assertEqual(1204515, s.punishmentNumber(657))
        self.assertEqual(2154349, s.punishmentNumber(703))
        self.assertEqual(2725885, s.punishmentNumber(756))
        self.assertEqual(3353149, s.punishmentNumber(792))
        self.assertEqual(4179430, s.punishmentNumber(909))
        self.assertEqual(5022154, s.punishmentNumber(918))
        self.assertEqual(5915179, s.punishmentNumber(945))
        self.assertEqual(6844475, s.punishmentNumber(964))
        self.assertEqual(7824575, s.punishmentNumber(990))
        self.assertEqual(8806656, s.punishmentNumber(991))
        self.assertEqual(9804657, s.punishmentNumber(999))
        self.assertEqual(10804657, s.punishmentNumber(1000))


if __name__ == "__main__":
    unittest.main()
