'''
797. All Paths From Source to Target
https://leetcode.com/problems/all-paths-from-source-to-target/

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all
possible paths from node 0 to node n - 1, and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from
node i (i.e., there is a directed edge from node i to node graph[i][j]).

Example 1:
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
'''
from unittest import TestCase
from typing import List

class Solution2:
    '''
    last node not necessarily the last one
    '''
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        last, lastx = None, -1 # find last node of graph
        for ix in range(len(graph) - 1, -1, -1):
            if len(graph[ix]) == 0:
                last = graph[ix]
                lastx = ix
                break

class SolutionAlmost:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        lastx = len(graph) - 1
        dp = [None] * len(graph)
        dp[lastx] = [[lastx]]  # paths
        for x in range(lastx - 1, -1, -1):
            nxtNodes = graph[x]
            pathx = []
            for nxt in nxtNodes:
                for nxtPath in dp[nxt]:
                    p = [x]
                    p.extend(nxtPath)
                    pathx.append(p)
            dp[x] = pathx
            lastx = x
        return dp[0]

class Solution:
    '''
    73.06%
    '''
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(dp, graph: List[List[int]]) ->List[List[int]]: # return dp
            lastx = len(graph) - 1
            for x in range(lastx - 1, -1, -1):
                nxtNodes = graph[x]
                pathx = []
                for nxt in nxtNodes:
                    if not dp[nxt]:
                        nxtNodes_ = [nxt_ for nxt_ in nxtNodes if nxt_ != nxt]
                        graph[x] = nxtNodes_
                        dp = dfs(dp, graph)
                        graph[x] = nxtNodes

                    for nxtPath in dp[nxt]:
                        p = [x]
                        p.extend(nxtPath)
                        pathx.append(p)
                dp[x] = pathx
                lastx = x
            return dp

        dp = [None] * len(graph)
        lastx = len(graph) - 1
        dp[lastx] = [[lastx]]  # paths
        dp = dfs(dp, graph)
        return dp[0]

if __name__ == '__main__':
    t = TestCase()
    s = Solution()

    t.assertCountEqual([[0,1,3],[0,2,3]], s.allPathsSourceTarget([[1,2],[3],[3],[]]))
    t.assertCountEqual([[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]],
                       s.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))
    t.assertCountEqual([[0,1,2,3],[0,2,3],[0,3]],
                       s.allPathsSourceTarget([[1,2,3],[2],[3],[]]))
    t.assertCountEqual([[0, 1]], s.allPathsSourceTarget([[1],[]]))
    t.assertCountEqual([[0,1,2,3],[0,2,3],[0,3]], s.allPathsSourceTarget([[1,2,3],[2],[3],[]]))
    t.assertCountEqual([[0,1,2,3],[0,3]], s.allPathsSourceTarget([[1,3],[2],[3],[]]))

    t.assertCountEqual([[0,2,1,3]], s.allPathsSourceTarget([[2],[3],[1],[]]))
    print('OK!')
