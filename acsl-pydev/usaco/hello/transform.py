'''
ID: odys.zh1
LANG: PYTHON3
TASK: transform
'''

# https://train.usaco.org/usacoprob2?a=ksu2wlLybOe&S=milk2
class Transform:
    def solve(self, lines):
        n = int(lines[0])
        
        def trs1(i, j):
            return j, n - 1 - i

        def trs2(i, j):
            k, l = trs1(i, j)
            return trs1(k, l)

        def trs3(i, j):
            return n - 1 - j, i
        
        def trs4(i, j):
            return i, n - 1 - j

        def trs5(i, j):
            i, j = trs4(i, j)
            return [trs1(i, j), trs2(i, j), trs3(i, j)]
        
        def trs6(i, j):
            return i, j
        
        tiles = []
        for l in lines[1 : n + 1]:
            tiles.append(list(l))
        
        transs = [(True, trs1), (True, trs2),  (True, trs3),  (True, trs4),  (True, trs5),  (True, trs6)]
        
        for i in range(n):
            for j in range(n):
                for tx in range(len(transs)):
                    t = transs[tx]
                    if t[0]:
                        i1, j1 = t[1](i, j)
                        transs[tx] = (t[0] and tiles[i1][j1] == tiles[i][j], t[1])
        for i in range(6): 
            if transs[i][0]: return i
        return 7

def outputLines(res: str):
    f = open('transform.out', 'w')
    for rl in res:
        f.write(rl + '\n')
    f.close()
 
if __name__ != '__main__':
    from unittest import TestCase

    t = TestCase() 
    m = Transform() 

    t.assertEqual('3', m.solve(['3',
                                '@-@',
                                '---',
                                '@@-',
                                '@-@',
                                '@--',
                                '--@',
                                ]))
    print('OK!')
else:
    g = Transform()
    fin = open('transform.in', 'r')
    ans = g.milk(fin.readlines()) 
    fin.close()
    outputLines([ans])
