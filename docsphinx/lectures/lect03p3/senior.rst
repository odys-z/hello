2020/2021 Senior
================

The problem
-----------

Lemma
_____

Lemma:

In radix R, digit root of number N, :math:`D_R(N) = N mod (R-1)`.

Where a digit root is the digits sum of N. If the sum is has more than 1 digit, repeat sum the digits until only 1 digit.


Proof:

For a 2-digits R radix number n, :math:`n = R\cdot a + b`,

where :math:`a, b \in {0, 1, ..., R-1}`.

.. math::

    n = R \cdot a + b (\pmod R-1)
..

where :math:`\equiv` is modular remain equial.

Since

.. math::

    n = R \cdot a + b \equiv ((10a (\pmod R-1) + b (\pmod R-1)) (\pmod R-1)
    but b (\pmod R-1) = b
    and
    10 \cdot a (\pmod R-1) = 10 (\pmod R-1) \cdot a (\pmod R-1) = 1 \cdot a (\pmod R-1) = a
    and thus
    n (\pmod R-1) = (a+b) (\pmod R-1)
..

Reference

`The DigitSum of a Number and Its Remainder for Division by Nine, San José State University <http://applet-magic.com/remainder0.htm>`_

2021 Contest 1, Senior Division
_______________________________

1

AMC10 A, 2018, Problem 19
_________________________

What if we only care about units digit?

- Problem

::

    A number m is randomly selected from the set {11,13,15,17,19\}, and a number n is randomly selected from {1999, 2000, 2001, ..., 2018}. What is the probability that :math:`m \sup {n}` has a units digit of 1?

.. math::

    $\textbf{(A) }   \frac{1}{5}   \qquad        \textbf{(B) }   \frac{1}{4}   \qquad    \textbf{(C) }   \frac{3}{10}   \qquad   \textbf{(D) } \frac{7}{20} \qquad  \textbf{(E) }   \frac{2}{5}$
..

- Hint

No matter what's the product is, only the units digit's product matter. So only the least digit is 1 can be the correct answer.

