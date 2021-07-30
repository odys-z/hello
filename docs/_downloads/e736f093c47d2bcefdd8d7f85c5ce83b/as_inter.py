'''
Created on 30 Jul 2021

@author: Odys Zhou
'''

from unittest import TestCase
from typing import List

class TreeNode:
    def __init__(self, c: int, l = None, r = None):
        self.l, self.r = l, r
        self.depth = 0
        self.v = c;
    
    def insert(self, c):
        if c <= self.v:
            if self.l == None:
                self.l = TreeNode(c)
                self.l.depth = self.depth + 1
            else: self.l.insert(c)
        else:
            if self.r == None:
                self.r = TreeNode(c)
                self.r.depth = self.depth + 1
            else: self.r.insert(c)

class Solution:
    '''
    ACSL Tree:
    http://www.categories.acsl.org/wiki/index.php?title=Data_Structures
    '''
    def treeInfo(self, s: str) -> List[int]: 
        if len(s) > 0:
            tree = TreeNode(s[0])
            for c in s[1:]:
                if c != ' ':
                    tree.insert(c)
        
        # depth, leaves, one-child, inter-path, external-path
        dpth, leaf, onech, inpth, expth = 0, 0, 0, 0, 0

        def travel(root):
            # for nonlocal, see
            # https://eli.thegreenplace.net/2011/05/15/understanding-unboundlocalerror-in-python
            nonlocal dpth, leaf, onech, inpth, expth

            inpth = inpth + root.depth
            dpth = max(dpth, root.depth)

            if (root.l is None and root.r is not None or
                root.r is None and root.l is not None):
                # one child
                onech += 1
            elif root.l is None and root.r is None:
                # leaf
                leaf += 1
            
            if root.l is None:
                expth += root.depth + 1
            if root.r is None:
                expth += root.depth + 1
            
            if root.l is not None:
                travel(root.l)
        
            if root.r is not None:
                travel(root.r)

        travel(tree)
        return [dpth, leaf, onech, inpth, expth]





if __name__ == '__main__':
    s = Solution()
    t = TestCase()
    
    l = 'AMERICAN'
    t.assertCountEqual([3, 4, 1, 15, 31], s.treeInfo(l))

    l = 'AMERICANF'
    t.assertCountEqual([4, 4, 2, 19, 37], s.treeInfo(l))

    l = 'AMERICANFG'
    '''
        A
     A       M
         E      R
       C   I   N
         F
          G
    '''
    t.assertCountEqual([5, 4, 3, 24, 44], s.treeInfo(l))

    l = 'AMERICANFGN'
    '''
        A
     A       M
         E      R
       C   I   N
          F   N
          G
    '''
    t.assertCountEqual([5, 4, 4, 28, 50], s.treeInfo(l))
    # depth, leaves, one-child, inter-path, external-path
    
    l = 'Winnie the Pooh and Tigger too'
    t.assertCountEqual([7, 7, 12, 103, 153], s.treeInfo(l))
    
    l = 'Cinderella and her evil stepsisters'
    t.assertCountEqual([8, 9, 14, 141, 203], s.treeInfo(l))

    l = 'American Computer Science League was formed in 1978.'
#     t.assertCountEqual([10, 13, 15, 198, 278], s.treeInfo(l))
    t.assertCountEqual([10, 15, 16, 210, 300], s.treeInfo(l))
    
    l = 'Newbury Park High School is located in Thousand Oaks, California, 91320'
    t.assertCountEqual([13, 18, 26, 415, 537], s.treeInfo(l))
#     t.assertCountEqual([13, 16, 23, 381, 489], s.treeInfo(l))

    l = input("case 1: Winnie the Pooh and Tigger too") # 1. Winnie the Pooh and Tigger too
    for n, r in enumerate(s.treeInfo(l)):
        # https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3
        print('{1:>2d}. {0}'.format(r, n + 1))

    
    print('OK!')
