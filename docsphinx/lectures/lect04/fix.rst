Topics
======

Prefix/Infix/Postfix
--------------------

`ACSL Topic: Prefix/Infix/Postfix <http://www.categories.acsl.org/wiki/index.php?title=Prefix/Infix/Postfix_Notation>`_

The algorithm to evaluate an infix expression is complex.

Infix needs a stack to parse expression, as it must address the order of precedence.

::

    a + b * c

    stack:
    +       *
            +

    ab      abc    -> a  bc*  +

Example:

Postfix: :math:`X=(AB− \frac{C}{D} )^E`

::

    = X ↑ - * A B / C D E

Check `ACSL Topics <http://www.categories.acsl.org/wiki/index.php?title=Prefix/Infix/Postfix_Notation>`_
for more examples.

Bit-string Flicking
-------------------

`ACSL Topic: Bit-String Flicking <http://www.categories.acsl.org/wiki/index.php?title=Bit-String_Flicking>`_

Bitwise Operators::

    NOT AND OR XOR

Shift Operators::

    (LSHIFT-2 x)    (RSHIFT-3 x)    (LCIRC-3 x)    (RCIRC-1 x)

LISP
----

LISP is one of the simplest computer languages

Read this carefully:

`ACSL Topic: LISP <http://www.categories.acsl.org/wiki/index.php?title=LISP>`_

Example::

    (SETQ X '(((a (b c) d) e)((b (c (d e) b)) a)(a b c)((e d) b (a b)(c e d))))

	Evaluate the following expression

    (CDR(CDR(CDR(REVERSE(CAR(REVERSE(CDR X)))))))


Answer: (e d)

1 X :

::

    ((a (b c) d) e)    ((b (c (d e) b)) a)    (a b c)    ((e d) b (a b)(c e d))

2 (CDR X)::

    ((b (c (d e) b)) a)    (a b c)    ((e d) b (a b)(c e d))

3 (CAR(REVERSE(CDR X)))::

    ((e d) b (a b) (c e d))

4 (CDR(REVERSE(CAR(REVERSE(CDR X)))))::

    ((a b) b (e d))

5 (CDR(CDR(CDR(REVERSE(CAR(REVERSE(CDR X)))))))::

    (e d)
