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
    # permutation
    for perm in product(nums, repeat=5):
        if threeProd(perm, nums):
            ans += 1

    return ans

def crypt2(n: int, nums: List[int]) -> int:
    ans = 0
    perm = [nums[0]] * 5
    for i in range(1, 5):
        for j in range(0, i):
            perm[i] = nums[i - 1]
            for k in range(n):

    
    return ans
    
if __name__ != "__main__": # PyUnit
    t = TestCase()
    ans = crypt1(5, [2, 3, 4, 6, 8])
    print(ans)
    t.assertEqual(1, ans)

    print('OK!')

else: # main
    fin = open('crypt1.in', 'r')
    lines = fin.readlines()
    fin.close()

    nums = list(map(lambda s: int(s.strip()), lines[1].split()))
    ans = crypt1(int(lines[0]), nums)

    fo = open('crypt1.out', 'w')
    fo.write(str(ans) + '\n')
    fo.close()
