Recursive Functions
===================

Topic Summary
-------------

A definition that defines an object in terms of itself is said to be recursive [4].

This summarized all of the topic.

At the first sight the "self-calling function" is hard to be understood. But
recursive exists in natural world everywhere.

This is essential in a mobile phone:

.. image:: ../img/03-Peano_Sierpinski_carpet_4.svg
    :width: 300px

`Image By Hyacinth - Own work, Public Domain <https://commons.wikimedia.org/w/index.php?curid=79215970>`_

.. image:: ../img/03-Flickr_-_cyclonebill_-_Romanesco.jpg
    :width: 320px

`Creative Commons Attribution-Share Alike 2.0 Generic license <https://en.wikipedia.org/wiki/File:Flickr_-_cyclonebill_-_Romanesco.jpg>`_

..
    This image, originally posted to Flickr, was reviewed on 23 December 2009 by
    the administrator or reviewer Multichill, who confirmed that it was available
    on Flickr under the stated license on that date.


To understand recursive function, just keep in mind::

    A function represents a result.

Remember this is enough.

E.g. if :math:`f(n)` is a number, then :math:`f(n-1)` also a number. We can define
more functions like

.. math::

    \begin{array}{cl}
    g(m) & = m ⋅ f(m - 1),\\
    h(s) & = s ⋅ g(s-1),\\
    ...
    \end{array}
..

If you try to implement these functions, you will quickly find that the functions
are exactly the same except the function names. Function :math:`h` calling
:math:`g` is the same as :math:`h` calling itself. So let's merge those into one.

.. math::

    f(n) = n ⋅ f(n-1), \quad\text{if $n > 0$},
..

Here :math:`f()` called itself, that's a recursive function.

We've now defined factorial in recursive style. And this is easy to be implemented
in program.

.. code-block:: python

    # n >= 0
    def f(n: int) -> int:
        if n > 0:
            return n * f(n - 1)
        else:
            return 1
..

The following is how :math:`f(5)` been evaluated.

.. math::

    \begin{array}{cl}
    \hline
	f(n) & = n ⋅ f(n - 1) \\
	\hline
    5! & = 5 ⋅ f(4)_? \\
       & = 5 ⋅ 4 ⋅ f(3)_? \\
       & = 5 ⋅ 4 ⋅ 3 ⋅ f(2)_? \\
       & = 5 ⋅ 4 ⋅ 3 ⋅ 2 ⋅ f(1)_? \\
       & = 5 ⋅ 4 ⋅ 3 ⋅ 2 ⋅ 1 ⋅ f(0)_? \\
       & = 5 ⋅ 4 ⋅ 3 ⋅ 2 ⋅ 1 ⋅ 1 \\
       & = 5 ⋅ 4 ⋅ 3 ⋅ 2 ⋅ 1 \\
       & = 5 ⋅ 4 ⋅ 3 ⋅ 2 \\
       & = 5 ⋅ 4 ⋅ 6 \\
       & = 5 ⋅ 24 \\
       & = 120 \\
	\end{array}
..

The self function call MUST eventually reach the last call.

One last thing to be noted is recursive function doesn't necessarily accept only
one argument. Here is also a recursive function:

.. math::

    f(a, b) =
    \begin{cases}
    f(\frac{a}{2}, \frac{b}{3}),  & \text{if $a$ is even and $b$ > 0} \\
    a + f(a - b, b - 2), & \text{if $a$ is odd and $b$ > 0} \\
    3, & \text{if $$} a, b \leqslant 0
    \end{cases}
..

Examples
--------

TODO handout
