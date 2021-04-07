'''
Subtrees And Paths @ HackerRank
https://www.hackerrank.com/challenges/subtrees-and-paths/problem

Given a rooted tree of N nodes, where each node is uniquely numbered in between [1..N].
The node 1 is the root of the tree. Each node has an integer value which is initially 0.

You need to perform the following two kinds of queries on the tree:

add t value: Add value to all nodes in subtree rooted at t
max a b: Report maximum value on the path from a to b

Input Format

First line contains N, number of nodes in the tree. Next N-1 lines contain two space
separated integers x and y which denote that there is an edge between node x and node y.
Next line contains Q, the number of queries to process.
Next Q lines follow with either add or max query per line.

Output Format

For each max query output the answer in a separate line.

Sample Input
5
1 2
2 3
2 4
5 1
6
add 4 30
add 5 20
max 4 5
add 2 -20
max 4 5
max 3 4

Sample Output
30
20
10

Initially all node values are zero.
Queries are performed in the following way:

add 4 30 // add 30 to node 4
add 5 20 // add 20 to node 5
max 4 5 // maximum of nodes 4,2,1,5 is 30
add 2 -20 // subtract 20 from nodes 2,3,4
max 4 5 // maximum of nodes 4,2,1,5 is 20
max 3 4 // maximum of nodes 3,2,4 is 10

Problem copied from HackerRank.

Issue: Wrong answer for test case 3 but passed customerized test. Why? 

@author: odys-z@github.com
'''
from typing import List
from idlelib.TreeWidget import TreeNode
from sklearn.tree._reingold_tilford import ancestor

class TreeNode():
    def __init__(self, v, p = None, children = None):
        self.v = v
        self.val = 0
        self.p = p
        self.children = children

    def addChild(self, chld):
        if self.children is None:
            self.children = []
        self.children.append(chld)
        chld.p = self

class Bitree:
    def __init__(self, N, edges:List[str]) -> 'Bitree':
        self.ans = []
        # constrains: 1 <= t, x, y, a, b <= N
        self.idx = [None] * (N+1) # [0] not used

        # The node 1 is the root of the tree.
        self.root = TreeNode(1)
        self.idx[1] = self.root

        while len(edges) > 0:
            resolving = []
            for e in edges:
                ev = e.strip().split()
                ev[0], ev[1] = int(ev[0]), int(ev[1])
                n0 = self.findNode(self.root, ev[0])
                n1 = self.findNode(self.root, ev[1])
                if n0 is None and n1 is None:
                    resolving.append(e)
                    continue

                if n0 is None and n1 is not None:
                    n0 = TreeNode(ev[0], n1)
                    n1.addChild(n0) # no exception raised?
                elif n1 is None and n0 is not None:
                    n1 = TreeNode(ev[1])
                    n0.addChild(n1)
                self.idx[ev[0]], self.idx[ev[1]] = n0, n1
            edges = resolving

    def findNode(self, rt: TreeNode, n: int):
        if rt is None or rt.v == n:
            return rt
        if rt.children is not None:
            for chld in rt.children:
                ch = self.findNode(chld, n)
                if ch is not None:
                    return ch
        return None

    def leastAncestor(self, a:int, b:int) -> int:
        ancestors = set()
        while a is not None:
            ancestors.add(a)
            a = a.p
        while b is not None and b not in ancestors:
            b = b.p
        return b

    def maxInPath(self, maxv: int, ancestor: TreeNode, me: TreeNode) -> int:
        if me == ancestor:
            return max(me.val, maxv)
        while me is not None and me != ancestor:
            maxv = max(me.val, maxv)
            me = me.p
        return maxv

    def solve(self, cmd: str) -> List[str]:
        def addVal(root: TreeNode, v1: int)-> None:
            root.val += v1
            if root.children is not None:
                for chld in root.children:
                    addVal(chld, v1)

        cmdss = cmd.split()
        if cmdss[0] == 'add':
            # add 5 20
            n = self.findNode(self.root, int(cmdss[1]))
            addVal(n, int(cmdss[2]))
        elif cmdss[0] == 'max':
            # max 4 5
            n1 = self.findNode(self.root, int(cmdss[1]))
            n2 = self.findNode(self.root, int(cmdss[2]))
            maxv = -float('inf')
            ancestor = self.leastAncestor(n1, n2)
            maxv = self.maxInPath(maxv, ancestor, n1)
            maxv = self.maxInPath(maxv, ancestor, n2)
            self.ans.append(maxv)
        else: raise(Exception(cmd))

        return self.ans

def problem():
    cnt = int(input())
    lins = []
    for _ in range(cnt-1):
        lins.append(input())

    tree = Bitree(cnt, lins)

    cnt = int(input()) # 6
    for _ in range(cnt):
        tree.solve(input())
    return tree.ans

def testProblem(t):
    def testexp(fexp, fin):
        f = open(fin)
        lins = f.readlines()
        f.close()
        cnt = int(lins[0])
        tree = Bitree(cnt, lins[1 : cnt])
        # lins[cnt] == cmd_conunt
        for l in lins[cnt + 1 : ]:
            tree.solve(l)

        f = open(fexp)
        exps = f.readlines()
        f.close()
        ints = list(map(lambda x: int(x), exps))
        for x in range(len(tree.ans)):
            t.assertEqual(ints[x], tree.ans[x])


    cnt = 5
    lins = ["1 2", "2 3", "2 4", "5 1"]
    tree = Bitree(cnt, lins)
    cnt = 6
    lins = ["add 4 30", "add 5 20", "max 4 5", "add 2 -20", "max 4 5", "max 3 4"]
    for i in range(cnt):
        tree.solve(lins[i])

    t.assertCountEqual([30, 20, 10], tree.ans)

    cnt = 10
    lins = ["1 2", "1 3", "2 4", "2 5","3 6", "3 7", "4 8", "8 9", "10 9"]
    tree = Bitree(cnt, lins)

    cnt = 30
    lins = ["add 1 -5", "add 2 -4", "add 3 6", "add 4 2", "add 5 4", "add 6 -3", "add 7 1", "add 8 -1",
            "add 9 -3", "add 10 5", "add 4 4", "max 8 1", "max 8 6", "add 3 3", "add 3 -1", "add 7 4",
            "add 9 4", "max 9 3", "max 5 3", "max 5 7", "add 5 -4", "max 6 9", "add 9 0", "add 2 -3",
            "max 7 6", "add 6 1", "add 4 -2", "add 1 1", "max 10 10", "max 7 10"]
    for i in range(cnt):
        tree.solve(lins[i])

    t.assertCountEqual([-3, 1, 3, 3, 8, 3, 8, -2, 9], tree.ans)

    testexp('01.exp', '01.in')
    testexp('01.2.exp', '01.2.in')

if __name__ == '__main__':
    ans = problem()
    for l in ans:
        print(l)

else:
    from unittest import TestCase
    t = TestCase()
    testProblem(t)
    print('OK 01 Subtree path max')
