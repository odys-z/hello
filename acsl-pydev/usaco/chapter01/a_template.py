'''
ID: odys.zh1
LANG: PYTHON3
TASK: ariprog
'''

from typing import List

class Ari:
    def prog(self, N, M):
        pass

if __name__ != '__main__':
    from unittest import TestCase

    print(__name__)
    t = TestCase() 
    a = Ari() 

    t.assertCountEqual([[1, 4], [37, 4], [2, 8], [29, 8], [1, 12], [5, 12], [13, 12], [17, 12], [5, 20], [2, 24]],
                       a.prog([5, 7]))
    print('OK!')

else:
    def outputLines(intArr2: List[List[int]]) -> int:
        f = open('ariprog.out', 'w')
        for s in intArr2:
            f.write('{} {}\n'.format(s[0], s[1]))
        f.close()
        return len(intArr2)
 
    g = Ari()
    fin = open('ariprog.in', 'r')
    l = fin.readlines()
    fin.close()
    N, M = int(l[0]), int(l[1])

    ans = g.prog(N, M) 
    outputLines([ans])
