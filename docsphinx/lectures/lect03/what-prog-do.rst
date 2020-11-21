What Does This Program Do?
==========================

`ACSL Topics: What Does This Program Do? <http://www.categories.acsl.org/wiki/index.php?title=What_Does_This_Program_Do%3F>`_

Go Through Problem 3
--------------------

Pseudo Code::

    input H, R
    B = 0
    if H>48 then
        B = B + (H - 48) * 2 * R
        H = 48
    end if
    if H>40 then
       B = B + (H - 40) * (3/2) * R
       H = 40
    end if
    B = B + H * R
    output B

The variables in loops:

.. math::

    \begin{array}{cl}
    \hline
    f(n) & = n ⋅ f(n - 1) \\
    \hline
    \end{array}
..
