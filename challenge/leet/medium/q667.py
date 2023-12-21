import unittest
from typing import List


class Solution_timeexceed:
    res = []
    maxdff = 0

    def constructArray(self, n: int, k: int) -> List[int]:
        kbuf = dict()
        def updatek(diff: int):
            '''
            return: false for new k not allowed
            '''
            if diff in kbuf:
                ref = kbuf[diff]
                kbuf.update({diff: ref+1})
                return False # k < n , to find new k asap
            elif len(kbuf) < k:
                kbuf.update({diff: 1})
                self.maxdff = max(self.maxdff, diff)
                return True
            else:
                return False

        def removek(diff: int):
            if diff in kbuf:
                ref = kbuf[diff]
                if ref <= 1:
                    del kbuf[diff]
                    if self.maxdff == diff:
                        self.maxdff = max(kbuf.keys()) if len(kbuf) > 0 else 0
                else:
                    kbuf.update({diff: ref - 1})


        def countArr(nums: [int], depth: int, lastv: int):
            if n == depth and len(kbuf) == k:
                return True

            if len(nums) > 1 and nums[-1] - nums[0] < self.maxdff:
                return
            for x, v in enumerate(nums):
                diff = abs(v - lastv)
                if depth == 0 or updatek(diff):
                    if countArr(nums[:x] + nums[x + 1:], depth + 1, v):
                        self.res.insert(0, nums[x])
                        return True
                if depth != 0:
                    removek(diff)

        self.res = []
        kbuf = dict()
        nums = [i for i in range(1, n + 1)]
        countArr(nums, 0, nums[0])
        return self.res


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = []
        def constk1(n0, n1):
            while n0 <= n1:
                res.append(n0)
                n0 += 1
        def constk2(n0, n1, ki):
            if ki == 1:
                return constk1(n0, n1)
            elif ki % 2 == 0:
                res.append(n1)
                constk2(n0, n1-1, ki-1)
            else:
                res.append(n0)
                constk2(n0+1, n1, ki-1)

        constk2(1, n, k)
        return res


class MyTestCase(unittest.TestCase):
    def test_q667(self):
        s = Solution()
        self.assertEqual([1, 10, 2, 9, 3, 8, 4, 7, 5, 6], s.constructArray(10, 9))
        self.assertEqual([1, 2, 3], s.constructArray(3, 1))
        self.assertEqual([3, 1, 2], s.constructArray(3, 2))


if __name__ == '__main__':
    unittest.main()
