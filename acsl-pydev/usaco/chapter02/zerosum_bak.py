'''
ID: odys.zh1
LANG: PYTHON3
TASK: zerosum
'''

from typing import List


class Ari:
    def prog(self, N):
        
        express = [[1]]
        for x in range(1, N):
            tempExpr = []
            for expr in express: # str
                # + - " "
                # mostly 2 operand, N < 9
                if x >= 2:
                    tempExpr.append(expr[:-1])
                    tempExpr[-1].append(10 * expr[-1] + (x+1) * 1 if expr[-1] >= 0 else -1)
                else:
                    tempExpr.append([12]) # x = 1

                tempExpr.append(expr[:])
                tempExpr[-1].append((x + 1))

                tempExpr.append(expr[:])
                tempExpr[-1].append(-(x + 1))

            express = tempExpr
        
        def evalue(expr):
            v = 0
            exp = ''
            
            for op in expr:
                v += op
                exp += '-' if op < 0 else '+'
                opblank = ''
                op = abs(op)
                while 0 < op:
                    opblank += str(op % 10) + ' '
                    op = op // 10
                opblank = opblank.strip()
                exp += opblank[::-1] # + str(op)

            return None if v != 0 else exp[1:]

        return sorted(list(filter(lambda x: x, map(lambda s: evalue(s), express))))

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
    V = int(fin.readline())
    needins = fin.readline()
    vitypes = int(fin.readline())
    vitamins = fin.readlines()
    fin.close()

    ans = g.prog(V, needins, vitypes, vitamins) 
    outputLines([ans])
