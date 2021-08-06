"""
ID: odys.zh1
LANG: PYTHON3
TASK: milk
"""

from typing import List

def milk(N, M, PA):
    cost, got = 0, 0
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
