Extension: Backtracking
=======================

About
-----

An import way to brutally enumerate all possible situations.

1. `Backtracking explained <https://medium.com/@andreaiacono/backtracking-explained-7450d6ef9e1a>`_

2. `Recursion and Backtracking <https://www.hackerearth.com/practice/basic-programming/recursion/recursion-and-backtracking/tutorial/>`_

3. `Backtracking Algorithms & Problems @ GeeksforGeeks <https://www.geeksforgeeks.org/backtracking-algorithms/>`_

Problem:
--------

1. `LeetCode Problem 46. Permutations <https://leetcode.com/problems/permutations/>`_

Solution: :download:`q046 <../../../challenge/leet/medium/q046.py>`

Exercise
========

LeetCode
--------

1. `LeetCode Problem 1791. Find Center of Star Graph <https://leetcode.com/problems/find-center-of-star-graph/>`_

Solution: :download:`q1791 <../../../challenge/leet/easy/q1791.py>`

2. `LeetCode Problem 401. Binary Watch <https://leetcode.com/problems/binary-watch/>`_
Recursive & Backtracking

Solution: :download:`q206 <../../../challenge/leet/easy/q401.py>`

3. #tree

3.1 convert tree from array to TreeNode.

Problem::

    Convert tree in array to tree of TreeNode. E.g. from
    0, 1, 2, 3, 4, 5, 6 =>

           0
       1       2
     3   4    5 6
    7 8 9 10

where

:math:`l = 2m+1, r = 2m + 2`

i.e.

:math:`m = (l-1)//2, m = (r-2)//2`

Solution: :download:`convert tree node <../../../challenge/leet/utils/treehelper2.py>`

3.2 print tree (DFV)

Problem::

    Print above tree to string of
    '{0, l: {1, l: {3, l: {7}, r: {8}}, r: {4, l: {9}, r: {10}}}, r: {2, l: {5}, r: {6}}}'

3.3 build tree

`LeetCode Problem 108. Convert Sorted Array to Binary Search Tree <https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/>`_.

Solution: :download:`q108 Python <../../../challenge/leet/easy/q108.py>`

4*. (medium) `LeetCode Problem 797. All Paths From Source to Target <https://leetcode.com/problems/all-paths-from-source-to-target/>`_

Solution: :download:`q797 <../../../challenge/leet/medium/q797.py>`

C++ Solution (runtime error at LeetCode): `q797 source folder <https://github.com/odys-z/hello/tree/master/challenge/leet.gcc/q797>`_

Tip:

i. With all paths of down & right only, this is a DP problem. see *SolutionAlmost*.

ii. With nodes referencing less index nodes, this is a backtracking problem. See *Solution*.

5. (medium, see hint) `LeetCode Problem 1641. Count Sorted Vowel Strings <https://leetcode.com/problems/count-sorted-vowel-strings/>`_

Solution: :download:`q1641 <../../../challenge/leet/medium/q1641.py>` & c++
version :download:`q1641 <../../../challenge/leet.gcc/q1641/q1641.h>`

hint::

    n = 1
    1 + 1 + 1 + 1 + 1

    n = 2
    5 + 4 + 3 + 2 + 1

    n = 3
    5 + 4 + 3 + 2 + 1  -- p(3, a) = 15 + p(3, e)
      + 4 + 3 + 2 + 1  -- p(3, e) = 10 + p(3, i)
          + 3 + 2 + 1  -- p(3, i) =  6 + p(3, o)
              + 2 + 1  -- p(3, o) =  3 + p(3, u)
                  + 1  -- p(3, u)


    a      e      i      o      u

    1      1      1      1      1      n = 1
    5      4      3      2      1      n = 2
    p3,a   p3,e   p3,i   p3,o   p3,u   n = 3
    p4,a   p4,e   p4,i   p4,o   p4,u   n = 4
    p5,a   p5,e   p5,i   p5,o   p5,u   n = 5

    p6,a   p6,e   p6,i   p6,o   p6,u   n = 6

    p4,a = p3,a + p3,e + p3,i + p3,o + p3,u
    p4,e = p3,e + p3,i + p3,o + p3,u
    p4,i = p3,i + p3,o + p3,u
    p4,o = p3,o + p3,u
    p4,u = p3,u

    p5,a = p4,a + p4,e + p4,i + p4,o + p4,u
    p5,e = p4,e + p4,i + p4,o + p4,u
    p5,i = p4,i + p4,o + p4,u
    p5,o = p4,o + p4,u
    p5,u = p4,u

    p6,a = p5,a + p5,e + p5,i + p5,o + p5,u
    p6,e =        p5,e + p5,i + p5,o + p5,u
    p6,i =               p5,i + p5,o + p5,u
    p6,o =                      p5,o + p5,u
    p6,u =                             p5,u

    p7,a = p6,a + p6,e + p6,i + p6,o + p6,u
    p7,e =        p6,e + p6,i + p6,o + p6,u
    p7,i =               p6,i + p6,o + p6,u
    p7,o =                      p6,o + p6,u
    p7,u =                             p6,u

    pn,a = pn-1,a + pn-1,e + pn-1,i + pn-1,o + pn-1,u
    pn,e = pn-1,e + pn-1,i + pn-1,o + pn-1,u
    pn,i = pn-1,i + pn-1,o + pn-1,u
    pn,o = pn-1,o + pn-1,u
    pn,u = pn-1,u

Sample Problems:
----------------

x.1 `Sample Problem, Intermediate, c4 <http://www.datafiles.acsl.org/samples/contest4/c_4_duplicates_int.pdf>`_

Hint 1: carefully study the example.

Initial::

    A B C D O R T
    7 5 2 1 1 2 1

ADD H::

    A B C D H O R T
    7 5 2 1 1 1 2 1

The letters are sorted! So the same the first sample output makes sense - 'R' is
initially at '3'.

Here is the critical problem the data structure must handling:

How to save the moved character's position (how to know the original position the
before it's been sorted)?

Once understood the unspoken critical point, it's clear that figuring out the
hidden information is essential to pass the test.

Hint 2: will it asking for reporting position beyond result length?

SAMPLE INPUT SAMPLE::

    RESET abracadabracabob
    REPORT 3
    REPORT 5
    ADD BATH
    DELETE boa
    REPORT 5
    DELETE drr
    REPORT 5
    RESET American Computer Science League
    ADD Computer
    DELETE Computer
    DELETE COMPUTER
    REPORT 10

OUTPUT::

    1. RC
    2. RO
    3. ROH
    4. ROHRT
    5. UTSRPRS

Issue:

:ref:`Our test case shows there are issue <issue_2018>`.

Shouldn't the 5-th output is 'UTSRPRSTU'?

Solution with issue: :download:`2017-18 Intermediate <../../../acsl-pydev/acsl/lect06/duplicates_int.py>`

x.2 `Sample Problem, 2017-18 Senior <http://www.datafiles.acsl.org/samples/contest4/c_4_duplicates_sr.pdf>`_

.. Solution: :download:`2017-18 Senior <../../../acsl-pydev/acsl/lect06/duplicates_sr.py>`
