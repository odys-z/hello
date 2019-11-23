'''
Question 1192. Critical Connections in a Network
https://leetcode.com/problems/critical-connections-in-a-network/

Benchmark: 3280ms, 107.6MB

Algorithm:
https://www.geeksforgeeks.org/bridge-in-a-graph/

reference:
[1] GeeksforGeeks, <a href='https://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/'>
    Articulation Points (or Cut Vertices) in a Graph</a><br>
[2] 2228ms, 82MB version:
class Solution:
    def criticalConnections(self, n: int, connections: [[int]]) -> [[int]]:
        def dfs(curr_node, rank):
            visited[curr_node] = True
            lowest[curr_node] = rank
            for child in graph[curr_node]:
                if child == parent[curr_node]:
                    continue
                if not visited[child]:
                    parent[child] = curr_node
                    dfs(child, rank + 1)
                lowest[curr_node] = min(lowest[curr_node], lowest[child])
                if lowest[child] >= rank + 1:
                    result.append((curr_node, child))

        graph = [[] for _ in range(n)]
        for i, j in connections:
            graph[i].append(j)
            graph[j].append(i)

        visited = [False] * n
        lowest = [0] * n
        result = []
        parent = [0] * n

        dfs(0, 0)
        return result

----------------------
Created on 11 Nov 2019

@author: odys-z@github.com
'''
import unittest
from typing import List
from collections import namedtuple, defaultdict

def getEdges(connections):
    ''' May be this is why it's slow than 95% of leetcode submitted solutions. '''
    edges = defaultdict(set)
    for conn in connections:
        edges[conn[0]].add(conn[1])
        edges[conn[1]].add(conn[0])
    return edges
    
class Solution:
    time = 0
    
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # graph
        self.Vert = namedtuple('vert', ['ix', 'low', 'disc', 'parent', 'edges'])
        self.verts = [None] * n # list[Vert]
        self.crits = []
        self.edges = getEdges(connections)

        for u in range(n):
            if self.verts[u] == None:
                # Not visited
                self.critConn(u, -1)

        print(self.crits)
        return self.crits

    def critConn(self, uix, pix):
        ''' '''
        # visit u
        # verts[uix] == None
        u = self.Vert(uix, self.time, self.time, pix, self.edges[uix])
        self.verts[u.ix] = u
        self.time += 1
        
        for vix in u.edges:
            v = self.verts[vix]
            if (v == None): 
                # not visited
                v = self.critConn(vix, uix)
                u = u._replace(low = min(u.low, v.low))
                self.verts[uix] = u
                
                if (v.low > u.disc):
                    self.crits.append([u.ix, v.ix])
            # this is bidirection connect, we just step here from parent, so don't check back
            elif u.parent != vix:
                u = u._replace(low = min(u.low, v.disc))
                self.verts[u.ix] = u
        return u
            

class Test(unittest.TestCase):

    def testDfs(self):
        solut = Solution()
        self.assertEqual([[1,3]],
                solut.criticalConnections(4, [[0, 1], [1, 2], [2, 0], [1, 3]]))
        self.assertEqual([[1,2],[0,1]],
                solut.criticalConnections(3, [[0, 1], [1, 2]]))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
