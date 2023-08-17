'''

199. Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/

'''

from typing import List, Optional
from unittest.case import TestCase

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
 64.56% 
'''
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        qu = [root]
        rview = [] 
        # lvl = 0
        
        while len(qu) > 0:
            rview.append(qu[-1].val)
            q_ = []

            for n in qu:
                if n.left != None:
                    q_.append(n.left)
                if n.right != None:
                    q_.append(n.right)

            qu = q_
            
        return rview

t = TestCase()
s = Solution()
t.assertCountEqual([], s.rightSideView(None))
t.assertCountEqual([1], s.rightSideView(TreeNode(1)))

print('OK!')
