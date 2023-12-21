import unittest
from functools import cache
from heapq import heapify, heappop, heappush
from typing import List


class Solution():
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


class Solution2():
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m, n = len(mentors), len(mentors[0])

        def sumsim(studx, mentx):
            s = 0
            for mx in range(n):
                s += 1 if students[studx][mx] == mentors[mentx][mx] else 0
            return s

        dist = [list([sumsim(sx, mx) for sx in range(m)]) for mx in range(m)]
        colvisit = [False for _ in range(m)]

        def dfs(r, similar):
            if r >= m:
                return

            for c in range(m):
                if colvisit[c]: continue

                colvisit[c] = True
                self.maxsim = max(self.maxsim, similar + dist[r][c])
                dfs(r+1, similar + dist[r][c])
                colvisit[c] = False

            return

        self.maxsim = 0
        dfs(0, 0)
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
            """Return max score of assigning students in mask to first j mentors."""
            ans = 0
            for i in range(m):
                if not mask & (1 << i):
                    ans = max(ans, fn(mask ^ (1 << i), j - 1) + score[i][j])
            return ans

        return fn(1 << m, m - 1)


class MyTestCase(unittest.TestCase):
    def test_q1947(self):
        s = Solution3()
        self.assertEqual(8, s.maxCompatibilitySum([[1, 1, 0], [1, 0, 1], [0, 0, 1]], [[1, 0, 0], [0, 0, 1], [1, 1, 0]]))
        self.assertEqual(0, s.maxCompatibilitySum([[0, 0], [0, 0], [0, 0]], [[1, 1], [1, 1], [1, 1]]))

'''
19
[[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
mentors =
[[1,0,1,1,1],[1,0,1,1,1],[0,0,1,1,1],[0,0,1,1,1],[0,0,1,1,1],[0,0,0,1,1]]

1
[[0]]
mentors =
[[0]]

[[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
mentors =
[[1,0,1,1,1],[1,0,1,1,1],[0,0,1,1,1],[0,0,1,1,1],[0,0,1,1,1],[0,0,0,1,1]]
Output
19

[[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
mentors =
[[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
Output
40

[[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1]]
mentors =
[[0,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,1,1,1,1,1,1]]
Output
55

[[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1]]
mentors =
[[0,0,1,1,1,1,1,1],[0,0,1,1,1,1,1,1],[0,0,1,1,1,1,1,1],[0,0,1,1,1,1,1,1],[0,0,1,1,1,1,1,1],[0,0,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,1,1,1,1,1]]
Output
48

[[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1]]
mentors =
[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0]]
Output
1

[[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1]]
mentors =
[[0,1,1,1,1,1,1,1],[1,0,1,1,1,1,1,1],[1,1,0,1,1,1,1,1],[1,1,0,1,1,1,1,1],[1,1,1,0,1,1,1,1],[1,1,1,1,0,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1]]
Output
58


'''

if __name__ == '__main__':
    unittest.main()
