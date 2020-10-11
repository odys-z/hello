Homework
========

Prequisite: Unit Test
---------------------

TDD stands for an important software engineering practice, Test Driven Development.
We need setup Python unit test helper to test our program.

Using unit test in Python is very simple: import, run your program & assert the
results. Here is the `tester of a LeetCode solution <https://github.com/odys-z/hello/blob/master/acsl/lect03/leetcode.py/test.py>`_.

.. code-block:: python

    import unittest
    from q1404 import Solution

    class Test(unittest.TestCase):
    def q1404(self):
        s = Solution()
        self.assertEqual(0, s.numSteps('1'))
        self.assertTrue(5 == s.numSteps('1111'))

    t = Test()
    t.q1404()
..

The *assert...* functions take what's it expected for assertion. If your program
results are not the same as expected, the test function, here the function q1404(),
will throw an exception - program stopped with error.

You should always use the method to test your program. It's efficient and convenient
once you get familiar with it.

Task 1 Sample Programming Problem
---------------------------------

2019-20 Contest #1

Intermediate - Number Transform

PROBLEM:

Given a positive integer (call it N) and a position in that integer (call it P)
transform N.  To transform N, find the :math:`P^{th}` digit of N from the right.
Replace each of the digits to the left of the :math:`P^{th}` digit by the sum of
that digit and the :math:`P^{th}` digit.  If the sum is greater than 9, use just
the units digits (see the second example below).  Replace each of the digits to
the right of the :math:`P^{th}` digit by the absolute value of the difference
between it and the :math:`P^{th}` digit. Do not change the :math:`P^{th}` digit.

Example 1:

N=102439, P=3.

Answer is: :math:`(1+4)(0+4)(2+4)4(|3-4|)(|9-4|) => 546415`

Example 2:

N=4329, P=1.

Answer is: :math:`(4+9)(3+9)(2+9)9 => (13)(12)(11)9 => 3219`

INPUT:

There will be 5 sets of data. Each set contains two positive integers: N and P.
N will be less than :math:`10^{15}`, and P will be valid. No input will cause an
output to have a leading digit of 0.

OUTPUT:

The transformed value of each input set. The printed number may not have any
spaces between the digits.

SAMPLE INPUT:

(http://www.datafiles.acsl.org/2020/contest1/int-sample-input.txt) ::

    296351 5
    762184 3
    45873216 7
    19750418 6
    386257914 5

SAMPLE OUTPUT::

    1. 193648
    2. 873173
    3. 95322341
    4. 86727361
    5. 831752441

Task 2. Number / String Replacement
-----------------------------------

`LeetCode 1295. Find Numbers with Even Number of Digits, <https://leetcode.com/problems/find-numbers-with-even-number-of-digits/>`_

A C++ Reference (Faster than 96%)

.. code-block:: c++

    class Solution {
    public:
        int findNumbers(vector<int>& nums) {
            int cnt = 0;
            for(auto it = begin(nums); it != end(nums); ++it) {
                int n = *it;
                while (n >= 100) n /= 100;
                if (n >= 10)
                    cnt++;
            }
            return cnt;
        }
    };
..

This program use dividing by 100 to search two digits a time.

.. note:: This lecture using Python3 as programming language. But if you are
    interested in C++, you can use tools like gcc, Qt Creator or Visual Studio etc.
    There is a `Qt project template <https://github.com/odys-z/hello/tree/master/gcc/leetcode/acsl/q1295>`_
    which can be used for quickly start LeetCode exercise.
..

Task 2 Round 2 (Advanced)

`LeetCode 833. Find And Replace in String <https://leetcode.com/problems/find-and-replace-in-string/>`_

* They have solution *

Task 3. Replace Chars
---------------------

`LeetCode 1576. Replace All ?'s to Avoid Consecutive Repeating Characters <https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/>`_

Task 4. Replace String*
-----------------------

`LeetCode 833. Find And Replace in String <https://leetcode.com/problems/find-and-replace-in-string/>`_
