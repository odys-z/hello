'''
Created on 26 Feb 2021

@author: odys-z@github.com
'''

from unittest import TestCase

# Offsets  [name,(x-off, y-off, c-bound), occupy, ...], where y-off is also r-bound
regular = [['A', (2, 0, 2), [(1, 0), (2, 0)]],
           ['B', (0, 2, 0), [(0, 1), (0, 2)]],
           ['B', (0,-2, 0), [(0,-1), (0,-2)]],
           ['C', (1, 1, 1), [(0, 1), (1, 1)]],
           ['D', (1, 2, 1), [(0, 1), (1, 1), (1, 2)]],
           ['E', (2, 1, 2), [(1, 0), (1, 1), (2, 1)]] ]

'''
      o    D o     E o
    o C    D     o E
           o
'''
mirror  = [['A', (2, 0, 2), [(1, 0), (2, 0)]],
           ['B', (0, 2, 0), [(0, 1), (0, 2)]],
           ['B', (0,-2, 0), [(0,-1), (0,-2)]],
           ['C', (1,-1, 1), [(1, 0), (1, -1)]],
           ['D', (1,-2, 1), [(0,-1), (0, -2), (1, -2)]],
           ['E', (2,-1, 2), [(1, 0), (1,-1), (2,-1)]] ]

def shape(r, c, s, blocks):
    ''' matrix (bolcks) & dir
    '''
    dirc, rx, cx = 1, -1, -1
    start = [(s-1) // c, (s-1) % c]
    if s % c == 0:
        dirc = -1
        start[1] = c - 1 - start[1]

    grid = [[0] * c for _ in range(r)]
    for b in blocks:
        if dirc < 0:
            cx = (c-1) - ((b-1) % c)
        else: 
            cx = (b-1) % c
        rx = (b-1) // c
        grid[rx][cx] = 1

    return [dirc, grid, start]

def tryPiece(grid, piece, rx, cx):
    '''
    rx, cx is exactly where to begin try
    '''
    maxr, maxc = len(grid), len(grid[0])
    if (cx < maxc
        and 0 <= cx + piece[1][2] < maxc and 0 <= rx + piece[1][1] < maxr # y-off is also r-bound
        and grid[rx][cx] == 0):
        for b in piece[2]:
            if (grid[rx+b[1]][cx+b[0]] == 1
                or 0 < cx+b[0] and grid[rx+b[1]  ][cx+b[0]-1] == 2
                or 0 < rx+b[1] and grid[rx+b[1]-1][cx+b[0]  ] == 2):
                return (None, None);
        else:
            # fill occupied with 2 - no adjacent
            c, r = cx, rx
            grid[r][c] = 2
            for b_ in piece[2]:
                c, r = cx + b_[0], rx + b_[1]
                grid[r][c] = 2
            return cx + piece[1][0] + 1, rx + piece[1][1]
    else: 
        return (None, None);

class Solution:
    def stretch(self, r, c, s, n, blocks):  # @UnusedVariable
        [dirc, grid, start] = shape(r, c, s, blocks)
        pieces = regular if dirc > 0 else mirror 
        res = []
        current = 0 # A
        row, col = start
        while col < c: 
            nxtc, nxtr = tryPiece(grid, pieces[current], row, col)
            if nxtc == None:
                current = (current + 1) % len(pieces)
            elif 0 < nxtc <= c:
                col = nxtc
                row = nxtr
                res.append(pieces[current][0])
                current = (current + (1 if current != 1 else 2)) % len(pieces) # skip -B
            else: # nxtc >= c
                raise Exception("(r, c) ({r}, {c})".format(r=nxtr, c=nxtc))

        return ''.join(res)

if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    
    t.assertEqual('ABCBE', s.stretch(6, 10, 11, 2, [48, 49]))
    t.assertEqual('ACDA', s.stretch(5, 10, 40, 1, [27]))
    t.assertEqual('ABCACA', s.stretch(6, 14, 70, 4, [66, 33, 7, 56]))
#     t.assertEqual('CECDEC', s.stretch(9, 12, 108, 5, [69, 106, 77, 91, 55]))
    t.assertEqual('ACDEA', s.stretch(6, 13, 78, 1, [49]))
    
    print('OK!')

