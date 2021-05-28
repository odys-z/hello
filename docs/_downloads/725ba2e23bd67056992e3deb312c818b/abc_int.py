'''
Intermediate Division Programming Problem: ACSL ABC, C#3

http://www.datafiles.acsl.org/samples/contest3/abc_3_int.pdf

Created on 22 Feb 2021

@author: odys-z@github.com
'''
from unittest import TestCase

def findMissing(locs):
    s = {'A', 'B', 'C'}
    for loc in locs:
        if loc in s:
            s.remove(loc)

    for e in s:
        return e
    return None

def col(matrix, i):
    '''
    get column of grid at i
    '''
    return [row[i] for row in matrix]

def resolving(grid4):
    hasNone = False
    for rx, r in enumerate(grid4):
        for cx, c in enumerate(r):
            if c == None:
                hasNone = True
                # s = {'A', 'B', 'C'}
                resolved = []
                for s0 in ['A', 'B', 'C']:
                    if s0 not in r and s0 not in col(grid4, cx):
                        resolved.append(s0)

                if len(resolved) == 1:
                    grid4[rx][cx] = resolved[0]
    return hasNone

class Solution:
    def abc(self, locs):
        [up, lft, dwn, rit] = [[2, 3, 4, 5], [7, 13, 19, 25], [32, 33, 34, 35], [12, 18, 24, 30]]
        m4loc = [[8, 9, 10, 11], [14, 15, 16, 17], [20, 21, 22, 23], [26, 27, 28, 29]]
        grid4 = [[None] * 4 for _ in range(4)]
        
        def fillp(e):
            '''
            fill (+)
            '''
            for r in range(len(m4loc)):
                for c in range(len(m4loc[r])):
                    if e == m4loc[r][c]:
                        grid4[r][c] = '+' # (+)
                        return True
            return False
        
        def inside(ix, e):
            '''
            put e int sides
            '''
            for side in [up, lft, dwn, rit]:
                for x in range(len(side)):
                    if ix == side[x]:
                        side[x] = e
                        return True
            return False
        
        def movein(up, lft, dwn, rit, grid):
            # up->down
            for x in range(len(up)):
                e = up[x]
                if e in {'A', 'B', 'C'}:
                    for rx in range(4):
                        if grid[rx][x] == None or grid[rx][x] == e:
                            # ok, try recursively
                            up[x] = None
                            grid[rx][x] = e
                            break

            # left->right
            for x in range(len(lft)):
                e = lft[x]
                if e in {'A', 'B', 'C'}:
                    for cx in range(4):
                        if grid[x][cx] == None or grid[x][cx] == e:
                            lft[x] = None
                            grid[x][cx] = e
                            break

            # left <- right
            for x in range(len(rit)):
                e = rit[x]
                if e in {'A', 'B', 'C'}:
                    for cx in range(3, -1, -1):
                        if grid[x][cx] == None or grid[x][cx] == e:
                            rit[x] = None
                            grid[x][cx] = e
                            break

            # down ^ up
            for x in range(len(dwn)):
                e = dwn[x]
                if e in {'A', 'B', 'C'}:
                    for rx in range(3, -1, -1):
                        if grid[rx][x] == None or grid[rx][x] == e:
                            # ok, try recursively
                            dwn[x] = None
                            grid[rx][x] = e
                            break

        # fill (+) 
        for ix, i in enumerate(locs):
            if i.isdigit() and fillp(int(i)):
                continue
            else:
                locs = locs[ix+1:] #  +1: numbers of first number, discarded safely
                break

        # put side ABC
        i = 0
        while i + 1 < len(locs):
            e, gx, i = locs[i], int(locs[i+1]), i+2
            inside(gx, e)

        # clear numbers in side?

        # move letters to grid
        movein(up[:], lft[:], dwn[:], rit[:], grid4)

        # resolve
        while resolving(grid4):
            pass
        
        # find answer: grid4[locs[-1]]
        lx = int(locs[-1])
        for r in range(len(m4loc)):
            for c in range(len(m4loc[r])):
                if lx == m4loc[r][c]:
                    lx = (r, c)
                    break
                 
        return grid4[lx[0]][lx[1]]

if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    
    t.assertEqual('B', s.abc([ '9', '17', '22', '26', '4', 'A', '7', 'C', '18', 'C', '19', 'C', '32', '14']))
    t.assertEqual('C', s.abc(['11', '16', '20', '27', '4', 'A', '7', 'B', '19', 'A', '24', 'B', '30', '22'])) 
    t.assertEqual('A', s.abc(['9', '14', '23', '28', '3', 'B', '7', 'A', '19', 'A', '30', '10']))
    t.assertEqual('A', s.abc(['8', '15', '23', '28', '4', 'A', '7', 'C', '24', 'C', '33', 'A', '30', '20']))
    t.assertEqual('A', s.abc(['9', '16', '23', '26', '4', 'A', '7', 'B', '19', 'B', '25', 'B', '18', '15']))

    t.assertEqual('A', s.abc(['10', '17', '20', '27', '3', 'A', '7', 'C', '18', 'B', '30', '15']))
    t.assertEqual('C', s.abc(['20', '27', '10', '17', '3', 'A', '25', 'B', '12', 'A', '18', '22']))
    t.assertEqual('B', s.abc(['8', '16', '21', '29', '3', 'B', '19', 'B', '4', 'A', '30', '27']))
    t.assertEqual('C', s.abc(['10', '15', '23', '26', '3', 'B', '25', 'B', '4', 'A', '30', '8']))
    t.assertEqual('A', s.abc(['10', '15', '20', '29', '4', 'A', '13', 'B', '32', 'C', '30', 'B', '24', '11']))

    print('OK!')