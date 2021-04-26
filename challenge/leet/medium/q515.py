'''
515. Find Largest Value in Each Tree Row
https://leetcode.com/problems/find-largest-value-in-each-tree-row/

Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]

Example 2:
Input: root = [1,2,3]
Output: [1,3]

Created on 26 Apr 2021

@author: Odys Zhou
'''

from unittest import TestCase
from typing import List
from utils.treehelper2 import list2tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''93.53% 
    '''
    def largestValues(self, root: TreeNode) -> List[int]:
        stack = list()
        top = -1
        
        def dfs(root, top) -> int:
            if root is None:
                return
            if len(stack) <= top:
                stack.append(root.val)
            else:
                stack[top] = max(root.val, stack[top])

            dfs(root.left, top+1)
            dfs(root.right, top+1)
        
        dfs(root, top+1)
        return stack

''' C# 18.0%
public class Solution {
    List<int> stack = new List<int>();

    public IList<int> LargestValues(TreeNode root) {
        Dfs(root, 0);
        return stack;
    }
    
    void Dfs(TreeNode root, int top) {
        if (root != null) {
            if (stack.Count <= top)
                stack.Add(root.val);
            else if (stack[top] < root.val)
                stack[top] = root.val;
            
            Dfs(root.left, top + 1);
            Dfs(root.right, top + 1);
        }
    }
}
'''
 
if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    
    r = list2tree([1,3,2,5,3, None, 9])
    t.assertCountEqual([1, 3, 9], s.largestValues(r))

    r = list2tree([1,2,3])
    t.assertCountEqual([1, 3], s.largestValues(r))
    
    r = list2tree([1, None, 2])
    t.assertCountEqual([1, 2], s.largestValues(r))

    r = list2tree([])
    t.assertCountEqual([], s.largestValues(r))

    r = list2tree([3,1,5,0,2,4,6])
    t.assertCountEqual([3, 5, 6], s.largestValues(r))

    print("q515 OK!")
