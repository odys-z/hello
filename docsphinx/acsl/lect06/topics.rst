Lec 06: Topics
==============

Graph Theory
------------

Prerequisite: Matrix Multiplication
___________________________________

A matrix can be used to represent paths from i to j if :math:`a_{ij} = 1`.

.. math::

    a = \left[\begin{array}{lcr}
    0 & 1 & 0 \\
    1 & 0 & 0 \\
    0 & 0 & 0
    \end{array}\right]
..

Matrix multiplication is defined as:

for n x m matrix A, m x k matrix B,

.. math::

    A \cdot B = C
..

where C is a n x k matrix,

.. math::

    \sum_{t=0}^m a_{jt} \cdot b_{tj} = c_{ij}.
..

Example, :math:`A_{2x4} \cdot M_{4x3} = C_{2x3}`

.. math::

    \begin{bmatrix}
    a_{00} & a_{01} & a_{02} & a_{03} \\
    a_{10} & a_{11} & a_{12} & a_{13}
    \end{bmatrix}
    \begin{bmatrix}
    m_{00} & m_{01} & m_{02} \\
    m_{10} & m_{11} & m_{12} \\
    m_{20} & m_{21} & m_{22} \\
    m_{30} & m_{31} & m_{32}
    \end{bmatrix} =
    \begin{bmatrix}
    c_{00} & c_{01} & c_{02} \\
    c_{10} & c_{11} & c_{12}
    \end{bmatrix}
..

where :math:`c_{00} = a_{00} \cdot b_{00} + a_{01} \cdot b_{10} + a_{02}\cdot b_{20} + a_{03} \cdot b_{30}`.

Digital Electronics
-------------------

Assembly Language
-----------------
