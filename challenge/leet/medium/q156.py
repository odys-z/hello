'''
156. Binary Tree Upside Down
https://leetcode-cn.com/problems/binary-tree-upside-down/

Given the root of a binary tree, turn the tree upside down and return the new root.

You can turn a binary tree upside down with the following steps:

The original left child becomes the new root.
The original root becomes the new right child.
The original right child becomes the new left child.

     x         |->x        y
    y z     y -+--> z    x z

      1            |->1        4
    2   3     |->2-+---> 3   5   2
   4 5     4 -+--> 5           3  1

Constraints:
------------
    The number of nodes in the tree will be in the range [0, 10].
    1 <= Node.val <= 10
    Every node has either 0 or 2 children.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-upside-down
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from medium.q156_helper import assert2, assert3l2r

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.r0 = None

    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        self.r0 = root
        def topdown(root):
            if root.left and root.right:
                l = root.left
                topdown(l)
                l.left, l.right = root.right, root
                root.left, root.right = None, None
            else:
                self.r0 = root
        topdown(root)
        return self.r0
        
if __name__ == '__main__':
    s = Solution()
    
    '''
    test shows [1, 2] case, but "Every node has either 0 or 2 children."
    l = TreeNode(2)
    r = TreeNode(1, l)
    t = TestCase()
    r = s.upsideDownBinaryTree(r)
    t.assertEqual(2, r.val)
    t.assertEqual(None, r.left)
    t.assertEqual(1, r.right.val)
    '''

    assert2(s)
    assert3l2r(s)
    # assert3(s)

    print('OK')