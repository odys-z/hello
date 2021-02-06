C#2 Programming Problem
=======================

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
