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

::

    Test 1: TEST OK [0.031 secs, 9912 KB]
    Test 2: TEST OK [0.032 secs, 9968 KB]
    Test 3: TEST OK [0.053 secs, 10236 KB]
    Test 4: TEST OK [0.031 secs, 9584 KB]
    Test 5: TEST OK [0.031 secs, 9708 KB]
    Test 6: TEST OK [0.035 secs, 9580 KB]
    Test 7: TEST OK [0.031 secs, 9984 KB]
    Test 8: TEST OK [0.032 secs, 10164 KB]
    Test 9: TEST OK [0.106 secs, 10252 KB]
    Test 10: TEST OK [0.260 secs, 10956 KB]
    Test 11: TEST OK [0.039 secs, 10376 KB]
    Test 12: TEST OK [0.262 secs, 10936 KB]
    Test 13: TEST OK [0.032 secs, 9968 KB]
    Test 14: TEST OK [0.032 secs, 9912 KB]
    Test 15: TEST OK [0.031 secs, 9568 KB]

- palsquare

`Section 1.3 PROB Palindromic Squares <https://train.usaco.org/usacogate>`_



Chapter 2
---------

TODO
`Reference Solution <https://github.com/odys-z/hello/tree/master/acsl-pydev/usaco/charpter02>`_
