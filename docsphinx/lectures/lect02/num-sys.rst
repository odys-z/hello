Computer Number Systems
=======================

`ACSL Topic: Computer Number Systems <http://www.categories.acsl.org/wiki/index.php?title=Computer_Number_Systems>`_

.. _l2-comp-num-sys:

Topic Summary
-------------

- Convention

:math:`12345=1×{10^4}+2×{10^3}+3×{10^2}+4×{10^1}+5×{10^0}=10000+2000+300+40+5=12345`

:math:`{175_8}=1×{8^2}+7×{8^1}+5×{8^0}=1×64+7×8+5×1=64+56+5={125_{10}}`

- Color (HTML CSS)

- Special Value

::

    255, -1, -128, 127
    65536, 32767, -32768
    black, white, red, green, blue

Exercise
--------

::

    Convert IP v4 address to Int32.

Example 1. Short Questions
__________________________

See handout *lec01-short-question.pdf*.

::

    q1: Convert octal to Mayan representation.
	...

Example 2. Jr. Programing
_________________________

.. _tutorial-unittest:

Prerequisite: Unit Test
+++++++++++++++++++++++

Eclipse & PyDev come with a build in facility of unit test, module "unittest".

Unittest typically can be used in test case like:

.. code-block:: python

    import unittest

    class Test(unittest.TestCase):
        def testEx1(self):
            self.assertEqual('7145010', s.numTrans('7145032 2 8'))
            self.assertEqual('1540400', s.numTrans('1540670 3 54'))

    t = Test()
    t.ex1()
    print('Test finished successfully!')
..

Now it's time to create a test case. Copy and modify the above snippet into test.py,
save next to conv_64.py, and run with::

    python3 test.py

Or in eclipse,

::

    right click test.py
    -> Debug as
    -> Python Run

Contest Problem
+++++++++++++++

`Junior Division - Number Transformation, ACSL Sample <http://www.datafiles.acsl.org/samples/contest1/C_1_JR_Transform.pdf>`_

Reference Answer `at github <https://github.com/odys-z/hello/blob/master/acsl/lect02/examples/jr2019_contest1.py>`_.

For Your Information:

An other string operation to replace some characters is typically like:

.. code-block:: python

    chars = list("String") # char = ['S', 't', 'r', 'i', 'n', 'g']
    chars[3] = 'o'
    s = ''.join(chars)     # s = 'Strong'
..

And a little bit faster:

.. code-block:: python

    s = "String"
    s = s[:3] + 'o' + s[4:] # s = 'Strong'
..

Example 3. Digital String
_________________________

- Find the correct :math:`P^{th}` number.

TODO ...

See handout.
