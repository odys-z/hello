C#2 Programming Problem
=======================

2018-2019 Sample, Senior
------------------------

See `ACSL Sample Problem <http://www.datafiles.acsl.org/samples/contest2/c2-int-prog.pdf>`_

::

    2018-2019 AMERICAN COMPUTER SCIENCE LEAGUE
    Contest #2
    Intermediate Division - Diff

**PROBLEM**::

    A useful computer utility is to report the differences between two files. In
    this program, you will compare two strings to find common substrings.

    The following algorithm will be used: Consider each character in turn in the
    first string. If it appears in the second string, add it to a resulting common
    string and delete all characters in the second string up to and including
    that character.

    For example, the common string from abcddef to vdfaddwf is addf. The common
    string from *vdfaddwf* to *abcddef* is *df*.

    INPUT:
    5 lines of data. Each line will contain two strings, A and B. The strings
    will contain letters only and the strings will be separated by a single blank.
    Each string will have fewer than 64 characters.

    OUTPUT:
    For each line, find the common string from A to B and from B to A going from
    left to right. Then repeat the process going from right to left. This will
    produce 4 common strings. Print in alphabetical order all of the different
    letters that are contained in all 4 common strings. If there are none that
    are common to all 4 strings, print “NONE”.

**SAMPLE INPUT**::

    http://www.datafiles.acsl.org/2019/contest2/int-sample-input.txt

    abcddef vdfaddwf
    friends afraid
    delicious indiginous
    shalom saaalaaam
    happy shipshape

**SAMPLE OUTPUT**::

    1. df
    2. dfir
    3. iosu
    4. ams
    5. hp

Solution: :download:`C2 Sample Problem (local) <../../../acsl-pydev/acsl/lect04/sampleprog.py>`

2020-2021 Sample, Intermediate
------------------------------

Problem: See handout 2021 Passort Number.

Code Template:

.. code-block:: python3

    from unittest import TestCase

    def passport(pn: str) -> int:
        # your code here!!!
        pass

    if __name__ == "__main__":
        t = TestCase()
        t.assertEqual(0, passport('A'))
        t.assertEqual(6, passport('ASORTING'))
        t.assertEqual(0, passport('AA'))
        t.assertEqual(0, passport('AAC'))
        t.assertEqual(1, passport('ACA'))
        t.assertEqual(0, passport('ACC'))
        t.assertEqual(1, passport('CBC'))
        t.assertEqual(1, passport('CBA'))
        t.assertEqual(2, passport('DCBA'))
        t.assertEqual(3, passport('DABC')) # ADBC ACBD ABCD

        print('OK!')

Solution: :download:`C2 Sample Problem, 2021, Intermediate (local) <../../../acsl-pydev/acsl/lect04/passport_int.py>`
