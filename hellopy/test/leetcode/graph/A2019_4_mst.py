'''
https://leetcode.com/discuss/interview-question/357310

reference:
https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/

Created on 14 Nov 2019

@author: ody
'''
import unittest

from collections import defaultdict
import heapq

''' by debeshindia
    https://leetcode.com/discuss/interview-question/357310
'''
class Solution1:
    def __init__(self):
        pass
    
    def minCostForRepair(self, n, edges, edgesToRepair):
        graph=defaultdict(list)
        addedEdges=set()
        for edge in edgesToRepair:
            graph[edge[0]].append((edge[2], edge[1]))
            graph[edge[1]].append((edge[2], edge[0]))
            addedEdges.add((edge[0], edge[1]))
            addedEdges.add((edge[1], edge[0]))
        for edge in edges:
            if tuple(edge) not in addedEdges:
                graph[edge[0]].append((0, edge[1]))
                graph[edge[1]].append((0, edge[0]))

        res=0
        priorityQueue=[(0, 1)]
        heapq.heapify(priorityQueue)
        visited=set()

        count = 0
        while priorityQueue:
            minCost, node=heapq.heappop(priorityQueue)
            if node not in visited:
                visited.add(node)
                res+=minCost
                for cost, connectedNode in graph[node]:
                    if connectedNode not in visited:
                        heapq.heappush(priorityQueue, (cost, connectedNode))
                    count += 1

        return res, count

class Solution2:
    def __init__(self):
        pass
    
    ''' Example 1:

        Input: n = 5, edges = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]], edgesToRepair = [[1, 2, 12], [3, 4, 30], [1, 5, 8]]
        Output: 20
        Explanation:
        There are 3 connected components due to broken edges: [1], [2, 3] and [4, 5].
        We can connect these components into a single component by repearing the edges between nodes 1 and 2, and nodes 1 and 5 at a minimum cost 12 + 8 
    '''
    def minCostForRepair(self, n, edges, edgesToRepair):
        connected = set()
        graph = dict() # node-id: [to-node]

        for e in edges:
            if e[0] not in graph:
                graph[e[0]] = {e[1]: 0}
            else:
                graph[e[0]].update({e[1]: 0})

            if e[1] not in graph:
                graph[e[1]] = {e[0]: 0}
            else:
                graph[e[1]].update({e[0]: 0})
        
        for e in edgesToRepair:
            if e[0] not in graph:
                graph[e[0]] = {e[1]: e[2]}
            else:
                graph[e[0]].update({e[1]: e[2]})

            if e[1] not in graph:
                graph[e[1]] = {e[0]: e[2]}
            else:
                graph[e[1]].update({e[0]: e[2]})
            
        count = 0
        allcost = 0
        toRepair = [(0, 1)]
        heapq.heapify(toRepair)
        while toRepair:
            cost, toNode = heapq.heappop(toRepair)
            if toNode not in connected:
                connected.add(toNode)
                allcost += cost
                for edge in graph[toNode]:
                    if edge not in connected:
                        heapq.heappush(toRepair, (graph[toNode][edge], edge))
                    count += 1
        return allcost, count

class Test(unittest.TestCase):


    def testDebeshindia(self):
        s=Solution1()
        print(s.minCostForRepair(5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]], [[1, 2, 12], [3, 4, 30], [1, 5, 8]]))
        print(s.minCostForRepair(6, [[1, 2], [2, 3], [4, 5], [3, 5], [1, 6], [2, 4]], [[1, 6, 410], [2, 4, 800]]))
        print(s.minCostForRepair(6, [[1, 2], [2, 3], [4, 5], [5, 6], [1, 5], [2, 4], [3, 4]], [[1, 5, 110], [2, 4, 84], [3, 4, 79]]))
         
        s=Solution2()
        print(s.minCostForRepair(5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]],
                                 [[1, 2, 12], [3, 4, 30], [1, 5, 8]]))
        print(s.minCostForRepair(6, [[1, 2], [2, 3], [4, 5], [3, 5], [1, 6], [2, 4]],
                                 [[1, 6, 410], [2, 4, 800]]))
        print(s.minCostForRepair(6, [[1, 2], [2, 3], [4, 5], [5, 6], [1, 5], [2, 4], [3, 4]],
                                 [[1, 5, 110], [2, 4, 84], [3, 4, 79]]))

        self.assertEqual(20, s.minCostForRepair(5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]],
                                                [[1, 2, 12], [3, 4, 30], [1, 5, 8]])[0])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()