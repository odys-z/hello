import unittest

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # beat 5% (500ms)
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        return (s != None and
                (  sameas(s, t)
                or sameas(s.left, t)
                or self.isSubtree(s.left, t)
                or sameas(s.right, t)
                or self.isSubtree(s.right, t)))

    #beat 99% (60ms) what's the difference?
    def isSubtreeTurbo(self, s, t, match=False):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t: 
            return True
        elif not s or not t: 
            return False
        if match and s.val != t.val: 
            return False
        if s.val == t.val and self.isSubtreeTurbo(s.right, t.right, True) and self.isSubtreeTurbo(s.left, t.left, True): 
            return True
        return self.isSubtreeTurbo(s.right, t, match) or self.isSubtreeTurbo(s.left, t, match)
           
def sameas(s, t):
    return (s == None and t == None or
        s != None and t != None and s.val == t.val
        and sameas(s.left, t.left) and sameas(s.right, t.right))
        
ix = 0
def buildtree(lst):
    global ix
    ix = 0
    rv = lst[0]
    ix += 1
    return buildSubtree(lst, rv)

def buildSubtree(lst, rootv):
    ''' build tree in BFS '''
    global ix
#     if ix > len(lst) - 1:
#         return None
#     elif lst[ix] is None:
#         ix += 1
#         return None

    if rootv == None:
        return None

    root = TreeNode(rootv)
    if ix >= len(lst):
        return root

    lv = lst[ix]
    ix += 1
    rv = None
    if ix < len(lst):
        rv = lst[ix]
        ix += 1

    lchild = buildSubtree(lst, lv)
    root.left = lchild
    if rv != None:
        rchild = buildSubtree(lst, rv)
        root.right = rchild

    return root
        
def stringToTreeNode(input):
    ''' https://leetcode.com/problems/subtree-of-another-tree/
        go python3 debug
     '''
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
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

class Test(unittest.TestCase):

    def test572(self):
        global ix
        solut = Solution()

        s = stringToTreeNode('[1, None, 2, 3]')
        t = stringToTreeNode('[2, 3]')
        self.assertEqual(True, solut.isSubtree(s, t))

        s = stringToTreeNode('[1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, 2]')
        t = stringToTreeNode('[1, None, 1, None, 1, None, 1, None, 1, None, 1, 2]')
        self.assertEqual(True, solut.isSubtree(s, t))

        s = stringToTreeNode('[0, 1, 2, 3, 4]')
        t = stringToTreeNode('[0, None, 2]')
        self.assertEqual(False, solut.isSubtree(s, t))

        s = stringToTreeNode('[0, 1, 2, 3, 4, 5,6]')
        t = stringToTreeNode('[2, 5, 6]')
        self.assertEqual(True, solut.isSubtree(s, t))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
