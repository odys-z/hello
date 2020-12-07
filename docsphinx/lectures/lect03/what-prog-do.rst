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

Go Through Problem 3
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

::

    J K N Aj Bk Cn
    0 0 0 12 17 0
    0 0 0 12 17 12
    1 0 1 41 17 17
    1 1 2 41 34 34
    1 2 3 41 81 41
    2 2 4 52 81 52
    3 2 5 57 81 57
    4 2 6 77 81 77
    C4: 52

Python3 Validation:

.. code-block:: python

    def wdtpd_problem3(A, B):
        C = [0] * (len(A) * len(B))
        J, K, N = 0, 0, 0
        print('J K N Aj Bk Cn')
        print(J, K, N, A[J], B[K], C[N])
        while A[J] > 0:
            while B[K] < A[J]:
                C[N] = B[K]
                print(J, K, N, A[J], B[K], C[N])
                N = N + 1
                K = K + 1

            C[N] = A[J]
            print(J, K, N, A[J], B[K], C[N])
            N, J = N + 1, J + 1

        C[N] = B[K]
        return C
..

:download:`python3 source file <./wdtpd-p3.py>`

Q6, Intermediate Division
-------------------------

Psedo Code: see * handout: Programming Problem: Agram, 2017, Intermediate *

Python3 Validation:

.. code-block:: python

    def q6():
        a = [0] * 100
        for i in range( 2, 26 ):
            a[i] = i
        print(0, a)

        for k in range( 2, 26 ):
            if a[k] != 0:
                for j in range( 2*k, 26, k ):
                    a[j] = 0
                print(k, a)

        s = 0
        for i in range(26):
            if a[i] > 0:
                s += 1
        print(s)
..
