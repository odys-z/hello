from unittest import TestCase

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def assert2(s):
    '''
    [1,2,3]
    '''
    t = TestCase()
    
    l = TreeNode(2)
    r = TreeNode(3)
    r = TreeNode(1, l, r)
    r = s.upsideDownBinaryTree(r)
    t.assertEqual(2, r.val)
    t.assertEqual(3, r.left.val)
    t.assertEqual(1, r.right.val)

def assert3(s):
    '''
    [1,2,3,4,5,6,7]
    '''
    t = TestCase()
    
    l, r = TreeNode(4), TreeNode(5)
    l1 = TreeNode(2, l, r)

    l, r = TreeNode(6), TreeNode(7)
    r1 = TreeNode(3, l, r)

    r = TreeNode(1, l1, r1)
    r = s.upsideDownBinaryTree(r)
    t.assertEqual(4, r.val)
    t.assertEqual(3, r.left.val)
    t.assertEqual(1, r.right.val)
    
def assert3l2r(s):
    '''
    [1,2,3,4,5]
    '''
    t = TestCase()
    
    l, r = TreeNode(4), TreeNode(5)
    l1 = TreeNode(2, l, r)

    r1 = TreeNode(3)

    r = TreeNode(1, l1, r1)
    r = s.upsideDownBinaryTree(r)
    t.assertEqual(4, r.val)
    t.assertEqual(5, r.left.val)
    t.assertEqual(2, r.right.val)
    t.assertEqual(3, r.right.left.val)
    t.assertEqual(1, r.right.right.val)
 