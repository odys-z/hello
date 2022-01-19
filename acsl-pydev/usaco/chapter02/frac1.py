'''
ID: odys.zh1
LANG: PYTHON3
TASK: frac1
'''

from typing import List

class Ari:
    def prog(self, N):
        pass

if __name__ != '__main__':
    from unittest import TestCase

    print(__name__)
    t = TestCase() 
    a = Ari() 

    t.assertCountEqual(['0/1', '1/5', '1/4', '1/3', '2/5', '1/2' '3/5' '2/3', '3/4', '4/5', '1/1'],
                       a.prog(5))
    print('OK!')

else:
    def outputLines(intArr2: List[List[int]]) -> int:
        f = open('frac1.out', 'w')
        for s in intArr2:
            f.write('{} {}\n'.format(s[0], s[1]))
        f.close()
        return len(intArr2)
 
    g = Ari()
    fin = open('frac1.in', 'r')
    l = fin.readlines()
    fin.close()
    N, M = int(l[0]), int(l[1])

    ans = g.prog(N, M) 
    outputLines([ans])
