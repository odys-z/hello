'''
Created on 1 Mar 2021

@author: odys-z@github.com
'''

from unittest import TestCase

'''
SolutionTreeNode: About 50 minutes
'''

class TreeNode:
    def __init__(self, name: str, lchild: 'TreeNode' = None, rchild: 'TreeNode' = None):
        self.n = name
        self.cnt = 1
        self.l, self.r = lchild, rchild
    
    def add(self, name):
        if self.n == name:
            self.cnt += 1
        elif name < self.n:
            if self.l == None:
                self.l = TreeNode(name)
            else:
                self.l.add(name)
        else:
            if self.r == None:
                self.r = TreeNode(name)
            else:
                self.r.add(name)
    
    def duplicates(self) -> int:
        lc = self.l.duplicates() if self.l else 0 
        rc = self.r.duplicates() if self.r else 0 
        if self.l and not self.r or self.r and not self.l:
            return self.cnt + lc + rc
        else:
            return lc + rc
 
class SolutionTreeNode:
    def duplicates(self, s: str):
        s = s.upper().strip()
        root = TreeNode(s[0])
        for ci in s[1:]: 
            if ci == ' ': continue
            root.add(ci)
        
        return root.duplicates()

class SolutionList:
    '''
    Wrong!
    '''
    def duplicates(self, s: str):
        s = s.upper().strip()
        xlen = 2 ** len(s) # max array size - not OK!!!
        cnt = [0] * xlen
        tre = [None] * xlen
        
        for c in s:
            p = 0
            while p < xlen:
                if tre[p] == None:
                    tre[p] = c
                    cnt[p] = 1
                    break
                elif c == tre[p]:
                    cnt[p] += 1
                    break
                elif c <= tre[p]: # l
                    p = 2 * p + 1
                else: # r
                    p = 2 * p + 2
        return sum(cnt)


if __name__ == '__main__':
    t = TestCase()
    s = SolutionTreeNode()
    t.assertEqual(15, s.duplicates('abracadabracabob'))
    t.assertEqual(4, s.duplicates('Amrican'))
    t.assertEqual(9, s.duplicates('American Computer Science League'))
    t.assertEqual(23, s.duplicates('Python and Java are programming languages'))
    t.assertEqual(18, s.duplicates('Python and Java and java and python'))
    t.assertEqual(9, s.duplicates('the quick brown fox jumped over the lazy river'))
    
    t.assertEqual(4, s.duplicates('simple simon'))
    t.assertEqual(10, s.duplicates('simple simon simply said something slowly'))
    t.assertEqual(7, s.duplicates('peter piper picked a peck of pickles'))
    t.assertEqual(8, s.duplicates('peter piper picked a peck of pickled peppers'))
    t.assertEqual(18, s.duplicates('how much wood could a woodchuck chuck if a woodchuck could chuck wood'))

    print('OK!')