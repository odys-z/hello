'''
ID: odys.zh1
LANG: PYTHON3
TASK: palsquare
'''
from typing import List

def toB(n: int, B: int) -> str:
    '''
    convert n to base B number
    '''
    b = '';

    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    while n >= 1:
        r = digits[n % B]
        b = r + b
        n //= B

    return b

def isPalindrom(N2, B):
    p = toB(N2, B)
    
    for x in range(len(p) // 2):
        if p[x] != p[-x - 1]:
            return None
    return p

def palsquare() -> List[str]:
    fin = open('palsquare.in')
    B = int(fin.readline().strip())
    fin.close()

    res = []
    for N in range(1, 301, 1):
        N2 = isPalindrom(N ** 2, B)
        if N2 is not None:
            res.append([toB(N, B), N2])
    return res
    
def outputLines(res: List[str]):
    print(res)
    f = open('palsquare.out', 'w')
    for rl in res:
        f.write('{} {}\n'.format(rl[0], rl[1]))
    f.close()

ans = palsquare()
outputLines(ans)
