Whad does the Program Do
========================

Example 1:

Intermediate, 2019, Question 5

.. code-block:: python

    def q5(a, b, c, d, e):
        if a + b > c / e:
            b = a - b
        else:
            c = c * c
        print('1:', a, b, c, d, e)

        if a / b == c / b :
            a = b + 2 * e
        else:
            d = b ** 2
        print('2:', a, b, c, d, e)

        if a > b and c > d :
            e = d / b
        else:
            b = a + c / e
        print('3:', a, b, c, d, e)

        if a + c > d * e or b / c == b / (2 * a):
            b = a - e
        else: c = b - c
        print('4:', a, b, c, d, e)

        if a < b or c < d and b + e == a:
            d = d - c
        else: c = c / a
        print('5:', a, b, c, d, e)

        print('x:', c / ( b + e) - d ** 2 + a / e)

    q5(10, 5, 20, 1, 2)
..

output::

    1: 10 5 20 1 2
    2: 10 5 20 25 2
    3: 10 20.0 20 25 2
    4: 10 8 20 25 2
    5: 10 8 20 5 2
    x: -18.0

The given solution shouldn't correct as e can not be 0.

