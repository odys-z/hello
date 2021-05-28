'''
108. Convert Sorted Array to Binary Search Tree
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Given an integer array nums where the elements are sorted in ascending
order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of
the two subtrees of every node never differs by more than one.

Created on 17 Apr 2021

@author: Odys Zhou
'''
from unittest import TestCase
from typing import List
from utils.treehelper2 import TreeNode, list2tree

# Definition for a binary tree node.

class Solution:
    '''
    64.58%
    '''
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        '''
        nums: sorted
        '''
        l, r = 0, len(nums) - 1
        
        def buildTree(lix, rix) -> 'root':
            '''
            0, 0    0, 1    0, 2    0, 3    0, 4
             0       0       1       1       2
            '''
            if lix > rix: return None

            m = (lix + rix) // 2
            root = TreeNode(nums[m])
            root.left  = buildTree(lix, m-1)
            root.right = buildTree(m+1, rix)
            return root

        return buildTree(l, r)


if __name__ == "__main__":
    t = TestCase()
    s = Solution()
    
    res =s.sortedArrayToBST([-10, -3, 0, 5, 9]).print()
    t.assertTrue( list2tree([0, -3, 9, -10, None, 5]).print() == res or
                  list2tree([0, -10, 5, None, -3, None, 9]).print() == res)

    print('q108 OK!')
