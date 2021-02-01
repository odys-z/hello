'''
TIP: If the function signature is not suitable for recursive stack, wrap it!
'''
from unittest import TestCase
from utils.treehelper import TreeNode, stringToTreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    Runtime: 68 ms, faster than 84.54% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
    Memory Usage: 28.2 MB, less than 10.85% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
    '''
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recurTrav(root, p, q) -> '(TreeNode, pq)':
            pq = root.val == p, root.val == q

            if root.left:
                lca, lpq = recurTrav(root.left,  p, q)
                if lca: return lca, lpq
                else:
                    pq = pq[0] or lpq[0], pq[1] or lpq[1]
                    if pq[0] and pq[1]: return root, pq

            if root.right:
                lca, rpq = recurTrav(root.right, p, q)
                if lca: return lca, rpq
                else:
                    pq = pq[0] or rpq[0], pq[1] or rpq[1]
                    if pq[0] and pq[1]: return root, pq

            return None, pq

        lca, _ = recurTrav(root, p.val, q.val)
        return lca


if __name__ == "__main__":
    t = TestCase()
    s = Solution()
    t.assertEqual(3, s.lowestCommonAncestor(stringToTreeNode('3,5,1,6,2,0,8,null,null,7,4'),
                                            TreeNode(5), TreeNode(1)).val)
    t.assertEqual(5, s.lowestCommonAncestor(stringToTreeNode('3,5,1,6,2,0,8,null,null,7,4'),
                                            TreeNode(5), TreeNode(4)).val)
    t.assertEqual(1, s.lowestCommonAncestor(stringToTreeNode('1, 2'),
                                            TreeNode(1), TreeNode(2)).val)
    print('OK!')