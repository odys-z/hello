About USACO Guid
================

`USACO <http://www.usaco.org/>`_ & `USACO Guid <https://usaco.guide/>`_

Task 0: test
------------

`USACO Training Resource <https://train.usaco.org/>`_

:download:`task.c <task-test/hello.c>`

:download:`task.py <task-test/hello.py>`

:download:`task.python3 <task-test/hello3.py>`

Chapter 1
---------

`Reference Solution <https://github.com/odys-z/hello/tree/master/acsl-pydev/usaco/charpter01>`_

- milk2

`Section 1.3 PROB Milking Cows, milk2 <https://train.usaco.org/usacogate>`_

::

    if i-th interval overlap with i-1, merge it, update max-miling;
    if i-th inteval doesn't overlap with i-1, update max-waiting.

:download:`Reference Solution <../../../acsl-pydev/usaco/charpter01/milk2.py>`

- transform

`Section 1.3 PROB Transformation <https://train.usaco.org/usacogate>`_

::

    hint: if a matrix is transposed, where does m[i, j] go ?

:download:`Reference Solution <../../../acsl-pydev/usaco/charpter01/transform.py>`

- namenum

`Section 1.3 PROB Name that Number <https://train.usaco.org/usacogate>`_

Performance consideration:

We use number to generated a permutation set, then read dict line by line to check
is it in permutation results.

permutation complexity (d = number of digits):

.. math::

    O(d * d ^ 3)
..

dict checking:

.. math::

    O(l), where l = len(dict.txt)
..

- palsquare

`Section 1.3 PROB Palindromic Squares <https://train.usaco.org/usacogate>`_

- 1.4 Mixing Milk

`Section 1.4 PROB Mixing Milk <https://train.usaco.org/usacogate>`_

hint: convert lines of strings to number arrays ready for sort

test data::

   10 11
   101 22
   2  33

.. code-block:: python3

    def convert(line):
        numss = line.split()
        return (int(numss[0]), int(numss[1]))

    fin = open('file.in', 'r')
    lines = fin.readlines()
    fin.close()

    mapobj = map(convert, lines)

    # to sort:
    ls = sorted(mapobj)
..

Chapter 2
---------

TODO
`Reference Solution <https://github.com/odys-z/hello/tree/master/acsl-pydev/usaco/charpter02>`_
