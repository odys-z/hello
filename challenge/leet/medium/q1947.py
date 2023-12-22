import unittest
from datetime import datetime
from functools import cache
from heapq import heapify, heappop, heappush
from typing import List


class Dijkstra():
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        s, m, n = len(students), len(mentors), len(mentors[0])

        def haming(studx, mentx):
            d = 0
            for i in range(n):
                d += 1 if students[studx][i] != mentors[mentx][i] else 0
            return d

        dist = [list([haming(sx, mx) for sx in range(s)]) for mx in range(m)]

        hq = [(0, 0, [0] * m)]  # cost, student, mentor state
        heapify(hq)
        while len(hq) > 0:
            cost, studx, ments = heappop(hq)
            if studx == m:
                return m * n - cost

            for i in range(m):
                if ments[i] == 1: continue
                costxm = cost + dist[i][studx]
                menstat = list(ments)
                menstat[i] = 1
                heappush(hq, (costxm, studx + 1, menstat))
        return m * n


class Solution1():
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m, n = len(mentors), len(mentors[0])

        def sumsim(studx, mentx):
            x = 0
            for s, m in zip(students[studx], mentors[mentx]):
                x += 1 if s == m else 0
            return x

        dist = [list([sumsim(sx, mx) for sx in range(m)]) for mx in range(m)]
        colvisit = [False for _ in range(m)]

        def dfs(r, similar):
            for c in range(m):
                if colvisit[c]: continue

                colvisit[c] = True
                self.maxsim = max(self.maxsim, similar + dist[r][c])
                dfs(r + 1, similar + dist[r][c])
                colvisit[c] = False

        self.maxsim = 0
        dfs(0, 0)
        return self.maxsim


class Solution2():
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m, n = len(mentors), len(mentors[0])

        def sumsim(studx, mentx):
            x = 0
            for s, m in zip(students[studx], mentors[mentx]):
                x += 1 if s == m else 0
            return x

        dist = [list([sumsim(sx, mx) for sx in range(m)]) for mx in range(m)]

        def dfs(colvisit, r, similar):
            if r < 0: return
            for c in range(m):
                bit = 1 << c
                # print(f"{colvisit: b} {r},{c} : {colvisit & bit:b}")
                if colvisit & bit == 0:
                    self.maxsim = max(self.maxsim, similar + dist[r][c])
                    dfs(colvisit | bit, r - 1, similar + dist[r][c])
                    print(f"     {colvisit | bit:b} {r},{c} : sim {dist[r][c]} -> {self.maxsim}")

        self.maxsim = 0
        colvisit = 1 << m
        dfs(colvisit, m-1, 0)
        return self.maxsim


class Solution3:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m = len(students)

        score = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                score[i][j] = sum(x == y for x, y in zip(students[i], mentors[j]))

        @cache
        def fn(mask, j):
            if j < 0: return 0
            """Return max score of assigning students in mask to first j mentors."""
            ans = 0
            for i in range(m):
                # print(f"{mask: b} {j},{i} : {mask & (1 << i):b}")
                if not mask & (1 << i):
                    ans = max(ans, fn(mask ^ (1 << i), j - 1) + score[i][j])
                    print(f"     {mask ^ (1 << i):b} {j},{i} : sim {score[i][j]} -> {ans}")
            return ans

        return fn(1 << m, m - 1)


class MyTestCase(unittest.TestCase):
    def test_q1947(self):
        def q1947(s):
            self.assertEqual(8, s.maxCompatibilitySum([[1, 1, 0], [1, 0, 1], [0, 0, 1]],
                                                      [[1, 0, 0], [0, 0, 1], [1, 1, 0]]))
            self.assertEqual(0, s.maxCompatibilitySum([[0, 0], [0, 0], [0, 0]], [[1, 1], [1, 1], [1, 1]]))

            self.assertEqual(19, s.maxCompatibilitySum(
                [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]],
                [[1, 0, 1, 1, 1], [1, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 0, 1, 1]]))

            self.assertEqual(1, s.maxCompatibilitySum([[0]], [[0]]))

            self.assertEqual(58, s.maxCompatibilitySum(
                [[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1]],
                [[0, 1, 1, 1, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1, 1, 1],
                 [1, 1, 1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 0, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1]]))

            self.assertEqual(19, s.maxCompatibilitySum(
                [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]],
                [[1, 0, 1, 1, 1], [1, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 0, 1, 1]]))

            self.assertEqual(40, s.maxCompatibilitySum(
                [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]],
                [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]))

            self.assertEqual(48, s.maxCompatibilitySum(
                [[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1]],
                [[0, 0, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1],
                 [0, 0, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1],
                 [0, 0, 0, 1, 1, 1, 1, 1]]))

            self.assertEqual(55, s.maxCompatibilitySum(
                [[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1]],
                [[0, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1],
                 [0, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1],
                 [0, 0, 1, 1, 1, 1, 1, 1]]))

            self.assertEqual(1, s.maxCompatibilitySum(
                [[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1]],
                [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0]]))

        # t = datetime.now()
        # q1947(Solution1())
        # print("s1", datetime.now() - t)

        t = datetime.now()
        q1947(Solution2())
        print("s2", datetime.now() - t)

        t = datetime.now()
        q1947(Solution3())
        print("s3", datetime.now() - t)

        # t = datetime.now()
        # q1947(Dijkstra())
        # print("Dijkstra", datetime.now() - t)


if __name__ == '__main__':
    unittest.main()
