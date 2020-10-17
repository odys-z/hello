Homework (2 tasks)
==================

Prerequisite
------------

You need a better IDE - PyDev

1. Download Eclipse

.. image:: ../img/01-download-eclipse.png

2. Install PyDev Plugin.

Install via Eclipse Marketplace::

    Help -> Eclipse Marketplace...

Search for *PyDev*.

.. image:: ../img/01-eclipse-plugin.png

Tip: install PyDev with offline package.

Follow `this <https://stackoverflow.com/a/11620013>`_.

3. Debug with PyDev

- create a new PyDev Project

- create a PyDev Module, add source file fibonacci.py

- run & debug

If there are problem, see :ref:`Tutorial: run & debug fibonacci.py<dubg-fibonacci>`.

Task: fix the above problem
---------------------------

Try a very large number N and figure out why and how to fix the problem.

Programming Task
----------------

1. Factorial
____________

Implement a program that takes user's input, an integer and output the factorial
result.

In mathematics, the factorial of a positive integer n, denoted by n!, is the
product of all positive integers less than or equal to n:

:math:`{n!=n\cdot (n-1)\cdot (n-2)\cdot (n-3)\cdot \cdots \cdot 3\cdot 2\cdot 1\,.}`

For example,

:math:`{5!=5\cdot 4\cdot 3\cdot 2\cdot 1=120\,.}`

The value of 0! is 1, according to the convention for an empty product.


2. Read Your Mind
_________________

Implement a game of *read your mind*, played like Tic-tac-toe.

About the game
++++++++++++++

Find out what's the game:

`example: a javascript implementation <https://www.cnblogs.com/sgs123/p/10829944.html>`_

..
    http://www.inforise.com.cn/acsl-prog = hello/acsl

Before reading through the source, you are recommended try
`a playable version <http://www.inforise.com.cn/acsl-prog/lect01/read-your-mind/game.html>`_.

.. note:: It's essential to understand math behind the game.
    To be a good programmer, you almost always thinks in math.
..

Goal
++++

- Print it out in the tic-tac-toe style. Show what's your program can guess.

- A short answer about the math principle.
