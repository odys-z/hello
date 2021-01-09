2020/2021 Senior
================

The problem
-----------

::

    Construct a Numeral Hex Triangle according to the following rules. You will be given three positive integers:
    s, a starting number;
    d, a delta (the amount by which to increase each number in the triangle);
    and r the number of rows.
    The numbers s and d will be in hexadecimal.

    1. The first row contains the number s.
    2. Each of the next rows has one more number than the previous row.
    3. Each number in the triangle is d more than the previous number in the triangle.

Solution 1
----------

Sum all digits at the last row.

.. code-block:: python

    def sumHex(n):
        s = 0
        while n > 0:
            s += n % 16;
            n //= 16
        return s

    def sol1(s:str, d:str, r:str) -> str:
        s = int(s, 16)
        d = int(d, 16)
        r = int(r, 10)

        sr0 = s + r * (r - 1) // 2 * d
        shex = 0
        for i in range(r):
            shex += sumHex(sr0 + i * d)


        while shex >= 16:
            shex = sumHex(shex)

        return '{:X}'.format(shex)
..

See source of `solution 1 <https://github.com/odys-z/hello/blob/master/acsl-pydev/acsl/contest1/c1_2021/senior.py>`_.

Solution 2
----------

Lemma
_____

    In radix R, digit root of number N, :math:`D_R(N) \equiv N \pmod {R-1}`,

    where :math:`\equiv` is modular equivalence.

A digit root is the digits sum of N. If the sum has more than 1 digit, repeat
sum the digits until only 1 digit.

Proof:

For a 2-digits R radix number n, :math:`n = R\cdot a + b`,

where :math:`a, b \in {0, 1, ..., R-1}`.

E.g. for hexadecimal digit root,

.. math::

    n \equiv 16 \cdot a + b \pmod{15} \quad \text{if remainder is not 0, otherwise 15}
..


.. math::
    \begin{align}
    & Since \\
    & n = R \cdot a + b \equiv ( 10 \cdot a \pmod{R-1} + b \pmod{R-1} ) \pmod {R-1} \\
    & but \space b \pmod {R-1} = b \\
    & and \\
    & 10 \cdot a \pmod{R-1} \equiv 10 \pmod{R-1} \cdot a \pmod{R-1} = 1 \cdot a \pmod{R-1} = a \\
    & and \space thus \\
    & n \pmod{R-1} = (a+b) \pmod{R-1} \\
    \end{align}
..

It's obvious if a k-1 digit number :math:`n` hold the property, the k digit number
:math:`R \cdot a + n` also hold the property.

Reference

`The DigitSum of a Number and Its Remainder for Division by Nine, San José State University <http://applet-magic.com/remainder0.htm>`_

.. code-block:: python

    def sol2(s: str, d: str, r: str) -> str:
        s = int(s, 16)
        d = int(d, 16)
        r = int(r, 10)

        sr0 = s + r * (r - 1) // 2 * d
        sr = r * sr0 + r * (r - 1) // 2 * d

        sr = sr % 15
        return '{:X}'.format(15 if sr == 0 else sr)
..

AMC10 A, 2018, Problem 19
_________________________

What if we only care about units digit?

- Problem

    A number m is randomly selected from the set :math:`\{11,13,15,17,19\}`, and
    a number n is randomly selected from :math:`\{1999, 2000, 2001, ..., 2018\}`.
    What is the probability that :math:`m ^ n` has a units digit of 1?

.. math::

    \textbf{(A) } \frac{1}{5} \qquad \textbf{(B) } \frac{1}{4}
    \qquad \textbf{(C) } \frac{3}{10} \qquad  \textbf{(D) } \frac{7}{20} \qquad
    \textbf{(E) } \frac{2}{5}
..

- Hint

No matter what's the product is, only the units digit's product matter. So only
the least digit is 1 can be the correct answer. Now the question can be simplified
as finding how many of :math:`1^{1}, 1^{2}, \cdots` or
:math:`\require{cancel}\cancel{3^1}, \cancel{3^2}, \cancel{3^3}, 3^{4}, \cdots`, and so on.
