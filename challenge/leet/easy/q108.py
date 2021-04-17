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
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        '''
        nums: sorted
        '''
        l, r = 0, len(nums) - 1 # 0, 1   0, 2  0, 3
        mid = (l + r) // 2      # 0,     1     1
        
        def buildTree(nums, root, lix, mix, rix) -> (TreeNode, TreeNode, l, r):
            # l tree 
            if lix < mix < rix:
                m = (lix + mix) // 2
                root.left = TreeNode(nums[m])
                buildTree(nums, root.left, lix, m, mix)

                m = (mix + rix) // 2
                root.right = TreeNode(nums[m])
                buildTree(nums, root.right, mix, m, rix)
            return root

        root = TreeNode(nums[mid])
        return buildTree(nums, root, l, mid, r)


if __name__ == "__main__":
    t = TestCase()
    s = Solution()
    
    t.assertEqual( list2tree([0, -3, 9, -10, None, 5]).print(),
                   s.sortedArrayToBST([-10, -3, 0, 5, 9]).print() )