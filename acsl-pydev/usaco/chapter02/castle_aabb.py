'''
ID: odys.zh1
LANG: PYTHON3
TASK: castle
'''

from typing import List

'''
PYTHON3 BFS with space sort & cut off
   Test 1: TEST OK [0.039 secs, 9644 KB]
   Test 2: TEST OK [0.036 secs, 9572 KB]
   Test 3: TEST OK [0.036 secs, 9540 KB]
   Test 4: TEST OK [0.043 secs, 9888 KB]
   Test 5: TEST OK [0.039 secs, 9524 KB]
   Test 6: TEST OK [0.039 secs, 10140 KB]
   Test 7: TEST OK [0.050 secs, 10116 KB]
   Test 8: TEST OK [0.538 secs, 10244 KB]
= 0.820 secs
   
PYTHON3 BFS with AABB
   Test 1: TEST OK [0.041 secs, 9688 KB]
   Test 2: TEST OK [0.036 secs, 9540 KB]
   Test 3: TEST OK [0.038 secs, 9540 KB]
   Test 4: TEST OK [0.036 secs, 10064 KB]
   Test 5: TEST OK [0.036 secs, 9628 KB]
   Test 6: TEST OK [0.039 secs, 10032 KB]
   Test 7: TEST OK [0.052 secs, 10400 KB]
   Test 8: TEST OK [0.062 secs, 10056 KB]
= 0.340 secs

C++ DFS & Greedy
   Test 1: TEST OK [0.007 secs, 1372 KB]
   Test 2: TEST OK [0.004 secs, 1400 KB]
   Test 3: TEST OK [0.011 secs, 1332 KB]
   Test 4: TEST OK [0.007 secs, 1400 KB]
   Test 5: TEST OK [0.004 secs, 1336 KB]
   Test 6: TEST OK [0.004 secs, 1372 KB]
   Test 7: TEST OK [0.007 secs, 1332 KB]
   Test 8: TEST OK [0.007 secs, 1352 KB]
= 0.051 secs

Java DFS & Gready
   Test 1: TEST OK [0.110 secs, 23624 KB]
   Test 2: TEST OK [0.110 secs, 23192 KB]
   Test 3: TEST OK [0.112 secs, 23624 KB]
   Test 4: TEST OK [0.117 secs, 23612 KB]
   Test 5: TEST OK [0.110 secs, 23668 KB]
   Test 6: TEST OK [0.133 secs, 23928 KB]
   Test 7: TEST OK [0.128 secs, 24212 KB]
   Test 8: TEST OK [0.126 secs, 24192 KB]
= 0.946 secs
'''

class Tile:
    def __init__(self, x, y, wall: int):
        self.room = None # room ID
        self.x = x
        self.y = y
        self.W, self.N, self.E, self.S = wall & 1, wall & 2, wall & 4, wall & 8 
        self.mergeOfWall = None # the final answer used to merge 2 rooms
        
    def canW(self):
        return self.W == 0
    def canN(self):
        return self.N == 0
    def canE(self):
        return self.E == 0
    def canS(self):
        return self.S == 0
    
MAXMN = 51

class Room:
    def __init__(self, roomId):
        self.id = roomId
        self.space = 0
        self.aabb = MAXMN, -1, MAXMN, -1

    def addTile(self, tile):
        self.space += 1 
        tile.room = self.id
        
        x0, x1, y0, y1 = self.aabb
        self.aabb = min(x0, tile.x-1), max(x1, tile.x), min(y0, tile.y), max(y1, tile.y+1)
        return self

def initmap(M, N, lines: List[str]) -> List[List[Tile]]:
    tiles = []
    for y in range(M):
        rowstr = lines[y].split()
        row = []
        for x in range(N):
            row.append(Tile(x, y, int(rowstr[x])))
        tiles.append(row)
    return tiles

def bfs(rooms: List[Room], neighbours: List[Tile], tiles: List[List[Tile]]):

    def mergeNotyet(rooms, rim, tile: Tile, to: Tile):
        if tile.room == None:
            rooms[to.room].addTile(tile)
            rim.append(tile)

    if neighbours == None or len(neighbours) == 0:
        return

    outerNodes = []
    for tile in neighbours:
        if tile.canW():
            w = tiles[tile.y][tile.x-1]
            mergeNotyet(rooms, neighbours, w, tile)
        if tile.canN():
            n = tiles[tile.y-1][tile.x]
            mergeNotyet(rooms, neighbours, n, tile)
        if tile.canE():
            e = tiles[tile.y][tile.x+1]
            mergeNotyet(rooms, neighbours, e, tile)
        if tile.canS():
            s = tiles[tile.y+1][tile.x]
            mergeNotyet(rooms, neighbours, s, tile)
    bfs(rooms, outerNodes, tiles)

def sortSpace(rooms: tuple):
    return sorted(rooms, key = lambda r : (-r.space, r.aabb[0], -r.aabb[2]))

def inAABB(aabb, r):
    x0, x1, y0, y1 = aabb
    u0, u1, v0, v1 = r.aabb
    
    if u0 <= x1 and x0 <= u1 and v0 <= y1 and y0 <= v1:
        return max(u0, x0), min(u1, x1), max(v0, y0), min(v1, y1)


class Ari:
    def findWallInAABB(self, id1, id2, aabb, tiles):
        x0, x1, y0, y1 = aabb
        for x in range(max(0, x0), min(x1 + 1, self.N)):
            for y in range(min(y1, self.M - 1), max(-1, y0 - 1), -1):
                t = tiles[y][x] 
                if t.room != id1 and t.room != id2:
                    continue
                if 0 < y:
                    n = tiles[y-1][x]
                    if (n.room == id1 or n.room == id2) and n.room != t.room:
                        # walls.append((t.y, t.x, 'N'))
                        return (t.y, t.x, 'N')
                if x < len(tiles[y]) - 1:
                    e = tiles[y][x+1]
                    if (e.room == id1 or e.room == id2) and e.room != t.room:
                        # walls.add((t.y, t.x, 'E'))
                        return (t.y, t.x, 'E')

    def prog(self, M, N, mapInLines):
        self.M, self.N = M, N

        tiles = initmap(M, N, mapInLines)
        
        # [ (space, [Tile]) ]
        rooms = []
        for y in range(M-1, -1, -1):
            for x in range(N):
                t = tiles[y][x]
                if t.room == None:
                    r = Room(len(rooms)).addTile(t)
                    rooms.append(r)
                    bfs(rooms, [t], tiles)
        
        rooms = sortSpace(rooms)
        
        maxWall, maxMergeSize = None, 0

        for nx in range(len(rooms)):
            rn = rooms[nx]
            for mx in range(nx + 1, len(rooms)):
                rm = rooms[mx]
                intersect = inAABB(rn.aabb, rm)
                if intersect != None:
                    w = self.findWallInAABB(rn.id, rm.id, intersect, tiles)
                    size = rm.space + rn.space
                    if w is not None and size > maxMergeSize:
                        maxMergeSize = size
                        maxWall = w
                    if size <= 2:
                        break
            if maxWall != None and 0 < maxMergeSize <= 2 and maxWall[2] == 'N':
                break

        return [len(rooms), rooms[0].space, maxMergeSize, 
                '{} {} {}'.format(maxWall[0] + 1, maxWall[1] + 1, maxWall[2])]

if __name__ != '__main__':
    from unittest import TestCase

    print(__name__)
    t = TestCase() 
    a = Ari() 

    t.assertCountEqual( [2, 1, 2, '1 1 E'],
                        a.prog(1, 2, ['15 15']) )

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
    
    # 1   2   3   4   5   6   7   8   9   10
    #---+---+---+---+---+---+---+---+---+---+
    # 15| 11  10  14| 7 | 3   10  2   2   6 |   1
    #---+---+---+---+   +   +---+   +   +   +
    # 3   2   2   6 | 5 | 1   2   0   0   4 |   2
    #   +   +   +   +   +   +   +   +   +   +
    # 1   0   0   4 | 5 | 1   0   0   0   4 |   3
    #   +   +   +   +   +   +   +   +   +   +
    # 1   0   0   4 | 13| 9   8   8   8   12|   4
    #   +   +   +   +---+---+---+---+---+---+
    # 1   0   0   4 | 7 | 11  10  10  14| 15|   5
    #   +   +   +   +   +---+---+---+---+---+
    # 1   0   0   4 | 5 | 7 | 3   2   2   6 |   6
    #   +   +   +   +   +   +   +   +   +   +
    # 1   0   0   4 | 5 | 5 | 1   0   0   4 |   7
    #   +   +   +   +   +   +   +   +   +   +
    # 1   0   0  [4>| 13| 5 | 1   0   0   4 |   8
    #   +   +   +   +---+   +   +   +   +   #
    # 1   0   0   4 | 7 | 5 | 1   0   0   4 |   9
    #   +   +   +   +   +   +   +   +   +   +
    # 9   8   8   12| 13| 13| 9   8   8   12|   10
    #---+---+---+---+---+---+---+---+---+---+
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

    t.assertCountEqual([2, 3, 4, '2 1 N',],
                       a.prog( 2, 2, [ '11 6', '15 13' ] ))
    
    N = 50
    l = ['15'] * N
    l = ' '.join(l)
    tiles = [l for _i in range(N)]
    t.assertCountEqual([N * N, 1, 2, '{0} 1 N'.format(N)], a.prog(N, N, tiles))

    t.assertCountEqual([25, 1, 2, '5 1 N',],
                       a.prog( 5, 5, [ '15 15 15 15 15', '15 15 15 15 15', '15 15 15 15 15', '15 15 15 15 15', '15 15 15 15 15' ] ))

    t.assertCountEqual([5, 9, 16, '4 1 E',],
                       a.prog( 4, 7, [
                        '11 6 11 6 3 10 6',
                        '7 9 6 13 5 15 5',
                        '1 10 12 7 13 7 5',
                        '13 11 10 8 10 12 13',]))
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
