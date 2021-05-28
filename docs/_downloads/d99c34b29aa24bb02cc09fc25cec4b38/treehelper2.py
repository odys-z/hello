'''
Another version of tree builder, converting list to tree.
where list is actually an array of tree.

@author: Odys Zhou
'''
from typing import List
from unittest import TestCase

class TreeNode(object):
    '''
    Definition for a binary tree node.
    '''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def print(self):
        buf = '{' + str(self.val)
        if self.left is not None:
            buf += ', l: ' + self.left.print()
        if self.right is not None:
            buf += ', r: ' + self.right.print()
        return buf + '}'

def list2tree(lst: List):
    '''
    convert int array (sorted in dfs binary tree) to tree of TreeNode 
    0, 1, 2, 3, 4, 5, 6 =>
    
           0
       1       2
     3   4    5 6
    7 8 9 10
    
    where l = 2m+1, r = 2m + 2
    i.e. m = (l-1)//2, m = (r-2)//2
    '''
    if not lst:
        return None

    m, l, r = 0, 1, 2  # @UnusedVariable
    root0 = TreeNode(int(lst[m]))
    lst[0] = root0
    for l in range(1, len(lst) - 1, 2):
        m = (l-1) // 2
        root = lst[m]
        if (lst[l] is not None):
            root.left = TreeNode(lst[l])
            lst[l] = root.left
        if (lst[l+1] is not None):
            root.right = TreeNode(lst[l+1])
            lst[l+1] = root.right

    return root0

if __name__ == '__main__':
    
    t = TestCase()
    t.assertEqual('{0, l: {1, l: {3, l: {7}, r: {8}}, r: {4, l: {9}, r: {10}}}, r: {2, l: {5}, r: {6}}}',
                  list2tree([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).print())

    t.assertEqual('{3, l: {5, l: {6}, r: {2, l: {7}, r: {4}}}, r: {1, l: {0}, r: {8}}}',
                  list2tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]).print())

    print('OK!')