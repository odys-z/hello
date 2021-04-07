Computer Number Systems
=======================

Topic Summary
-------------

See :ref:`l2-comp-num-sys` in lec 2.

Examples
--------

Let's have our skill progressing into a new level.

1. Convert Color Value
______________________

In html source, color can be expressed as '#0405ff'. Which means::

    red: 04
    green: 05
    blue: 255

The problem is it is a string that can't been understood internally. Let's parse
the formated string into 3 integer, each range from 0 ~ 255.

.. code-block:: python

    def parseColor(col: str):   # "col: str" shows the argument is a str type
        if (col[0] == '#'):
            r = int(col[1] + col[2], base = 16)
            g = int(col[3] + col[4], base = 16)
            b = int(col[4] + col[6], base = 16)
            return (r, g, b)
        else:
            return (0, 0, 0)
..

See `source and tester <https://github.com/odys-z/hello/blob/master/acsl/lect03/ex01/>`_

2. Convert Decimal to Radix 64
______________________________

Problem: Given a string representing a decimal integer, convert it into a base 64
integer.

Solution:

We can use characters from Base64 to represent each digit in radix 64 integer.
They are::

    0 ~ 9, U ~ U, a ~ u, +, -
    There is also an extra char, '=' which we don't use.

To find the correct digits in base 64, we need a table to map value less than 64
into the digit::

    0, 1, 2, ... 9, 10, 11, ..., 35, 36, ..., 61, 62, 63
    0, 1, 2, ... 9,  A,  B, ...   Z,  a, ...,  z,  +,  /

With this table, the conversion is straight forward:

.. code-block:: python

    def conv_64(n: str) -> str:
        v64 = ''
        v10 = int(n)             # See comment below
        if v10 == 0:
            return '0'

        while v10 > 0:
            digit64 = v10 % 64
            v10 //= 64            # a // b return an integer
            v64 = tab64[digit64] + v64

        return v64
..

In this function, we use python int() function to brutally convert the whole
string into one large integer, and divide it by 64 each time. This is time
consuming and using a lot of memory.

For reference answer, see `here <https://github.com/odys-z/hello/blob/master/acsl-pydev/acsl/lect03/dec_r64.py>`_.

For python implementation, see `python source at github <https://github.com/python/cpython/blob/7668a8bc93c2bd573716d1bea0f52ea520502b28/Modules/binascii.c>`_

.. code-block:: c

    static const unsigned char table_b2a_base64[] =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
..

- A step further

There is a way to optimize this. As a radix 64 digit alway corresponding to a 6-bit
integer, we can scan 6 bits a time and convert it into base 64 representation.

Find a basic introduction about Base64 and open source for the conversion if you
are interested. Scan and convert is very important for Base64 conversion as it
is always used in large bulk of data transmission. Converting from thousands of
bytes into on single integer is not acceptable.

3. LeetCode Question 1404
_________________________

Question:

`Number of Steps to Reduce a Number in Binary Representation to One <https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/>`_.

Given a number s in their binary representation. Return the number of steps to
reduce it to 1 under the following rules:

    If the current number is even, you have to divide it by 2.

    If the current number is odd, you have to add 1 to it.

    It's guaranteed that you can always reach to one for all testcases.

See `examples there <https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/>`__.

test cases

.. math::

    \begin{array}{l|c}
    \hline
    Input & Output \\
    \hline
    1101  & 6 \\
    10    & 1 \\
    1111  & 5 \\
    011111111011111111 & 19 \\
    \end{array}
..

With Python, we don't have to care about integer overflow. In some language, int
type has a maximum limitation, for C++, it's :math:`2^{32} - 1`.

We can take a Python's advantage, just directly convert a base 2 string into integer:

.. code-block:: python

    s = '10011' # can be very large, above 2^32 -1
    v = int(s, base = 2)
..

This converted integer can be checked like:

.. code-block:: python

    class Solution:
        def numSteps(self, s: str) -> int:
            c = 0
            v = int(s, base=2)
            while v != 1:
                if (v & 1) == 1:
                    v += 1
                else:
                    v = v >> 1
                c += 1
            return c
..

Save the above code in file "q1404.py".

To test your python, you can take use of *unittest* module from python::

    python3
    >>> from q1404 import Solution
    >>> import unittest
    >>> tester = unittest.TestCase()
    >>> tester.assertEqual(0, Solution().numSteps('1'))

Now try it! Verify the test cases from above table.

- A Step Further

In some language like Java or C/C++, integer has a maximum limitation. A very large
value represented by a long string can not converted to **int** type. For the
question 1404 of which input s can as long as 500 digits, the above way can not
simply ported to Java or C++, etc.

There are `2 C++ solution for reference <https://github.com/odys-z/hello/blob/master/acsl/lect03/leetcode.qt/q1404.h>`_.
One modified the question, which can only working correctly with input value less
than :math:`2^{31}-1`. The other use another way to handle the carry out.

4. Roman Numbers
________________

TODO ...
