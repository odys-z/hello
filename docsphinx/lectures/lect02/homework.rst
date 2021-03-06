Homework
========

Task 1 Exercise
---------------

1. If a logic function has three inputs, how many rows must the truth table have
to contain all possible states? Justify your answer.

2. For the following functions, construct a truth table and draw a circuit diagram.

    (a). :math:`y(A,B) = \overline{AB}+\overline{B}`

    (b). :math:`y(A,B,C) = \overline{AC} + BC`

    (c). :math:`y(A,B,C) = (A ⨁ B)\overline{C}`

    (d). :math:`y(A,B,C) = \overline{\overline{A+B}\space\overline{B+C}}`

    (e). :math:`y(A,B,C,D) = \overline{A}B\overline{C} + (A ⨁ B)C + \overline{A}\overline{B}C\overline{D} + ABC`

3. Design a 4-input NAND gate using two 2-input NAND gates and one 2-input NOR
gate. Hint: Use DeMorgan's law.

4. Simplify

:math:`\overline{ABC}+ \overline{AB}C+ \overline{A}B\overline{C}+ A\overline{BC}+ A\overline{B}C`

:math:`\overline{\overline{X\overline{Y} + XYZ} + X (Y + X\overline{Y}) }`

:math:`(A + B)(\overline{A} + C)(B + C)`

:math:`XY + \overline{XZ} + X \overline{Y} Z (XY + Z)`

..
    https://docs.google.com/viewer?a=v&pid=sites&srcid=ZGVmYXVsdGRvbWFpbnxzb3VtZW5jYXxneDozOTY2ZjY5ODNmMzhlZjhl

Answer: :math:`(\overline{A}+\overline{B}+\overline{C}), \quad0, \quad AC+B\overline{A}, \quad1`

Reference

..
    https://ufdcimages.uflib.ufl.edu/AA/00/01/16/38/00001/DigitalLogic.pdf

1. James Feher, Introduction to Digital Logic with Laboratory Exercises, Global
Text. (Creative Commons Attribution 3.0 License, Copyright 2009)

2. DIGITALS ELECTRONICS, TYPICAL QUESTIONS & ANSWERS, `Google Docs <https://docs.google.com/viewer?a=v&pid=sites&srcid=ZGVmYXVsdGRvbWFpbnxzb3VtZW5jYXxneDozOTY2ZjY5ODNmMzhlZjhl>`_.

..
    https://mohduzir.uitm.edu.my/digital/DigitalElectronicsSLC.pdf

3. Tertulien Ndjountche, Sequential and Arithmetic Logic Circuits, Digital
Electronics 2, by John Wiley & Sons, Inc. 2016

Task 2. Debunk CPU Myth
-----------------------

After finished this project, you can get a basic idea about the principal of the
CPU's. And would provide a good understand when starting Assembly Language learning.
(There are much more in a CPU)

..
    http://computerscience.jbpub.com/ecoa/2e/Null03.pdf

Step through the reference examples using *Logisim* to build the logic units:

- Half Adder (One bit ignoring carry)

..
    image:: ../img/02-hafl-adder.png

.. math::

    \begin{array}{|cc|cc|}
    \hline
    Inuts & & Outputs & \\
    \hline
    x & y & Sum & Carray \\
    \hline
    0 & 0 & 0 & 0 \\
    0 & 1 & 1 & 0 \\
    1 & 0 & 1 & 0 \\
    1 & 1 & 1 & 1 \\
    \hline
    \end{array}

- Full Adder (Two bit dealing with carry in & carry out)

.. image:: ../img/02-full-adder.png

- 2 Bits Decoder + Output Selector (The function control)

This is comparable to a Multiplexer. See `Toturialspoint, Multiplexer <https://www.tutorialspoint.com/digital_circuits/digital_circuits_multiplexers.htm>`_.

.. image:: ../img/02-decoder.png

- 2 Bits ALU

.. image:: ../img/02-2bit-alu.png

:download:`Logisim ALU Circuit <../res/lec02-alu.circ>`

The finished ALU can be one like in the above. With the control command been set,
finish the following truth table.

The (t0, t1) and the selector part formed the function control circuit (selecting
usage).

- Arithmetic Add

Set t0, t1 = 0, 0 and verify the following results.

.. math::

    \begin{array}{cc|cc}
    A  & B  & A+B & carry\\
    \hline
    00 & 00 & 00 & 0 \\
    00 & 01 & 01 & 0 \\
    00 & 10 & 10 & 0 \\
    00 & 11 & 11 & 0 \\
    11 & 00 & 11 & 0 \\
    11 & 01 & 00 & 1 \\
    11 & 10 & 01 & 1 \\
    11 & 11 & 10 & 1 \\
    \hline
    \end{array}
..

This shows the 00 comand will have the 2-bit ALU add 2 binary number. If you are
interested, you can try all 4 selected function and complete the function
selection table.

.. math::

    \begin{array}{c|c}
    t1,t0& Function \\
    \hline
    0 0  & A \space + \space  B \\
    0 1  &  \\
    1 0  &  \\
    1 1  &  \\
    \hline
    \end{array}
..

- A step further

If you are interested in this topic, you can read through [4], Chapter 3. See
:ref:`reference section <l2-ref>`.

Task 3 Convert to Base 64
-------------------------

`reference answer <https://github.com/odys-z/hello/tree/master/acsl/lect03/ex02>`_

Task 3 Prefix Expression *
--------------------------

.. attention:: Try this after the lecture of recursive functions.

Let's rewrite the logic with the following operator:

.. math::

   \begin{array}{c|c}
   \hline
   logic & operator\\
   \hline
   NOT & ! \\
   AND & \&  \\
   OR  & | \\
   XOR & \hat \\
   \end{array}
..

Write the first four expression in step 4, task1 in prefix form. E.g (A OR B) AND
X's prefix form is::

    & | A B X.

Then implement a program to evaluate all answers of question 4 in task 1.

Hint: the important data structure for the program is Stack.

Task 4 Reading*
---------------

`ACSL Wiki: Recursive Functions <http://www.categories.acsl.org/wiki/index.php?title=Recursive_Functions>`_
