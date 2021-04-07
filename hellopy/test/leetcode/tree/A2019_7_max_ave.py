'''
Subtree with Maximum Average
https://leetcode.com/discuss/interview-question/349617

Example 1:

Input:
         20
       /   \
     12     18
  /  |  \   / \
11   2   3 15  8

Output: 18
Explanation:
There are 3 nodes which have children in this tree:
12 => (11 + 2 + 3 + 12) / 4 = 7
18 => (18 + 15 + 8) / 3 = 13.67
20 => (12 + 11 + 2 + 3 + 18 + 15 + 8 + 20) / 8 = 11.125

18 has the maximum average so output 18.

Created on 16 Nov 2019

@author: odys-z@github.com
'''
import unittest

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.children = []

class Solution: 
    def MaxAverageSubtree(self, root):
        if not root:
            return 0

        rec = averageTree(root)
        return rec[3]

def averageTree(root):
    maxAve = 0
    # maxChild = None
    if root.children:
        mySum, myAve, myCnt, valId = 0, 0, 0, 0
        for ch in root.children: 
            chSum, cnt, ave, v = averageTree(ch)
            mySum += chSum
            myCnt += cnt
            if maxAve < ave:
                maxAve = ave
                valId = v

        myCnt += 1
        myAve = (mySum + root.val) / myCnt
        if maxAve < myAve:
            maxAve = myAve
            valId = root.val

        # s = reduce(lambda s, v : s + v.sum if v else 0, root.children, 0)
        return mySum, myCnt, maxAve, valId
    else:
        return root.val, 1, 0, root.val # leave node don't have average


class Test(unittest.TestCase):


    def testName(self):
#         a = [('a', 1), ('b', 2), ('x', 3), ('z', 4)]
#         s = reduce(lambda x, y : ('s', x[1] + y[1]), a)
        '''         20
                   /   \
                 12     18
              /  |  \   / \
            11   2   3 15  8
        '''
        root = TreeNode(20)
        ch = TreeNode(12)
        ch.children.append(TreeNode(11))
        ch.children.append(TreeNode(2))
        ch.children.append(TreeNode(3))
        root.children.append(ch)

        ch = TreeNode(18)
        ch.children.append(TreeNode(15))
        ch.children.append(TreeNode(8))
        root.children.append(ch)
        
        s = Solution()
        self.assertEqual(18, s.MaxAverageSubtree(root))

        '''         500
                   /   \
                 12     18
              /  |  \   / \
            11   2   3 15  8
        '''
        root = TreeNode(500)
        ch = TreeNode(12)
        ch.children.append(TreeNode(11))
        ch.children.append(TreeNode(2))
        ch.children.append(TreeNode(3))
        root.children.append(ch)

        ch = TreeNode(18)
        ch.children.append(TreeNode(15))
        ch.children.append(TreeNode(8))
        root.children.append(ch)
        
        s = Solution()
        self.assertEqual(500, s.MaxAverageSubtree(root))

        '''          5
                   /   \
                 12     18
              /  |  \   / \
            11   200 3 15  8
        '''
        root = TreeNode(5)
        ch = TreeNode(12)
        ch.children.append(TreeNode(11))
        ch.children.append(TreeNode(200))
        ch.children.append(TreeNode(3))
        root.children.append(ch)

        ch = TreeNode(18)
        ch.children.append(TreeNode(15))
        ch.children.append(TreeNode(8))
        root.children.append(ch)
        
        s = Solution()
        self.assertEqual(12, s.MaxAverageSubtree(root))




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()