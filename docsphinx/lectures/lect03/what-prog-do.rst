What Does This Program Do?
==========================

`ACSL Topics: What Does This Program Do? <http://www.categories.acsl.org/wiki/index.php?title=What_Does_This_Program_Do%3F>`_

Go Through Problem 2
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

.. note: The ACSL topic about the pseudo code defined "/" is real division, and "3/2" = 1.5
..

Go Through Problem 2
--------------------

Pseudo Code::

    A(0) = 12: A(1) = 41: A(2) = 52
    A(3) = 57: A(4) = 77: A(5) = -100
    B(0) = 17: B(1) = 34: B(20 = 81
    J = 0: K = 0: N = 0
    while A(J) > 0
      while B(K) <= A(J)
        C(N) = B(K)
        N = N + 1
        k = k + 1
      end while
      C(N) = A(J): N = N + 1: J = J + 1
    end while
    C(N) = B(K)

Input::

       0   1   2   3   4    5
    A [12, 41, 52, 57, 77, -100]
    B [17, 34, 81]

The variables in loops:

.. math::

    \begin{array}{lllll}
    J, A_J & &  N / N' & \\
    \hline
    J = 0, A_J = 12 \\
        & B_0 = 17 & 0 / 1 & C = 17 \\
        & B_1 = 34 & 1     & \\
        & 	      & 1 / 2 & C = 17, 12 \\
    \hline
    J = 1, A_J = 42 \\
        & B_0 = 17 & 2 & C = 17, 12, 17 \\
        & B_1 = 34 & 3 & C = 17, 12, 17, 34 \\
        & B_2 = 81 & & \\
        &         & 4 / 5 & C = 17, 12, 17, 34, 42 \\
    \hline
    J = 2, A_J = 52 \\
        & B_0 = 17 & 5 & C = 17, 12, 17, 34, 42, 17 \\
        & B_1 = 34 & 6 & C = 17, 12, 17, 34, 42, 17, 34 \\
        & B_2 = 81 & & \\
        &         & 7 / 8 & C = 17, 12, 17, 34, 42, 17, 34, 52 \\
    \hline
    J = 3, A_J = 57 \\
        & B_0 = 17 & 9  & C = 17, 12, 17, 34, 42, 17, 34, 52, 17 \\
        & B_1 = 34 & 10 & C = 17, 12, 17, 34, 42, 17, 34, 52, 17, 34 \\
        & B_2 = 81 \\
        &         & 11 / 12	& C = 17, 12, 17, 34, 42, 17, 34, 52, 17, 34, 57 \\
    \hline
    J = 4, A_J = 77 \\
        & B_0 = 17 & 13 & C = 17, 12, 17, 34, 42, 17, 34, 52, 17, 34, 57, 17 \\
        & B_1 = 34 & 14 & C = 17, 12, 17, 34, 42, 17, 34, 52, 17, 34, 57, 17, 34 \\
        & B_2 = 81 \\
        &         & 14 / 15 & C = 17, 12, 17, 34, 42, 17, 34, 52, 17, 34, 57, 17, 34, 81 \\
    \hline
    J = 5, A_J = -100 \\
        &         & 15 & C = 17, 12, 17, 34, 42, 17, 34, 52, 17, 34, 57, 17, 34, 81, 81 \\
    \end{array}
..
