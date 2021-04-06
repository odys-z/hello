'''
1557. Minimum Number of Vertices to Reach All Nodes
https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

Created on 1 Apr 2021

@author: Odys Zhou
'''

from unittest import TestCase
from typing import List
from collections import defaultdict

class Solution:
    ''' 7.12% 
    '''
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(dict)
        parent = defaultdict(int)

        for [frm, to] in edges:
            graph[frm][to] = '' # edge frm -> to starting at frm
            parent[frm] = frm
        print(graph)
        
        def dfs(startings, graph, frm):
            if frm in startings or frm not in graph:
                return
            for to in graph[frm]:
                if graph[frm][to] == '':
                    startings.add(frm)
                graph[frm][to] = 'T'
                if parent[to] == to:
                    parent[to] = parent[frm]
                    dfs(startings, graph, to)
                    if to in startings:
                        startings.remove(to)
                
        startings = set()
        for frm in graph:
            dfs(startings, graph, frm)
        return list(startings)

if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    
    t.assertCountEqual([0,3], s.findSmallestSetOfVertices(6, [[0,1],[0,2],[2,5],[3,4],[4,2]]))
    t.assertCountEqual([0,2,3], s.findSmallestSetOfVertices(5, [[0,1],[2,1],[3,1],[1,4],[2,4]]))
    
    print('OK!')