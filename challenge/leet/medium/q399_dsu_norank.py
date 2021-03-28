'''
see 
https://leetcode.com/problems/evaluate-division/discuss/255407/Python-Union-Find
'''

from unittest import TestCase
from typing import List

class DJS:
    def __init__(self, alphabet):
        self.parent = {char: char for char in alphabet}
        self.vals = {char: 1.0 for char in alphabet}
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x], val = self.find(self.parent[x])
            self.vals[x] *= val
        return self.parent[x], self.vals[x]
    
    def union(self, y, x, val):
        x, valx = self.find(x)
        y, valy = self.find(y)
        if x == y: return
        self.parent[y] = self.parent[x]
        self.vals[y] = val * valx / valy
        
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        alphabet = set(sum(equations, []))
        ufo = DJS(alphabet)
        for (y, x), val in zip(equations, values):
            ufo.union(y, x, val)
            
        res = []
        for y, x in queries:
            if x not in alphabet or y not in alphabet: 
                res.append(-1.0)
                continue
            y, valy = ufo.find(y)
            x, valx = ufo.find(x)
            if x == y: res.append(valy / valx)
            else: res.append(-1.0)
        return res

if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    
    t.assertCountEqual([15.0], s.calcEquation(
        equations = [["a", "b"], ["b", "c"], ['c', 'd']],
        values =     [2.0,        3.0,        5        ],
        queries = [["b", "d"]] ))

    t.assertCountEqual([6.0], s.calcEquation(
        equations = [["a", "b"], ["b", "c"], ['c', 'd'], ['e', 'b']],
        values =     [2.0,        3.0,        5,          2],
        queries = [["e", "c"]] ))

    t.assertCountEqual([6.0, 0.5, 15.0, 1.0, -1.0], s.calcEquation(
        equations = [["a", "b"], ["b", "c"], ['c', 'd'], ['e', 'd']],
        values =     [2.0,        3.0,        5,          2],
        queries = [["a","c"], ["b","a"], ["a","e"], ["a","a"], ["x","x"]] ))

    t.assertCountEqual([6.00000,0.50000,-1.00000,1.00000,-1.00000], s.calcEquation(
        equations = [["a","b"],["b","c"]],
        values    =  [2.0,      3.0],
        queries = [["a","c"], ["b","a"], ["a","e"], ["a","a"], ["x","x"]] ))

    print('OK!')
