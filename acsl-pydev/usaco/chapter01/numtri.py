'''
ID: odys.zh1
LANG: PYTHON3
TASK: numtri
'''

class Ari:
    def prog(self, N, rows):
        maxpath, lastrow, c = 0, [int(rows[0])], 1
        for r in rows[1:]:
            c += 1 # count
            row = [int(ch) for ch in r.split()]
            # find path
            for i in range(c):
                lastv, lastv1 = 0 if i == 0 else lastrow[i-1], 0 if i >= c - 1 else lastrow[i]
                row[i] = int(row[i]) + max(lastv, lastv1)
                maxpath = max(maxpath, row[i])
            lastrow = row
        return maxpath

if __name__ != '__main__':
    from unittest import TestCase

    print(__name__)
    t = TestCase() 
    a = Ari() 

    t.assertEqual(30, a.prog(5, [
'7',
'3 8',
'8 1 0',
'2 7 4 4',
'4 5 2 6 5' ]))
    print('OK!')

else:
    def outputLines(line: int):
        f = open('numtri.out', 'w')
        f.write('{}\n'.format(str(line)))
        f.close()
 
    g = Ari()
    fin = open('numtri.in', 'r')
    l = fin.readlines()
    fin.close()
    N = int(l[0])

    ans = g.prog(N, l[1:]) 
    outputLines(ans)
