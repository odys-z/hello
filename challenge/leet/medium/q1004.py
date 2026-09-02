'''
1004. Max Consecutive Ones III
https://leetcode.com/problems/max-consecutive-ones-iii/description/
'''
from unittest import TestCase
from typing import List, cast

class Solution:
    '''
    [0,0,1,1,0,0,1,1,1,0,1,0,0,0,0,0,1]
    [-2, 2,  -2, 3,   -1,1,-5,       1] k=4
    [-2, 2]  k=2, max=4
    [-2, 2, -2, 3]   k=0, max=9
    [-1, 2, -2, 3, -1, 1]  k=0, max=10
        [2, -2, 3, -1, 1, -1]  k=0, max=10
                         [-4, 1]  k=0, max=10

    [1,0,0,1,1,0,0,1,1,1,0,1,0,0,0,0,0,1]
    [1,-2, 2,  -2, 3,   -1,1,-5,       1] k=4
    [1,-2]  k=2, max=3
    [1,-2, 2]  k=2, max=5
    [1,-2, 2,-2,3]  k=0, max=9
    '''

    def longestOnes(self, nums: List[int], k: int) -> int:
        nix: List[int] = [0]
        _0s, _1s, _n = 0, 0, nums[0]
        for n in nums:
            if _n != n:
                if _n == 0:
                    nix.append(-_0s)
                else:
                    nix.append(_1s)
                _0s, _1s, _n = 0, 0, n

            if n == 0:
                _0s, _1s = _0s + 1, 0
            else:
                _0s, _1s = 0, _1s + 1
        else:
            if _n == 0:
                nix.append(-_0s)
            else:
                nix.append(_1s)

        cover, mxlen, ilen, l, r = k, 0, 0, 0, 1

        if nix[r] < 0:
            l, r = r, r + 1

        nix[l] = - min(k, -nix[l])  # spent to the left 0s
        cover = k + nix[l]
        ilen = -nix[l]
        mxlen = max(ilen, mxlen)

        while r < len(nix):
            iv:int = nix[r]

            if iv > 0:
                ilen = ilen + iv
                mxlen = max(ilen, mxlen)
                r = r+1
            else: #
                if -iv <= cover:
                    ilen = ilen - iv
                    mxlen = max(ilen, mxlen)
                    cover = cover + iv
                    r = r+1
                elif -iv > cover and -iv <= cover - nix[l]:
                    left = -nix[l] + cover + iv # left over to the left after spent all budgets
                    ilen = ilen + cover
                    mxlen = max(mxlen, ilen)
                    nix[l], cover = -left, 0
                    r = r+1
                    if nix[l] == 0:
                        l = l+1
                else: # otherwise the gap cannot be covered
                    mxlen = max(ilen + cover, mxlen)

                    while nix[l] >=0 and l < r:
                        # l = l+1
                        l, ilen = l + 1, ilen - nix[l]
                    if l < r:
                        if nix[l] >= 0:
                            print("EEEEEEEEEEEEEEEEEEEEEEE")
                        nix[l], cover, l, ilen = 0, cover - nix[l], l + 1, ilen + nix[l]
                    else: # l == r and nix[r] < -k
                        cover = 0
                        r = r+1
                        ilen = k
                        nix[l] = -k # spent all k here (left 0s)
                        mxlen = max(ilen, mxlen)
        return mxlen


if __name__ == "__main__":
    t = TestCase()
    s = Solution()

    t.assertEqual(2, s.longestOnes( [1, 0, 0], 1))
    t.assertEqual(2, s.longestOnes( [0, 1, 0], 1))
    t.assertEqual(3, s.longestOnes( [0, 1, 0], 2))
    t.assertEqual(3, s.longestOnes( [0, 0, 1, 0], 2))
    t.assertEqual(3, s.longestOnes( [0, 0, 0, 1, 0], 2))
    t.assertEqual(3, s.longestOnes( [0, 1, 0, 1, 0], 1))
    t.assertEqual(3, s.longestOnes( [1, 0, 1, 0, 1, 0], 1))

    t.assertEqual(10, s.longestOnes(
        [1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0], 3))
    t.assertEqual(5, s.longestOnes(
        [1,1,1,0,0,0,1,1,1,1,0], 1))
    t.assertEqual(6, s.longestOnes(
        [1,1,1,0,0,0,1,1,1,1,0], 2))
    t.assertEqual(10, s.longestOnes(
        [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3))
    t.assertEqual(10, s.longestOnes(
        [0,0,1,1,0,0,1,1,1,0,1,0,0,0,0,0,1], k = 4))

    t.assertEqual(11, s.longestOnes(
        [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 5))
    t.assertEqual(11, s.longestOnes(
        [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 4))
    t.assertEqual(10, s.longestOnes(
        [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 3))
    t.assertEqual(10, s.longestOnes(
        [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0], 3))

    # pip install anson.py3 semantics.py3
    from semanticshare.io.oz.leetcode import TestData # since 0.6.1
    from anson.io.odysz.anson import Anson

    cases = cast(TestData, Anson.from_file('q1004.leetest.json'))
    for cas in cases.cases:
        print(cas.name)
        t.assertEqual(cas.expect, s.longestOnes(cas.nums, cas.i_v[0]))

    print('OK!')