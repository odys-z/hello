'''
ID: odys.zh1
LANG: PYTHON3
TASK: castle
'''

from typing import List

class Tile:
    def __init__(self, x, y, wall: int):
        self.room = None # room ID
        self.x = x
        self.y = y
        self.W, self.N, self.E, self.S = wall & 1, wall & 2, wall & 4, wall & 8 
        #
        
def initmap(M, N, lines: List[str]) -> List[List[Tile]]:
    tiles = []
    for y in range(M):
        rowstr = lines[y].split()
        row = []
        for x in range(N):
            row.append(Tile(x, y, int(rowstr[x])))
        tiles.append(row)
    return tiles

class Ari:
    def dfs(self, tile: Tile, roomsize: List[int], tiles: List[List[Tile]]):
        self.maxroom = 0
        if tile == None:
            return

        def mergeNotyet(roomsize: List[int], tile: Tile, to: Tile):
            if tile.room == None:
                tile.room = to.room
                roomsize[to.room] += 1
                return tile
            return None
        
        y, x = tile.y, tile.x
        if 0 < x and tile.W == 0:
            w = tiles[y][x-1]
            w = mergeNotyet(roomsize, w, tile)
            self.dfs(w, roomsize, tiles)
        if 0 < y and tile.N == 0:
            n = tiles[y-1][x]
            n = mergeNotyet(roomsize, n, tile)
            self.dfs(n, roomsize, tiles)
        if x+1 < self.N and tile.E == 0:
            e = tiles[tile.y][tile.x+1]
            e = mergeNotyet(roomsize, e, tile)
            self.dfs(e, roomsize, tiles)
        if y+1 < self.M and tile.S == 0:
            s = tiles[tile.y+1][tile.x]
            s = mergeNotyet(roomsize, s, tile)
            self.dfs(s, roomsize, tiles)

    def prog(self, M, N, mapInLines):
        self.N, self.M = N, M
        tiles = initmap(M, N, mapInLines)
        
        roomNo, roomsize = 0, []
        for y in range(M-1, -1, -1):
            for x in range(N):
                t = tiles[y][x]
                if t.room == None:
                    t.room = roomNo
                    roomNo += 1
                    roomsize.append(1)
                    self.dfs(t, roomsize, tiles)
        
        wall, mergesize = None, 0
        
        for x in range(N):
            for y in range(M-1, -1, -1):
                t = tiles[y][x]

                if t.N != 0 and 0 < y:
                    n = tiles[y-1][x]
                    if t.room != n.room:
                        size = roomsize[t.room] + roomsize[n.room]
                        if mergesize < size:
                            mergesize, wall = size, (t.y, t.x, 'N')

                if t.E != 0 and x+1 < N:
                    e = tiles[y][x+1]
                    if t.room != e.room:
                        size = roomsize[t.room] + roomsize[e.room]
                        if mergesize < size:
                            mergesize, wall = size, (t.y, t.x, 'E')
                     
        return [roomNo, max(roomsize), mergesize,
                '{} {} {}'.format(wall[0] + 1, wall[1] + 1, wall[2])]

if __name__ != '__main__':
    from unittest import TestCase

    print(__name__)
    t = TestCase() 
    a = Ari() 
    
    t.assertCountEqual( [2, 1, 2, '1 1 E'],
                        a.prog(1, 2, ['15 15']) )
    
    t.assertCountEqual([25, 1, 2, '5 1 N',],
                       a.prog( 5, 5, [ '15 15 15 15 15', '15 15 15 15 15', '15 15 15 15 15', '15 15 15 15 15', '15 15 15 15 15' ] ))

    # 1   2   3   4   5   6   7   8   9   10
    #---+---+---+---+---+---+---+---+---+---+
    # 11  10  10  14| 7 | 3   10  2   2   6 #   1
    #---+---+---+---+   +   +---+   +   +   #
    # 3   2   2   6 | 5 | 1   2   0   0   4 #   2
    #   +   +   +   +   +   +   +   +   +   #
    # 1   0   0   4 | 5 | 1   0   0   0   4 #   3
    #   +   +   +   +   +   +   +   +   +   #
    # 1   0   0   4 | 13| 9   8   8   8   4 #   4
    #   +   +   +   +---+---+---+---+---+   #
    # 1   0   0   4 | 7 | 11  10  10  14| 13#   5
    #   +   +   +   +   +---+---+---+---+---#
    # 1   0   0   4 | 5 | 7 | 3   2   2   6 #   6
    #   +   +   +   +   +   +   +   +   +   #
    # 1   0   0   4 | 5 | 5 | 1   0   0   4 #   7
    #   +   +   +   +   +   +   +   +   +   #
    # 1   0   0   4 | 13| 5 | 1   0   0   4 #   8
    #   +   +   +   + # +   +   +   +   +   #
    # 1   0   0   4 | 7 | 5 | 1   0   0   4 #   9
    #   +   +   +   +   +   +   +   +   +   #
    # 9   8   8   12| 13| 13| 9   8   8   12#   10
    #---+---+---+---+---+---+---+---+---+---+
    t.assertCountEqual( [9, 36, 41, '6 10 N'],
                        a.prog( 10, 10, [
                        '11 10 10 14 7 3 10 2 2 6',
                        '3 2 2 6 5 1 2 0 0 4',
                        '1 0 0 4 5 1 0 0 0 4',
                        '1 0 0 4 13 9 8 8 8 4',
                        '1 0 0 4 7 11 10 10 14 13',
                        '1 0 0 4 5 7 3 2 2 6',
                        '1 0 0 4 5 5 1 0 0 4',
                        '1 0 0 4 13 5 1 0 0 4',
                        '1 0 0 4 7 5 1 0 0 4',
                        '9 8 8 12 13 13 9 8 8 12'] ))
    
    #   +---+---+---+---+---+
    #   | 3   2   6 | 3   6 |
    #   +   +   +   +   +   +
    #   | 1   8   4 | 1   4 |
    #   +   +---+   +   +   +
    #   | 13| 7 | 13| 9   4 |
    #   +---+   +---+---+   +
    #   | 3   0   2   6 | 5 |
    #   +   +   +   +   +   +
    #   | 9   8   8   12| 13|
    #   +---+---+---+---+---+
    t.assertCountEqual([3, 9, 17, '4 1 N'],
                       a.prog( 5, 5, [
                        '3 2 6 3 6',
                        '1 8 4 1 4',
                        '13 7 13 9 4',
                        '3 0 2 6 5',
                        '9 8 8 12 13'] ))

    N = 50
    l = ['15'] * N
    l = ' '.join(l)
    tiles = [l for _i in range(N)]
    t.assertCountEqual([N * N, 1, 2, '{0} 1 N'.format(N)], a.prog(N, N, tiles))

    t.assertCountEqual([2, 3, 4, '2 1 N',],
                       a.prog( 2, 2, [ '11 6', '15 13' ] ))

    t.assertCountEqual([5, 9, 16, '4 1 E',],
                       a.prog( 4, 7, [
                        '11 6 11 6 3 10 6',
                        '7 9 6 13 5 15 5',
                        '1 10 12 7 13 7 5',
                        '13 11 10 8 10 12 13',]))

    t.assertCountEqual( [11, 36, 40, '8 4 E'],
                        a.prog( 10, 10, [
                        '15 11 10 14 7 3 10 2 2 6',
                        '3 2 2 6 5 1 2 0 0 4',
                        '1 0 0 4 5 1 0 0 0 4',
                        '1 0 0 4 13 9 8 8 8 12',
                        '1 0 0 4 7 11 10 10 14 15',
                        '1 0 0 4 5 7 3 2 2 6',
                        '1 0 0 4 5 5 1 0 0 4',
                        '1 0 0 4 13 5 1 0 0 4',
                        '1 0 0 4 7 5 1 0 0 4',
                        '9 8 8 12 13 13 9 8 8 12'] ))

    print('OK!')

else:
    def outputLines(intArr2: List) -> int:
        '''
         Line 1:  The number of rooms the castle has.
         Line 2:  The size of the largest room
         Line 3:  The size of the largest room creatable by removing one wall
         Line 4:  The single wall to remove to make the largest room possible
        '''
        f = open('castle.out', 'w')
        for s in intArr2:
            f.write('{}\n'.format(s))
        f.close()
        return len(intArr2)
 
    g = Ari()
    fin = open('castle.in', 'r')
    ll = fin.readlines()
    fin.close()
    l0 = ll[0].split()
    N, M = int(l0[0]), int(l0[1])

    ans = g.prog(M, N, ll[1: M+1]) 
    outputLines(ans)
