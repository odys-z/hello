'''
399. Evaluate Division
https://leetcode.com/problems/evaluate-division/

Created on 27 Mar 2021

@author: Odys Zhou
'''
from unittest import TestCase
from typing import List

class Dsu:
    def __init__(self, equations):
        self.variables = set(sum(equations, []))
        self.vars = {v: v for v in self.variables}
        self.rank = {v: 0 for v in self.variables}
        self.vals = {v: 1 for v in self.variables}
    
    def find(self, x, v):
        if x not in self.vars:
            return x
        while self.vars[x] != x:
            x = self.vars[x]
            self.vals[x] *= v
        return x, self.vals[x]

    def unify(self, x, y, v):
        ''' x = v * y '''
        x, vx = self.find(x, v)
        y, vy = self.find(y, v)
        
        if x == y: 
            return False

        if self.rank[x] < self.rank[y]:
            # [y] / [x] = 1/v
            self.vars[x] = y
            self.rank[y] += 1
            self.vals[y] = self.vals[x] / self.vals[y] / vy
        else:  # [x] / [y] = v
            self.vars[y] = x
            self.rank[x] += 1
            self.vals[x] = self.vals[y] / self.vals[x] * vx
    
    def div(self, x, y):
        if x not in self.variables or y not in self.variables:
            return -1
        return self.vals[x]/self.vals[y]


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dsu = Dsu(equations)
        
        for (x, y), v in zip(equations, values):
            dsu.unify(x, y, v)
            
        res = []
        for x, y in queries:
            # x, y = dsu.find(x), dsu.find(y)
            res.append(dsu.div(x, y))
        
        return res

        
if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    
    t.assertCountEqual([6.00000,0.50000,-1.00000,1.00000,-1.00000], s.calcEquation(
        equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]] ))