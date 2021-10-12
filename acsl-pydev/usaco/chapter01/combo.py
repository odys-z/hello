'''
ID: odys.zh1
LANG: PYTHON3
TASK: combo
'''
from typing import List
from unittest.case import TestCase

def closeTo(k, n, N, d):
    '''
        is k close to n in distance of d, mode by N
    '''
    yes = True
    for i in range(len(n)):
        if abs(n[i] - k[i]) > d:
            yes = False
            break
    return yes

def canOpen(key1, key2, n, N, dist):
    '''
        is n close to key1 or key2?
    '''
    if closeTo(key1, n, N, dist):
        return True
    return closeTo(key2, n, N, dist)

def products(digits, radx):
    '''
        [[-3, -2, -1, 0, 1], [-1, 0, 1, 2, 3], [4, 5, 6, 7, 8]]
        digits permutation in range
    '''
    c, L = 0, len(digits)
    ix = [0] * L # the digits counter
    while True:
        perm = [digits[x][v] for x, v in enumerate(ix)]
        yield perm

        ix[L - 1] += 1
        if ix[L - 1] >= radx:
            ix[L - 1] = 0
            c = 1

        digit = L - 2 # digits -1 is last, already done, so begin with -2
        while c > 0 and digit >= 0: # c must be 1
            ix[digit] += 1
            if ix[digit] >= radx:
                ix[digit] = 0
                c = 1
            else: c = 0
            digit -= 1
        if c > 0:
            break

def combo(N, farmer: List[int], master: List[int]) -> int:

    ans = set()
    dist = 2

    for n in products([[d for d in range(k - dist, k + dist + 1)] for k in farmer], 5):
        if canOpen(farmer, master, n, N, dist):
            ans.add(tuple(map(lambda e: e % N, n)))

    for n in products([[d for d in range(k - dist, k + dist + 1)] for k in master], 5):
        if canOpen(farmer, master, n, N, dist):
            ans.add(tuple(map(lambda e: e % N, n)))

    return len(ans)
    
if __name__ != "__main__": # PyUnit
    t = TestCase()
    ans = combo(50, [1, 2, 3], [5, 6, 7])
    t.assertEqual(249, ans)
    
    ans = combo(1, [1, 1, 1], [1, 1, 1])
    t.assertEqual(1, ans)

    ans = combo(4, [1, 2, 3], [2, 3, 4])
    t.assertEqual(64, ans)

    print('OK!')

else: # main
    fin = open('combo.in', 'r')
    lines = fin.readlines()
    fin.close()

    farmer = list(map(lambda s: int(s.strip()), lines[1].split()))
    master = list(map(lambda s: int(s.strip()), lines[2].split()))
    print(int(lines[0]), farmer, master)
    ans = combo(int(lines[0]), farmer, master)

    fo = open('combo.out', 'w')
    fo.write(str(ans) + '\n')
    fo.close()

