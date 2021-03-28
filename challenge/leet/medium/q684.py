'''
684. Redundant Connection
https://leetcode.com/problems/redundant-connection/

In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values
1, 2, ..., N), with one additional edge added. The added edge has two different
vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair
[u, v] with u < v, that represents an undirected edge connecting nodes u and v.

Return an edge that can be removed so that the resulting graph is a tree of N nodes.
If there are multiple answers, return the answer that occurs last in the given 2D-array.
The answer edge [u, v] should be in the same format, with u < v.

Example 1:
Input: [[1,2], [1,3], [2,3]]

Output: [2,3]
Explanation: The given undirected graph will be like this:
  1
 / \
2 - 3

Created on 23 Mar 2021

@author: odys-z@github.com
'''

from unittest import TestCase
from typing import List

class SolutionSetStack:
    '''
    A modified DSU
    13.76%
    '''
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def mergeDS(dsus, e):
            n1, n2 = e
            dsu = None
            for dsu in dsus:
                if n1 in dsu and n2 in dsu:
                    return e
                if n1 in dsu or n2 in dsu:
                    break
            if dsu == None:
                dsu = set()
                dsu.add(n1)
                dsus.insert(0, dsu)
            
            if n1 not in dsu and n2 in dsu:
                n1, n2 = n2, n1

            if n2 not in dsu:
                for dsu_ in dsus:
                    if n2 in dsu_ and dsu_ != dsu:
                        dsus.remove(dsu_)
                        for n in dsu_:
                            dsu.add(n)

            if n1 in dsu:
                dsu.add(n2)
            else: dsus.append(set([n1, n2])) 

        def removeDS(dsus, e):
            n1, n2 = e
            for dsu in dsus:
                if n1 in dsu or n2 in dsu:
                    dsus.remove(dsu)
                    if n2 not in dsu:
                        return dsu #, n2
                    else:
                        return dsu #, n1 if n1 not in dsu else None

        tree = set()
        stack = []
        
        for e in edges:
            if e[0] in tree and e[1] in tree:
                return e
            elif len(tree) == 0:
                tree.add(e[0])
                tree.add(e[1])
            elif (e[0] in tree and e[1] not in tree
               or e[1] in tree and e[0] not in tree):
                tree.add(e[0])
                tree.add(e[1])
                dsu = removeDS(stack, e)
                if dsu != None:
                    tree = tree.union(dsu)

            else:
                cyc = mergeDS(stack, e)
                if cyc is not None:
                    return cyc
        print('No cycles')
        
        

class Simplified:
    '''
    First try the tree is guaranteed to be constructed without a stack.

    Wrong Answer:
    Input [[3,4],[1,2],[2,4],[3,5],[2,5]]
    Output [2,4]
    Expected [2,5] 
    '''
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodes = set()
        for e in edges:
            if e[0] in nodes and e[1] in nodes:
                return e
            else:
                nodes.add(e[0])
                nodes.add(e[1])

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        pass

t = TestCase()
s = Solution()
t.assertCountEqual([2, 3], s.findRedundantConnection([[1,2], [1,3], [2,3]]))
t.assertCountEqual([1, 4], s.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))
t.assertCountEqual([2, 5], s.findRedundantConnection([[3,4],[1,2],[2,4],[3,5],[2,5]]))
t.assertCountEqual([3, 10], s.findRedundantConnection([[7,8],[2,6],[2,8],[1,4],[9,10],[1,7],[3,9],[6,9],[3,5],[3,10]]))
t.assertCountEqual([5, 25], s.findRedundantConnection(
    [[6,13],[15,22],[10,13],[12,24],[3,23],[19,20],[3,12],[2,16],
     [19,23],[2,11],[18,23],[1,25],[2,17],[4,5],[14,19],[2,3],[1,7],
     [4,6],[9,10],[8,22],[7,22],[13,18],[13,21],[15,23],[5,25]]))
t.assertCountEqual([5, 48], s.findRedundantConnection([
    [30,44], [34,47], [22,32], [35,44], [26,36], [2,15], [38,41], [28,35],
    [24,37], [14,49], [44,45], [11,50], [20,39], [7,39], [19,22], [3,17],
    [15,25], [1,39], [26,40], [5,14], [6,23], [5,6], [31,48], [13,22],
    [41,44], [10,19], [12,41], [1,12], [3,14], [40,50], [19,37], [16,26],
    [7,25], [22,33], [21,27], [9,50], [24,42], [43,46], [21,47], [29,40],
    [31,34], [9,31], [14,31], [5,48], [3,18], [4,19], [8,17], [38,46], 
    [35,37],[17,43]]))

print('OK!')