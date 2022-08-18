'''
ID: odys.zh1
LANG: PYTHON3
TASK: wormhole
'''
# from typing import List

class Solution2:
    '''
    Fix for test case according to Rob Kolstad:
    6
     1 15 
    20 15 
    17 11 
    22 21 
    25 11 
    20 17 
    

    +x = down

       11  15  17  21
     1     a
    17  b
    20     x   x
    22             c
    25  d
    '''

    def __init__(self) -> None:
        self.rows = dict()
    
    def permute(self, sublocs):
        '''
            build sparse matrix
        '''
        if (len(sublocs) == 2):
            return [sublocs]

        subs, l = [], len(sublocs)
        s0 = sublocs[0]
        for y in range(1, l):
            subp = self.permute(sublocs[1: y] + sublocs[y+1:])
            for sub in subp:
                pair = [s0, sublocs[y]]
                pair.extend(sub)
                subs.append(pair)
        return subs

    # def linkup(self, permt: List[tuple]):
    def linkup(self, permt):
        def mark(rows: dict, loc: tuple, target: tuple):
            x, y = loc
            if x in rows:
                row = rows[x]
            else:
                row = {'row': dict(), 'cols': []}
                rows.update({x: row})

            row['row'].update({y: target})

        '''
        grid {
            0: [(0, 0) -> (1, 0), (0, 1) -> (1, 1)], 
            1: [(1, 0) -> (0, 0), (1, 1) -> (1, 1)]
        }
        '''
        grid = dict()
        for cx in range(0, len(permt), 2):
            pair = permt[cx: cx+2]
            mark(grid, pair[0], pair[1])
            mark(grid, pair[1], pair[0])

        for r in grid:
            row = grid[r]
            row.update({'cols': sorted(row['row'].keys())})

        return grid

    def walkBessie(self, r, grid):
        def moveStep(grid, step):
            x, y = step
            step = grid[x]['row'][y]
            if step != None:
                x, y = step
                nextCol = None
                # binary search?
                for nxt in grid[x]['cols']:
                    if nxt <= y:
                        continue
                    else:
                        # nextCol = grid[x]['cols'][nxt]
                        nextCol = nxt
                        break

                if nextCol != None:
                    step = (x, nextCol)
                else:
                    step = None
                return step
            else: return None

        for rx in self.rows.keys():
            row = self.rows[rx]
            for col in row['cols']:
                step = (rx, col)
                footprint = set()

                while step != None:
                    step = moveStep(grid, step)
                    if step in footprint:
                        return 1
                    elif step != None:
                        footprint.add(step)
        return 0
 
                
    # def findLoop(self, rows: List[int]) -> int:
    def findLoop(self, rows):
        cnt = 0

        for rx in rows:
            trap = self.walkBessie(rx, self.rows)
            if trap > 0:
                cnt += 1
                break
        return cnt

    def enumpath(self, N, locs):
        cnt = 0

        permts = self.permute(locs)

        print(locs)
        print(len(permts))
        
        for perm in permts:
            # print(perm)
            self.rows = self.linkup(perm)
            cnt += self.findLoop(self.rows)
        return cnt

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
    locs.append((int(l[1]), int(l[0])))

s = Solution2()
outputLines(s.enumpath(N, locs))
