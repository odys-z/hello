"""
ID: odys.zh1
LANG: PYTHON3
TASK: dualpal
"""

from typing import List

def toBase(n: int, b: int) -> str:
    '''
    convert n to base b number
    '''
    s = '';

    digits = '0123456789ABCDEFGHIJ'
    while n >= 1:
        r = digits[n % b]
        s = r + s
        n //= b

    return s

def isPalindrom(N, B):
    p = toBase(N, B)

    for x in range(len(p) // 2):
        if p[x] != p[-x - 1]:
            return None
    return p

def dualpal(N, S):
    res = []
    n = S
    while len(res) < N :
        cn = 0
        n += 1
        for b in range(2, 11):
            p = isPalindrom(n, b)
            if p is not None:
	            cn += 1
	            if cn >= 2 :
	                res.append(n)
	                break
    return res

def outputLines(res: List[str]):
    print(res)
    f = open('dualpal.out', 'w')
    for rl in res:
        f.write('{}\n'.format(rl))
    f.close()

fin = open('dualpal.in')
[N, S] = fin.readline().split()
fin.close()

res = dualpal(int(N), int(S))
outputLines(res)
