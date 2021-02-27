Exercise
========

Part 1
------

1. #List `LeetCode Problem 206. Reverse Linked List <https://leetcode.com/problems/reverse-linked-list/>`_

Solution: :download:`q206 <../../../challenge/leet/easy/q206.py>`

2. #List `LeetCode Problem 83. Remove Duplicates <https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/>`_

Solution: :download:`q083 <../../../challenge/leet/easy/q083.py>`

3. #DP `LeetCode Problem 303 <https://leetcode.com/problems/range-sum-query-immutable/submissions/>`

Solution: :download:`q303 <../../../challenge/leet/easy/q303.py>`

4. #Math `LeetCode Problem 1551. Minimum op for Equal <https://leetcode.com/problems/minimum-operations-to-make-array-equal/submissions/>`_

Solution: :download:`q1551 <../../../challenge/leet/medium/q1551.py>`

Part 2
------

1. #Backtracking `LeetCode Problem 303. Subsets <https://leetcode.com/problems/subsets/>`_

Solution: :download:`q078 <../../../challenge/leet/medium/q078.py>` &
:download:`java version <../../../challenge/leet.java/src/leet/java/medium/Q078.java>`,

2. #Backtracking #Pemutation `LeetCode Problem 784. Letter Case Permutation <https://leetcode.com/problems/letter-case-permutation/>`_

Solution: :download:`q784 <../../../challenge/leet/medium/q784.py>` &
:download:`java version <../../../challenge/leet.java/src/leet/java/medium/Q784.java>`,
:download:`c++ version <../../../challenge/leet.gcc/q784/q784.h>`,

3. #DP `LeetCode Problem 1314. Matrix Block Sum <https://leetcode.com/problems/matrix-block-sum/>`_

Hint::

    Cumulative Sum;
    Inclusion & Exclusion

Solution: :download:`q784 <../../../challenge/leet/medium/q1314.py>`

Part X
------

x1. `ABC, C#3 2015/2016 ACSL Intermediate <http://www.datafiles.acsl.org/samples/contest3/abc_3_int.pdf>`_

Hint: read this carefully::

    These letters (outside letters) tell that that letter will be the first found
    in that row or column starting from that direction.

Solution: :download:`C3 2016, Intermediate <../../../acsl-pydev/acsl/lect05/abc_int.py>`

x2. `STRECH, C#3 2018/2019 ACSL Senior <>`_

Hint1: Can not touch - 'ABCBCB' is wrong answer::

    1   2  3  4  5  6  7  8  9 10
    o   A  o  o 15 16 17 18 19 20
    21 22 23  B 25 26  o  o 29 30
    31 32 33  o  o 36  B  C  o  o
    41 42 43 44  C  o  o [] []  B
    51 52 53 54 55 56 57 58 59  o

Hint2: This is not a path searching or DP problem::

    Pieces are placed in alphabetical order. If a piece does not fit, skip it
    and use the next piece that fits. When Piece E is either used or skipped,
    then begin again with Piece A.

Hint3: Also not a backtracking::

    We guarantee that if a piece can be placed, then that will be the only
    location that it can be placed.

Start here::

    How can A, B, C, D, E piece's shape, tiles been represented in program?

Tried Solution: :download:`C3 2019, Senior <../../../acsl-pydev/acsl/lect05/stretch_sr.py>`
with issue on test case.

input::

    9, 12, 108, 5, 69, 106, 77, 91, 55

expected::

    CECDEC

But first step should b 'B'?

A step by step tried recordings::

    -------------- Initialized --------------------
     1   2   3   4   5   6   7   8   9  10  11  12
    13  14  15  16  17  18  19  20  21  22  23  24
    25  26  27  28  29  30  31  32  33  34  35  36
    37  38  39  40  41  42  43  44  45  46  47  48
    49  50  51  52  53  54 [ ]  56  57  58  59  60
    61  62  63  64  65  66  67  68 [ ]  70  71  72
    73  74  75  76 [ ]  78  79  80  81  82  83  84
    85  86  87  88  89  90 [ ]  92  93  94  95  96
    97  98  99 100 101 102 103 104 105 [ ] 107 108

    --------- C does not fit next to [ ] ----------
     1   2   3   4   5   6   7   8   9  10  11  12
    13  14  15  16  17  18  19  20  21  22  23  24
    25  26  27  28  29  30  31  32  33  34  35  36
    37  38  39  40  41  42  43  44  45  46  47  48
    49  50  51  52  53  54 [ ]  56  57  58  59  60
    61  62  63  64  65  66  67  68 [ ]   o  71  72
    73  74  75  76 [ ]  78  79  80  81   C   o   o
    85  86  87  88  89  90 [ ]  92  93  94  95   B
    97  98  99 100 101 102 103 104 105 [ ] 107   o

    --------------------- BDE ----------------------
     1   2   3   4   5   6   7   8   9  10  11  12
    13  14  15  16  17  18  19  20  21  22  23  24
    25  26  27  28  29  30  31  32  33  34  35  36
    37  38  39  40  41  42   o   E  45  46  47  48
    49  50  51  52  53  54 [ ]   E   o   o   D  60
    61  62  63  64  65  66  67  68 [ ]  70   D  72
    73  74  75  76 [ ]  78  79  80  81  82   o   o
    85  86  87  88  89  90 [ ]  92  93  94  95   B
    97  98  99 100 101 102 103 104 105 [ ] 107   o

    ------------------- BDEAB(-B) ------------------
    - then D - The one and only tile allowed to touch the opposite side is a circle tile.

     1   2   3   4   5   6   7   8   9  10  11  12
    13  14   o  16  17  18  19  20  21  22  23  24
    25  26   B  28  29  30  31  32  33  34  35  36
     o   D   o   o   A   o   o   E  45  46  47  48
    49   D   B  52  53  54 [ ]   E   o   o   D  60
    61   o   o  64  65  66  67  68 [ ]  70   D  72
    73  74  75  76 [ ]  78  79  80  81  82   o   o
    85  86  87  88  89  90 [ ]  92  93  94  95   B
    97  98  99 100 101 102 103 104 105 [ ] 107   o

Helpful python script:

.. code-block:: python3

    for i in range(1, 10):
        for j in range(1, 13):
            c = (i-1) * 12 + j
            if c in [69, 106, 77, 91, 55]:
                print("[ ]", end = ' ')
            else:
                print("{:3d}".format(c), end=' ')
        print('')
..
