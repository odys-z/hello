Exercise
========

1. `LeetCode Problem 401. Binary Watch <https://leetcode.com/problems/binary-watch/>`_
Recursive & Backtracking

Solution: :download:`q206 <../../../challenge/leet/easy/q401.py>`

2*. (medium)`LeetCode Problem 797. All Paths From Source to Target <https://leetcode.com/problems/all-paths-from-source-to-target/submissions/>`_

Solution: :download:`q797 <../../../challenge/leet/medium/q797.py>`

C++ Solution (runtime error at LeetCode): `q797 source folder <https://github.com/odys-z/hello/tree/master/challenge/leet.gcc/q797>`_

Tip:

i. With all paths of down & right only, this is a DP problem. see *SolutionAlmost*.

ii. With nodes referencing less index nodes, this is a backtracking problem. See *Solution*.

3. (medium, see hint) `LeetCode Problem 1641. Count Sorted Vowel Strings <https://leetcode.com/problems/count-sorted-vowel-strings/>`_

Solution: :download:`q1641 <../../../challenge/leet/medium/q1641.py>` & c++
version `q1641 <../../../challenge/leet.gcc/q1641/q1641.h>`

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

4. #Directed Graph

5. #Undirected Graph

6. #Graph #DFS

7. #Graph #BFS

8. #Graph #DSU
