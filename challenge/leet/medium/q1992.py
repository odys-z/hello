'''
1992. Find All Groups of Farmland
https://leetcode.com/problems/find-all-groups-of-farmland/

'''
from unittest import TestCase
from typing import List

class Solution:
    '''
    76.10%
    '''
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def pos(r, c):
            '''
            position of r, c in grid
            '''
            return r + c // C, c % C

        r, c = 0, 0
        R, C = len(land), len(land[0])
        islands = []
        
        while r < R and c < C:
            if type(land[r][c]) == list: # visited
                # [r1, c1, r2, c2]
                c = land[r][c][3] + 1
                r, c = pos(r, c)
                continue
            
            if land[r][c] == 0:
                c += 1
                r, c = pos(r, c)
            else: # new land found
                island = [r, c, r, c]
                land[r][c] = island
                r_monkey = r + 1
                while r_monkey < R and land[r_monkey][c] == 1:
                    land[r_monkey][c] = island
                    island[2] = r_monkey
                    r_monkey = r_monkey + 1
                r_monkey -= 1
                
                c_monkey = c + 1
                while c_monkey < C and land[r_monkey][c_monkey] == 1:
                    land[r_monkey][c_monkey] = island
                    island[3] = c_monkey
                    c_monkey += 1

                c = c_monkey
                r, c = pos(r, c)
                
                islands.append(island)
        return islands


if __name__ == "__main__":
    t = TestCase()
    s = Solution()
    t.assertEqual([], s.findFarmland([[0]]))
    t.assertEqual([[0,0,0,0]], s.findFarmland([[1]]))
    t.assertEqual([[0,0,0,1]], s.findFarmland([[1,1]]))
    t.assertEqual([[0,0,1,0]], s.findFarmland([[1],[1]]))
    t.assertEqual([[0,0,0,0],[1,1,2,2]], s.findFarmland([[1,0,0],[0,1,1],[0,1,1]]))
    t.assertEqual([[0,0,1,1]], s.findFarmland([[1,1],[1,1]]))

    t.assertCountEqual([[0,0,5,1], [0,3,0,3], [0,5,0,5], [1,4,1,4],[3,3,4,3],[5,4,5,5]],
        s.findFarmland([
        [1,1,0,1,0,1],
        [1,1,0,0,1,0],
        [1,1,0,0,0,0],
        [1,1,0,1,0,0],
        [1,1,0,1,0,0],
        [1,1,0,0,1,1]
        ]))

    print('OK!')