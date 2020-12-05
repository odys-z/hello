Examples
========

- `LeetCode q231 <https://leetcode.com/problems/power-of-two/submissions/>`_

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

- Agram 2017 Intermediate

See handout.

Reference Answer

.. code-block:: python

    def agram2(cards):
        '''
            scan without sort
            -----------------
        '''
        # for compare King, Queen, Jack, Ten, ...
        rule = {
            'A': 1, '2': 2, '3': 3, '4': 4, '5': 5,
            '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10,
            'J': 11, 'Q': 12, 'K': 13 }

        suit = []         # greater ranks in the suit
        s, r = cards[0][1], rule[cards[0][0]]# spade, rank

        least_r, least_card = 14, None # minimal higher rank than card 0
        min_r, min_card = 14, None     # minimal rank & card of all cards
        min_s, min_suit = 14, None     # minimal rank & card of the suit

        for x in range(1, len(cards)):
            rx = rule[cards[x][0]]     # rank of card x
            if cards[x][1] == s:
                if r < rx:
                    if least_r > rx:
                        least_r = rx;
                        least_card = cards[x]
                if min_s > rx:
                    min_s = rx
                    min_suit = cards[x]

            if min_r > rx:
                min_r = rx
                min_card = cards[x]

        if least_card is not None:
            return least_card
        elif min_suit is not None:
            return min_suit
        else:
            return min_card
..
