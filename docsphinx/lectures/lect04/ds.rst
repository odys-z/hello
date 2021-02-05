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

Trees
-----

Some different terms::

    root  leaf / external node   internal node

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
