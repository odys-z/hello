Examples
========

- `LeetCode q231 <https://leetcode.com/problems/power-of-two/>`_

Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that
:math:`n == 2^x`.

::

    36 ms, faster than 20.31%, Memory Usage: 14 MB, less than 95.80%

.. code-block:: python

    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        for i in range(32):
            if n & 1:
                n >>= 1
                if n > 0:
                    return False
                else:
                    return True
            else:
                n >>= 1
..

See `here <https://github.com/odys-z/hello/blob/master/acsl-pydev/acsl/lect03p2/lc_q231.py>`_
for more solutions.
