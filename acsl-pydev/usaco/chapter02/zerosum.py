'''
ID: odys.zh1
LANG: PYTHON3
TASK: zerosum
'''

from typing import List


class Ari:
    '''
       Test 1: TEST OK [0.035 secs, 9556 KB]
       Test 2: TEST OK [0.034 secs, 9556 KB]
       Test 3: TEST OK [0.035 secs, 9556 KB]
       Test 4: TEST OK [0.036 secs, 9532 KB]
       Test 5: TEST OK [0.038 secs, 9556 KB]
       Test 6: TEST OK [0.042 secs, 10004 KB]
       Test 7: TEST OK [0.057 secs, 9996 KB]
    '''
    def prog(self, N):
        
        express = ['1']
        for x in range(2, N+1):
            tempExpr = []
            for expr in express: # str
                # + - " "
                tempExpr.append(expr + '+' + str(x))
                tempExpr.append(expr + '-' + str(x))
                tempExpr.append(expr + ' ' + str(x))

            express = tempExpr
        
        def evalue(expr):
            v = 0
            sign = 1
            lastv = 0
            for tk in expr:
                if tk == '+':
                    v += sign * lastv
                    lastv = 0
                    sign = 1
                elif tk == '-':
                    v += sign * lastv
                    lastv = 0
                    sign = -1
                elif tk == ' ':
                    pass
                else:
                    lastv = lastv * 10 + int(tk)
                
            v += sign * lastv

            return v == 0

        return sorted(list(filter(lambda s: evalue(s), express)))

if __name__ != '__main__':
    from unittest import TestCase

    print(__name__)
    t = TestCase() 
    a = Ari() 

    t.assertCountEqual([
            '1+2-3+4-5-6+7',
            '1+2-3-4+5+6-7',
            '1-2 3+4+5+6+7',
            '1-2 3-4 5+6 7',
            '1-2+3+4-5+6-7',
            '1-2-3-4-5+6+7' ],
        a.prog( 7 ))

    print('OK!')

else:
    def outputLines(intArr2: List[str]) -> int:
        f = open('zerosum.out', 'w')
        for s in intArr2:
            f.write('{}\n'.format(s))
        f.close()
        return len(intArr2)
 
    g = Ari()
    fin = open('zerosum.in', 'r')
    N = int(fin.readline())
    fin.close()

    ans = g.prog(N)
    outputLines(ans)
