Data Structure
==============

`Data Structures, ACSL Topic <http://www.categories.acsl.org/wiki/index.php?title=Data_Structures>`_

Stacks and Queues
-----------------

LIFO::

    PUSH('A')
    PUSH('B')
    x = POP()
    y = POP()
    PRINT x y

output::

    B A

Sample Problem::

    A star indicates a pop operation and a letter indicates push the letter.
    What would be the next item to be popped?

    Z A * N * S * O M * * Y O R * * G * X A * D E S * * *

Answer: X

The operations can be quickly simplified as::

    Z Y X

FIFO::

    PUSH('A')
    PUSH('B')
    x = POP()
    y = POP()
    PRINT x y

output::

    A B

Stack in Python3
-----------------

Using List
__________

.. code-block:: python3

    stack = []
    stack.append('A')
    stack.append('B')
    print(stack)
    stack.pop()
    print(stack)
..

Using Queue
___________

.. code-block:: python3

    stack.append('A')
    stack.append('B')
    print(stack)
    stack.pop(0)
    print(stack)
..

List
----

ACSL::

    Although ACSL does not cover linked lists per se, they are a great preliminary
    study for binary search trees.

Example Problem: `reverse list <https://leetcode.com/problems/reverse-linked-list/>`_

.. code-block:: python3

    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    class Solution:
        def reverseList(self, head: ListNode) -> ListNode:
            if head and head.next:
                h2 = ListNode(head.val)
                head = head.next
                while head is not None:
                    h2, h2.next, head = head, h2, head.next
                return h2
            return head

    t = TestCase()
    s = Solution()
    r = ListNode(1)
    h = ListNode(2, r)
    h = ListNode(3, h)
    h = s.reverseList(h)
    t.assertEqual(1, h.val)
    r = h.next
    t.assertEqual(2, r.val)
    r = r.next
    t.assertEqual(3, r.val)
..

Solution: :download:`List Sample Problem <../../../challenge/leet/easy/q206.py>`

Trees
-----

Some different terms::

    root  leaf / external node   internal node

    Our ACSL convention places duplicate keys into the tree as if they were less
    than their equal key. (In some textbooks and software libraries, duplicate
    keys may be considered larger than their equal key.)

    Our ACSL convention is that an external node is the name given to a place
    where a new node could be attached to the tree. (In some textbooks, an external
    node is synonymous with a leaf node.)

    This tree has 9 external nodes and 31 external path length.

              A
          A          M
        o  o      E       R
                C   I   N   o
               o o o o o o

        2   2  4 4 4 4 4 4  3

Python example:

.. code-block:: python3

    class TreeNode():
        def __init__(self, v, lchild = None, rchild = None):
            self.val = v
              self.l = lchild
            self.r = rchild

    l = TreeNode(1)
    r = TreeNode(2)
    n = TreeNode(0, l, r)
..

::

      0
    1   2

Inernal Path Length
___________________

::

             P
          O    R
         G    R
        A M

    2 * 1 + 2 * 2 + 2 * 3 = 12

Binary search
_____________

pseudo code::

    p = root
    found = FALSE
    while (p ≠ NIL) and (not found)
      if (x < p’s key)
        p = p’s left child
      else if (x > p’s key)
        p = p’s right child
      else
        found = TRUE
      end if
    end while

Python program:

.. code-block:: python3

    p = root          # root = TreeNode(v)
    found = False
    while p and not found:
        if x < p.val:
            p = p.l
        elif: x > p.val:
            p = p.r
        else:
            found = TRUE

Delete Node
___________

pseudo code::

    p = node to delete
    f = father of p
    if (p has no children)
      delete p
    else if (p has one child)
      make p’s child become f’s child
      delete p
    else if (p has two children)
      l = p’s left child (it might also have children)
      r = p’s right child (it might also have children)
      make l become f’s child instead of p
      stick r onto the l tree
      delete p
    end if

        f             f
      p             l
    l   r         r

Exercise: implement function *deleteNode()*, delete node 'p'.

.. code-block:: python3

    from unittest import TestCase

    def deleteNode(v: str, root: TreeNode):
        # ...
        pass

    l = TreeNode('l')
    r = TreeNode('r')
    p = TreeNode('p', l, r)
    f = TreeNode('f', p)

    deletNode('p', r)

    t = TestCase()
    t.assertEqual('f', f.val)
    t.assertEqual('l', f.l.val)
    t.assertEqual('r', f.l.l.val)
    print('OK!')
..

Recursive Travel
________________

Although ACSL topics doesn't include recusive function, the recursive tree travelling
algorithm is a basic knowledge and skill of data structure.

Let's have a look at an example:

.. code-block:: python3

    l = TreeNode(1, TreeNode(3), TreeNode(4))
    r = TreeNode(2, TreeNode(5), TreeNode(6))
    n = TreeNode(0, l, r)

    reslt = []
    def firsttravel(root: TreeNode, reslt) -> List:
        reslt.append(root.val)
        firsttravel(root.l)
        firsttravel(root.r)

    # [0, 1, 2, 3, 4, 5, 6]
    print(reslt)
..

Source file: `first visiting tree travelling example <https://raw.githubusercontent.com/odys-z/hello/master/acsl-pydev/acsl/lect04/firstvisit.py>`_

Exercise: implement a last visiting algorithm. With the tree above, print

::

    [6, 5, 4, 3, 2, 1, 0]

Priority Queues
---------------

A priority queue is quite similar to a binary search tree, but one can only delete
the smallest item and retrieve the smallest item only. These insert and delete
operations can be done in a guaranteed time proportional to the log (base 2) of
the number of items; the retrieve-the-smallest can be done in constant time.

The queue is usually called as heap, or min heap. In python/python3, it's
`heapq <https://docs.python.org/3/library/heapq.html>`_.


A heap can implemented with an array. The parent-children relation is fixed with
indexes::

    parent  = (child - 1) // 2
    l-child = parent * 2 + 1
    r-child = parent * 2 + 2

    0 1 2   0 1 2 3 4 5 6
      0          0
     1 2      1     2
             3 4   5 6

Here is what Python 3.9 documents define a heap::

    arrays for which heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2] for all k,
    counting elements from zero

Adding an element::

    0 1 2 3 4 ?

         0
      1     2
     3 4   ?

Then competing up.

Deleting an element (heap can only delete the first/top)::

    0 1 2 3 4 5                                       1 3 2 5 4
        ( )               (5)             1              1
      1     2           1     2       (5)    2        5     2
     3 4   5           3 4            3 4            3 4

Actually pop the top, move last, then competing downward.

Exercise: implement a min-heap.

.. code-block:: python3

    class MinHeap():
        '''
        Implement a min-heap
        '''
        def peek():
            return self.h[0]

        def pop():
            t = self.h.pop(0)
            # Your task: implement moving then competing downward
            return t

        def push(v):
            self.h.append(v)
            # Your task: implement competing upward
            pass
..

Solution: :download:`MinHeap (local) <../../../acsl-pydev/acsl/lect04/minheap.py>`
