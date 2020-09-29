Homework
========

1. Problem Solving
------------------

2. Debunk CPU Myth
------------------

After finished this project, you can get a basic idea about the principal of the
CPU's. And would provide a good understand when starting Assembly Language learning.
(There are much more in a CPU)

..
    http://computerscience.jbpub.com/ecoa/2e/Null03.pdf

Reference: `Essentials of Computer Organization and Architecture, Second Edition, Chapter 3 Boolean Algebra and Digital Logic, Section 3.5.2 Examples of Typical Combinational Circuits <http://computerscience.jbpub.com/ecoa/2e/>`_

Step through the reference examples using *Logisim* to build the logic units::

    Half Adder (One bit ignoring carry)
	Full Adder (Two bit dealing with carry in & carry out)
	2 Bit Decoder + Output Selector (The function control)
	2 Bit ALU

The finished ALU can be one like in the reference. With the control command been
set, try the following truth table.

- Arithmetic Add

.. math::

    \begin{array}{cc|cc}
	A  & B  & A+B & carry\\
	\hline
	00 & 00 & 00 & 0\\
	00 & 01 &    & 0\\
	00 & 10 &    & 0\\
	00 & 11 &    & 0\\
	11 & 00 &    & 0\\
	11 & 01 &    & 0\\
	11 & 10 &    & 0\\
	11 & 11 &    & 0\\
	\hline
	\end{array}
..

If you are interested, you can finish all 4 calculation's truth tables.
