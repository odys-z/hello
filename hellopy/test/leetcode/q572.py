# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        return (s != None and sameas(s, t) or 
            sameas(s.left, t) and self.isSubtree(s.left, t) or 
            sameas(s.right, t) and self.isSubtree(s.right, t))
        
def sameas(s, t):
    return (s == None and t == None or
        s != None
        and t != None and s.val == t.val
        and sameas(s.left, t.left) and sameas(s.right, t.right))
        
