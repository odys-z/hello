2020/2021 Intermediate
======================

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

.. code-block:: python

    def sum8(n10):
        reslt = 0
        while n10 > 0:
            reslt += n10 % 8
            n10 //= 8
        # print(reslt)
        return reslt

    def inter(s, d, r):
        s = int(s, 8)
        d = int(d, 8)
        r = int(r)

        '''
        0    s                                    s        + 0  (r = 1)
        1    s + d,  s + 2d                       s + d    + 1  (r = 2)
        2    s + 3d, s + 4d, s + 5d               s + 3d   + 2  (r = 3)
        3    s + 6d, s + 7d, s + 8d, s + 9d       s + 6d   + 3  (r = 4)

        r    s0,     s0 + d, s0 + 2d, ...         s + (r(r-1)/2) d
        '''
        sr0 = s + r * (r - 1) // 2 * d

        n = 0
        for i in range(r):
            n += sum8(sr0 + i * d);
            # print('{:o}'.format(sr0 + i * d))

        return n
..

Solution soruce: `inder.py <https://github.com/odys-z/hello/blob/master/acsl-pydev/acsl/contest1/c1_2021/inter.py>`_.
