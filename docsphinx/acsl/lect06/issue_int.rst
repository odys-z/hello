Issue 2018 Intermediate
=======================

Problem:
--------

2017-2018
American Computer Science League Contest #4
Intermediate Division Programming Problem: Duplicates

`See here <http://www.datafiles.acsl.org/samples/contest4/c_4_duplicates_int.pdf>`_

SAMPLE INPUT SAMPLE::

    RESET abracadabracabob
    REPORT 3
    REPORT 5
    ADD BATH
    DELETE boa
    REPORT 5
    DELETE drr
    REPORT 5
    RESET American Computer Science League
    ADD Computer
    DELETE Computer
    DELETE COMPUTER
    REPORT 10

OUTPUT::

    1. RC
    2. RO
    3. ROH
    4. ROHRT
    5. UTSRPRS

.. _issue_2018:

Issue:
------

Shouldn't the 5-th output is 'UTSRPRSTU'?

(Add 'Computer', Delete 'Computer' won't affect the sequence)

::

    RESET American Computer Science League
    [('A', 3, 'A'), ('C', 4, 'CEM'), ('E', 6, 'EIM'), ('G', 1, 'GIMR'),
     ('I', 1, 'ILMR'), ('L', 1, 'LMNR'), ('M', 1, 'MNOR'), ('N', 1, 'NOPR'),
     ('O', 1, 'OPR'), ('P', 1, 'PRSTU'), ('R', 1, 'RSTU'), ('S', 1, 'STU'),
	 ('T', 1, 'TU'), ('U', 2, 'U')]


    - CO
    [('A', 3, 'A'), ('C', 4, 'CEM'), ('E', 6, 'EIM'), ('G', 1, 'GIMR'),
     ('I', 1, 'ILMR'), ('L', 1, 'LMNR'), ('M', 1, 'MNOR'), ('N', 1, 'NOPR'),
     ('P', 1, 'POPR'), ('R', 1, 'RPRSTU'), ('S', 1, 'SRSTU'), ('T', 1, 'TSTU'),
     ('U', 2, 'UTU'), ('', 0, 'U')]

    - M
    [('A', 3, 'A'), ('C', 4, 'CEM'), ('E', 6, 'EIM'), ('G', 1, 'GIMR'),
     ('I', 1, 'ILMR'), ('L', 1, 'LMNR'),
     ('N', 1, 'NMNOR'), ('P', 1, 'PNOPR'),
     ('R', 1, 'RPOPR'), ('S', 1, 'SRPRSTU'), ('T', 1, 'TSRSTU'),
     ('U', 2, 'UTSTU'), ('', 0, 'UTU'), ('', 0, 'U')]

    - P
    [('A', 3, 'A'), ('C', 4, 'CEM'), ('E', 6, 'EIM'), ('G', 1, 'GIMR'),
     ('I', 1, 'ILMR'), ('L', 1, 'LMNR'),
     ('N', 1, 'NMNOR'),
     ('R', 1, 'RPNOPR'),
     ('S', 1, 'SRPOPR'), ('T', 1, 'TSRPRSTU'), ('U', 2, 'UTSRSTU'),
     ('', 0, 'UTSTU'), ('', 0, 'UTU'), ('', 0, 'U')]

    - U
    [('A', 3, 'A'), ('C', 4, 'CEM'), ('E', 6, 'EIM'), ('G', 1, 'GIMR'), ('I', 1, 'ILMR'), ('L', 1, 'LMNR'),
     ('N', 1, 'NMNOR'),
     ('R', 1, 'RPNOPR'),
     ('S', 1, 'SRPOPR'), ('T', 1, 'TSRPRSTU'), ('U', 1, 'UTSRSTU'),
     ('', 0, 'UTSTU'), ('', 0, 'UTU'), ('', 0, 'U')]

    - TE
    [('A', 3, 'A'), ('C', 4, 'CEM'), ('E', 5, 'EIM'), ('G', 1, 'GIMR'), ('I', 1, 'ILMR'), ('L', 1, 'LMNR'),
     ('N', 1, 'NMNOR'),
     ('R', 1, 'RPNOPR'),
     ('S', 1, 'SRPOPR'),
     ('U', 1, 'UTSRPRSTU'), ('', 0, 'UTSRSTU'), ('', 0, 'UTSTU'),
     ('', 0, 'UTU'), ('', 0, 'U')]

    - R
    [('A', 3, 'A'), ('C', 4, 'CEM'), ('E', 5, 'EIM'), ('G', 1, 'GIMR'), ('I', 1, 'ILMR'), ('L', 1, 'LMNR'),
     ('N', 1, 'NMNOR'),
     ('S', 1, 'SRPNOPR'),
     ('U', 1, 'USRPOPR'),
     ('', 0, 'UTSRPRSTU'), ('', 0, 'UTSRSTU'), ('', 0, 'UTSTU'),
     ('', 0, 'UTU'), ('', 0, 'U')]
