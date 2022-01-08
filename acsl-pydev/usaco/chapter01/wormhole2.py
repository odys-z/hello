'''
ID: odys.zh1
LANG: PYTHON3
TASK: wormhole
'''
from itertools import permutations
import math

class Solution:
    def __init__(self) -> None:
        pass

    def walkBessie(self, holes, r, cols):
        footprint = set()
        row, col, maxcol = r, cols[0], cols[1]
        footprint.add((row, col))

        while col < maxcol + 1:
            for x in range(0, len(holes), 2):
                h0, h1 = holes[x : x+2]
                # if (row, col) == h0:
                #     row, col = h1
                if (row, col) == h1:
                    row, col = h0
                    if (row, col) in footprint:
                        return 1
                    else: 
                        footprint.add((row, col))
                        break

            col += 1
            if (row, col) in footprint:
                return 1
            else:
                footprint.add((row, col))

        return 0

    def findPairs(self, rows, cols, holes):
        cnt = 0

        for row in rows:
            trap = self.walkBessie(holes, row, cols)
            if trap > 0:
                cnt += 1
                print("+", holes)
                break

            # print("-", holes)
        return cnt
    
    def permute(self, N, locs):
        cnt = 0
        rows = set()
        cols = [float('inf'), -1]
        for loc in locs:
            rows.add(loc[0])
            cols = [min(cols[0], loc[1]), max(cols[1], loc[1])]
        
        for holes in permutations(locs):
            cnt += self.findPairs(rows, cols, holes)
        return cnt // 2 // math.factorial(N // 2)
    
'''
class SolutionBak:
    def walkBessie(self, holes, r, cols):
        footprint = set()
        cols.sort()

        for x in range(len(cols)):
            col = cols[x]
            step = (r, col)
            if step in footprint:
                return 1
            else:
                footprint.add(step)

            for x in range(0, len(holes), 2):
                h0, h1 = holes[x : x+2]
                if step != h0 and step != h1:
                    continue

                if step == h0:
                    step = h1
                elif step == h1:
                    step = h0
                    # if (row, col) in footprint:
                    #     return 1
                    # else: 
                    #     footprint.add((row, col))
                    break

        return 0

    def findPairs(self, rows, cols, holes):
        cnt = 0

        for row in rows:
            trap = self.walkBessie(holes, row, cols)
            if trap > 0:
                cnt += 1
                print("+", holes)
                break

        return cnt


    def enumpath(self, N, locs):
        cnt = 0
        rows = set()

        def permute(sublocs) -> List[HolePair]:
            if (len(sublocs) == 2):
                return [sublocs]

            subs, l = [], len(sublocs)
            s0 = sublocs[0]
            for y in range(1, l):
                subp = permute(sublocs[1: y] + sublocs[y+1:])
                for sub in subp:
                    pair = [s0, sublocs[y]]
                    pair.extend(sub)
                    subs.append(pair)
            return subs
        
        cnt = 0
        grid = dict()
        for loc in locs:
            grid.update({loc[0]: HolePair((loc[0], -1))})

        perms = permute(locs, grid)

        grid = dict()

        for holes in perms:
            print(holes)
            cnt += self.findPairs(rows, cols, holes)
        return cnt

class HolePair:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
        self.nxt = None
    
    def link(self, nxt: HolePair) -> HolePair:
        if self.a[0] == nxt[0]:
            self.nxt_a = nxt
        elif self.b[0] == nxt[0]:
            self.nxt_b = nxt
        return self
    
    # def markGrid(self, grid):
    #     def mark(loc):
    #         x, y = loc
    #         if x in grid:
    #             cells = grid[x]
    #         else:
    #             cells = []
    #             grid.update({x: cells})
    #         cells.append(self)
    #         cells.sort()

    #         grid.update({x: cells})

    #     mark(self.a)
    #     mark(self.b)

    #     return self

    def transf(self, src) -> tuple:
        if self.a == src:
            return self.b
        elif self.b == src:
            return self.a
        else: return None
    
    def moveStep(self, footprint):
        if self.a in footprint or self.b in footprint:
            return True
        else:
            footprint.add(self.a)
            footprint.add(self.b)
            return False

class Solution2:
    def __init__(self) -> None:
        # [key: row-num, value: first node]
        self.rows = dict()
    
    def permute(self, sublocs: List[tuple], grid: dict) -> List[HolePair]:
            # build sparse matrix
        if (len(sublocs) == 2):
            n = HolePair(sublocs[0], sublocs[1]).markTo(self.grid)
            return [n]

        subs, l = [], len(sublocs)
        s0 = sublocs[0]
        for y in range(1, l):
            subp = self.permute(sublocs[1: y] + sublocs[y+1:])
            pair = HolePair(s0, sublocs[y]).markTo(grid)
            for sub in subp:
                sub.insert(0, pair)
                subs.append(sub)
        return subs

    def linkup(self, holes: List[HolePair]):
        def mark(rows: dict, parent: HolePair, loc: tuple):
            x, y = loc
            if x in rows:
                cell = rows[x]
                parent.nxt = cell
            else:
                cell = parent
            rows.update({x: cell})

        for h in holes:
            self.mark(self.rows, h, h.a)
            self.mark(self.rows, h, h.b)
        return self

    def walkBessie(self, r, holepairs: List[HolePair]):
        footprint = set()
        step = holepairs[0]
        while step != None:
            if step.moveStep(footprint):
                return 1
            step = step.nxt
        return 0

    def findLoop(self, rows: List[int], holepairs: List[HolePair]):
        cnt = 0

        for row in rows:
            trap = self.walkBessie(row, holepairs)
            if trap > 0:
                cnt += 1
                break
        return cnt

    def enumpath(self, N, locs):
        cnt = 0

        permts = self.permute(locs, self.rows)

        self.rows = self.linkup(permts[0])

        rows = list(self.rows.keys())
        for perm in permts:
            print(perm)
            cnt += self.findLoop(rows, perm)
        return cnt
'''

def outputLines(intArr2: int) -> int:
    f = open('wormhole.out', 'w')
    f.write(str(intArr2) + '\n')
    f.close()
    return intArr2
 
fin = open('wormhole.in', 'r')
lines = fin.readlines()
fin.close()
N = int(lines[0])
locs = []
for l in lines[1:]:
    l = l.split()
    locs.append((int(l[0]), int(l[1])))

s = Solution()
outputLines(s.permute(N, locs))

# t = TestCase()
# t.assertEqual(2, s.permute(N, locs))
# print('OK')