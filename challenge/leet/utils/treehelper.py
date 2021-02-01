'''
Created on 15 Jan 2021

@author: Odys Zhou
'''
from unittest import TestCase

class TreeNode(object):
    '''
    Definition for a binary tree node.
    '''
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def stringToTreeNode(enput):
    ''' https://leetcode.com/problems/subtree-of-another-tree/
        go python3 debug
     '''
    enput = enput.strip()
    if not input:
        return None

    inputValues = [s.strip() for s in enput.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null" and item != "None":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null" and item != "None":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

if __name__ == '__main__':
    
    t = TestCase()
    # TODO not work currently
    t.assertEqual('TreeNode{val: 3, left: TreeNode{val: 5, left: TreeNode{val: 6, left: None, right: None}, right: TreeNode{val: 2, left: TreeNode{val: 7, left: None, right: None}, right: TreeNode{val: 4, left: None, right: None}}}, right: TreeNode{val: 1, left: TreeNode{val: 0, left: None, right: None}, right: TreeNode{val: 8, left: None, right: None}}}',
        '{}'.format(stringToTreeNode('3,5,1,6,2,0,8,null,null,7,4')))