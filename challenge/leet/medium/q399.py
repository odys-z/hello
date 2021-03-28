'''
399. Evaluate Division
https://leetcode.com/problems/evaluate-division/

Created on 27 Mar 2021

@author: Odys Zhou
'''
from unittest import TestCase
from typing import List

class Dsu:
    def __init__(self, alphabet):
        self.parent = {c: c for c in alphabet}
        self.value = {c: 1 for c in alphabet}
        self.rank = {c: 1 for c in alphabet}
    
    def find(self, u):
        if u != self.parent[u]:
            self.parent[u], val = self.find(self.parent[u])
            self.value[u] *= val
        return self.parent[u], self.value[u]
    
    def union(self, u, v, w):
        pu, vu = self.find(u)
        pv, vv = self.find(v)
        if pu == pv: return
        if self.rank[pu] > self.rank[pv]: self.union(v, u, 1/w)
        else: 
            self.parent[pu] = self.parent[pv]
            self.value[pu] = w * vv / vu
            self.rank[pv] += self.rank[pu]
        
class Solution:
    ''' https://leetcode.com/problems/evaluate-division/discuss/827506/Python3-dfs
    '''
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        alphabet = set(sum(equations, []))
        uf = Dsu(alphabet)
        
        for (u, v), w in zip(equations, values):
            uf.union(u, v, w)
            
        ans = []
        for u, v in queries:
            if u in alphabet and v in alphabet: 
                pu, vu = uf.find(u)
                pv, vv = uf.find(v)
                if pu == pv: ans.append(vu / vv)
                else: ans.append(-1)
            else: ans.append(-1)
        return ans

        
if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    
    t.assertCountEqual([6.00000,0.50000,-1.00000,1.00000,-1.00000], s.calcEquation(
        equations = [["a", "b"], ["b", "c"], ['c', 'd'], ['e', 'd']],
        values =     [2.0,        3.0,        5,          2],
        queries = [["a","c"], ["b","a"], ["a","e"], ["a","a"], ["x","x"]] ))

    t.assertCountEqual([6.00000,0.50000,-1.00000,1.00000,-1.00000], s.calcEquation(
        equations = [["a","b"],["b","c"]],
        values    = [2.0,      3.0],
        queries = [["a","c"], ["b","a"], ["a","e"], ["a","a"], ["x","x"]] ))

    print('OK!')