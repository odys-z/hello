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

    \begin{array}{lllll}
    J, Aj & &  N / N' & \\
    \hline
    J = 0, Aj = 12 \\
        & B0 = 17 & 0 / 1 & C = 17 \\
        & B1 = 34 & 1     & \\
        & 	      & 1 / 2 & C = 17, 12 \\
    \hline
    J = 1, Aj = 42 \\
        & B0 = 17 & 2 & C = 17, 12, 17 \\
        & B1 = 34 & 3 & C = 17, 12, 17, 34 \\
        & B2 = 81 & & \\
        &         & 4 / 5 & C = 17, 12, 17, 34, 42 \\
    \hline
    J = 2, Aj = 52 \\
        & B0 = 17 & 5 & C = 17, 12, 17, 34, 42, 17 \\
        & B1 = 34 & 6 & C = 17, 12, 17, 34, 42, 17, 34 \\
        & B2 = 81 & & \\
        &         & 7 / 8 & C = 17, 12, 17, 34, 42, 17, 34, 52 \\
    \hline
    J = 3, Aj = 57 \\
        & B0 = 17 & 9  & C = 17, 12, 17, 34, 42, 17, 34, 52, 17 \\
        & B1 = 34 & 10 & C = 17, 12, 17, 34, 42, 17, 34, 52, 17, 34 \\
        & B2 = 81 \\
        &         & 11 / 12	& C = 17, 12, 17, 34, 42, 17, 34, 52, 17, 34, 57 \\
    \hline
    J = 4, Aj = 77 \\
        & B0 = 17 & 13 & C = 17, 12, 17, 34, 42, 17, 34, 52, 17, 34, 57, 17 \\
        & B1 = 34 & 14 & C = 17, 12, 17, 34, 42, 17, 34, 52, 17, 34, 57, 17, 34 \\
        & B2 = 81 \\
        &         & 14 / 15 & C = 17, 12, 17, 34, 42, 17, 34, 52, 17, 34, 57, 17, 34, 81 \\
    \hline
    J = 5, Aj = -100 \\
        &         & 15 & C = 17, 12, 17, 34, 42, 17, 34, 52, 17, 34, 57, 17, 34, 81, 81 \\
    \end{array}
..
