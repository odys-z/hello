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

        def trs51(i, j):
            i, j = trs4(i, j)
            return trs1(i, j)
        
        def trs52(i, j):
            i, j = trs4(i, j)
            return trs2(i, j)
        
        def trs53(i, j):
            i, j = trs4(i, j)
            return trs3(i, j)
        
        def trs6(i, j):
            return i, j
        
        def matchEach(n, tiles, trsj):
            for i in range(n):
                for j in range(n):
                    i1, j1 = trsj(i, j)
                    if tiles[i][j] != tiles[i1 + n][j1]:
                        return False
            return True

        def matchAny(n, tiles, trsi):
            # #5 has multiple cases
            for tr in trsi:
                if matchEach(n, tiles, tr):
                    return True
            return False
        
        tiles = []
        for l in lines[1 : 2 * n + 1]:
            tiles.append(list(l))
        
        transs = [[trs1], [trs2], [trs3], [trs4], 
                  [trs51, trs52, trs53],
                  [trs6]]
        
        for tx in range(len(transs)):
            t = transs[tx]
            if matchAny(n, tiles, t):
                return str(tx + 1)

        return '7'

def outputLines(res: str):
    f = open('transform.out', 'w')
    for rl in res:
        f.write(rl + '\n')
    f.close()
 
if __name__ != '__main__':
    from unittest import TestCase

    t = TestCase() 
    m = Transform() 

    t.assertEqual('7', m.solve(['10', 
        '@--------@',
        '----------',
        '----------',
        '----------',
        '----------',
        '----------',
        '----------',
        '----------',
        '----------',
        '----------',
        '@---------',
        '----------',
        '----------',
        '----------',
        '----------',
        '----------',
        '----------',
        '----------',
        '----------',
        '---------@' ]))

    t.assertEqual('1', m.solve(['3',
                                '@-@',
                                '---',
                                '@@-',

                                '@-@',
                                '@--',
                                '--@',
                                ]))

    t.assertEqual('3', m.solve(['3',

                                'x x',
                                ' x ',
                                '  x',

                                'x x',
                                ' x ',
                                'x  ',
                                ]))

    t.assertEqual('3', m.solve(['4',

                                '+oo+',
                                'o+oo',
                                'oo+o',
                                'ooo+',

                                '+oo+',
                                'oo+o',
                                'o+oo',
                                '+ooo'
                                ]))

    t.assertEqual('4', m.solve(['4',

                                'o+o+',
                                'o+oo',
                                'oo+o',
                                'ooo+',

                                '+o+o',
                                'oo+o',
                                'o+oo',
                                '+ooo'
                                ]))

    ''' after mirroring:
                                '+o+o',
                                'oo+o',
                                'o+oo',
                                '+ooo',
    '''
    t.assertEqual('5', m.solve(['4',

                                'o+o+',
                                'o+oo',
                                'oo+o',
                                'ooo+',

                                '+oo+',
                                'o+oo',
                                'oo++',
                                'oooo'
                                ]))

    t.assertEqual('6', m.solve(['4',
                                'o+o+',
                                'o+oo',
                                'oo+o',
                                'ooo+',

                                'o+o+',
                                'o+oo',
                                'oo+o',
                                'ooo+'
                                ]))


    t.assertEqual('7', m.solve(['4',
                                'o+o+',
                                'o+oo',
                                'oo+o',
                                'ooo+',

                                'o++o',
                                'o+oo',
                                'oo+o',
                                'ooo+'
                                ]))

    print('OK!')
else:
    g = Transform()
    fin = open('transform.in', 'r')
    ans = g.solve(fin.readlines()) 
    fin.close()
    outputLines([ans])
