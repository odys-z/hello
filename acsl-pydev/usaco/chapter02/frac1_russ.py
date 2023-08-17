'''
ID: odys.zh1
LANG: PYTHON3
TASK: frac1
'''

from typing import List

class Ari:
    # According algorithm by Russ.
    def prog(self, N):
        def dfs(ans, ln, ld, rn, rd):
            n, d = ln + rn, ld + rd
            
            if n > d or d > N:
                return
            
            dfs(ans, ln, ld, n, d)
            ans.append((n, d))
            dfs(ans, n, d, rn, rd)
        
        ans = [(0, 1)]
        dfs(ans, 0, 1, 1, 1)
        ans.append((1, 1))
        return ans

if __name__ != '__main__':
    from unittest import TestCase

    print(__name__)
    t = TestCase()
    a = Ari()

    t.assertCountEqual(['0/1', '1/1'],
                       list(map(lambda x : '{}/{}'.format(x[0], x[1]), a.prog(1))) )

    t.assertCountEqual(['0/1', '1/5', '1/4', '1/3', '2/5', '1/2', '3/5', '2/3', '3/4', '4/5', '1/1'],
                       list(map(lambda x : '{}/{}'.format(x[0], x[1]), a.prog(5))) )


    t.assertCountEqual(['0/1', '1/6', '1/5', '1/4', '1/3', '2/5', '1/2', '3/5', '2/3', '3/4', '4/5', '5/6', '1/1'],
                       list(map(lambda x : '{}/{}'.format(x[0], x[1]), a.prog(6))) )
    print('OK!')

else:
    def outputLines(intArr2: List[List[int]]) -> int:
        f = open('frac1.out', 'w')
        for s in intArr2:
            f.write('{}/{}\n'.format(s[0], s[1]))
        f.close()
        return len(intArr2)

    g = Ari()
    fin = open('frac1.in', 'r')
    l = fin.readlines()
    fin.close()
    N = int(l[0])

    ans = g.prog(N)
    outputLines(ans)
