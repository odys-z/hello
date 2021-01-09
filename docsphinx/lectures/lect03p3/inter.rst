Intermediate Problem
====================

Problem
-------

::

    Construct a Numberal Octal Triangle according to the following rules. You
    will be given three positive integers:
    s, a starting number;
    d, a delta (the amount by which to increase each number in the triangle);
    and r the number of rows.

    The number s and d will be in octal.

    1. The first row contains the number s.
    2. Each of the rows has one more number than the previous row.
    3. Each number in the triangle is d more than the previous number in the triangle.

    Here are two examples of Numberal Octal Triangles:
    s = 2, delta = 3, rows = 5

    2
    5    10
    13   16    21
    24   27    32    35
    40   43    46    51    54

    s = 221, d = 2, r = 4

    221
    223   225
    227   231   233
    235   237   241   243

See next section for more triangles.

Solution soruce: `inder.py <https://github.com/odys-z/hello/blob/master/acsl-pydev/acsl/contest1/c1_2021/inter.py>`_.
