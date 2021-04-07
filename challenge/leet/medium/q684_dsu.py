'''
'''
from unittest import TestCase
from typing import List

'''
 72.05% 
'''

class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)] # 1, 2 .. N
        self.r = [0] * (n + 1)
    
    def find(self, x:int) -> int:
        while self.parent[x] != x:
            x = self.parent[x]
        return x
    
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        
        rx, ry = self.r[x], self.r[y]
        if rx < ry:
            self.parent[x] = y
            self.r[y] += 1
        else:
            self.parent[y] = x
            self.r[x] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges) + 1)

        for e in edges:
            if not dsu.union(*e):
                return e
        print('No cycle...')


if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    
    t.assertCountEqual([1, 3], s.findRedundantConnection([[1, 2], [2, 3], [1, 3]]))
    t.assertCountEqual([2, 5], s.findRedundantConnection([[3,4],[1,2],[2,4],[3,5],[2,5]]))
    t.assertCountEqual([3, 10], s.findRedundantConnection([[7,8],[2,6],[2,8],[1,4],[9,10],[1,7],[3,9],[6,9],[3,5],[3,10]]))
    t.assertCountEqual([5, 25], s.findRedundantConnection([
        [6,13],[15,22],[10,13],[12,24],[3,23],[19,20],[3,12],[2,16],[19,23],[2,11],
        [18,23],[1,25],[2,17],[4,5],[14,19],[2,3],[1,7],[4,6],[9,10],[8,22],[7,22],
        [13,18],[13,21],[15,23],[5,25]] ) )
        
    t.assertCountEqual([5, 48], s.findRedundantConnection([
        [30,44],[34,47],[22,32],[35,44],[26,36],[2,15],[38,41],[28,35],[24,37],[14,49],
        [44,45],[11,50],[20,39],[7,39],[19,22],[3,17],[15,25],[1,39],[26,40],[5,14],
        [6,23],[5,6],[31,48],[13,22],[41,44],[10,19],[12,41],[1,12],[3,14],[40,50],
        [19,37],[16,26],[7,25],[22,33],[21,27],[9,50],[24,42],[43,46],[21,47],[29,40],
        [31,34],[9,31],[14,31],[5,48],[3,18],[4,19],[8,17],[38,46],[35,37],[17,43]]))
    
    print('OK!')