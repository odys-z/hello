from typing import List

class TreeNode():
    def __init__(self, v, lchild = None, rchild = None):
        self.val = v
        self.l = lchild
        self.r = rchild

def firsttravel(root: TreeNode, reslt) -> List:
    if not root: return
    reslt.append(root.val)
    firsttravel(root.l, reslt)
    firsttravel(root.r, reslt)

'''
         0
      1       4
    2   3   5   6
'''
l = TreeNode(1, TreeNode(2), TreeNode(3))
r = TreeNode(4, TreeNode(5), TreeNode(6))
n = TreeNode(0, l, r)

reslt = []
firsttravel(n, reslt)

# [0, 1, 2, 3, 4, 5, 6]
print(reslt)
