Lec 04: Data Structure
======================

`Data Structures, ACSL Topic <http://www.categories.acsl.org/wiki/index.php?title=Data_Structures>`_

Statcks and Queues
------------------

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
