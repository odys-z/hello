"""
ID: odys.zh1
LANG: PYTHON3
TASK: crypt1
"""
from unittest import TestCase
from typing import List
from itertools import product

'''
'''
def checkDigits(nums, prod) -> bool:
    if prod > 9999 or prod <= 0:
        return False
    while prod > 0:
        unit, prod = prod % 10, prod // 10
        if unit not in nums:
            return False
    return True

def threeProd(abcde, nums) -> bool:
    '''
        a b c
          d e
      -------
        * * *
      * * *
      -------
      * * * *
    '''
    a, b, c, d, e = abcde
    abc = a * 100 + b * 10 + c
    p1 = (abc) * e
    if p1 > 999 or not checkDigits(nums, p1):
        return False

    p2 = (abc) * d
    if p2 > 999 or not checkDigits(nums, p2):
        return False

    p = p1 + p2 * 10
    if p > 9999 or not checkDigits(nums, p):
        return False;

    return True

def crypt1(n: int, nums: List[int]) -> int:
    ans = 0
    # permutation (python product)
    for perm in product(nums, repeat=5):
        if threeProd(perm, nums):
            ans += 1

    return ans

def crypt2(n: int, nums: List[int]) -> int:
    ans = 0

    '''
    reading:
    https://en.wikipedia.org/wiki/Steinhaus%E2%80%93Johnson%E2%80%93Trotter_algorithm   
    https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
    '''

    # brutal

    def products(digits, radx):
        perm = [0] * 5
        c = 0
        while True:
            yield perm
            perm[digits - 1] += 1
            if perm[digits - 1] >= radx:
                perm[digits - 1] = 0
                c = 1

            digit = 3
            while c > 0 and digit >= 0: # c must be 1
                perm[digit] += 1
                if perm[digit] >= radx:
                    perm[digit] = 0
                    c = 1
                else: c = 0
                digit -= 1
            if c > 0:
                break
    
    for p in products(5, len(nums)):
        abcde = [nums[p[0]], nums[p[1]], nums[p[2]], nums[p[3]], nums[p[4]]]
        if threeProd(abcde, nums):
            ans += 1

    return ans
    
if __name__ != "__main__": # PyUnit
    t = TestCase()
    ans = crypt2(5, [2, 3, 4, 6, 8])
    print(ans)
    t.assertEqual(1, ans)

    print('OK!')

else: # main
    fin = open('crypt1.in', 'r')
    lines = fin.readlines()
    fin.close()

    nums = list(map(lambda s: int(s.strip()), lines[1].split()))
    ans = crypt2(int(lines[0]), nums)

    fo = open('crypt1.out', 'w')
    fo.write(str(ans) + '\n')
    fo.close()
