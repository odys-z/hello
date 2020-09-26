Homework
========

Task 1 Boolean Algebra

Task 2. Computer Number Systems

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

.. note:: This lecture using Python3 as programming language. But if you are
    interested in C++, you can use tools like gcc, Qt Creator or Visual Studio etc.
    There is a `Qt project template <https://github.com/odys-z/hello/tree/master/gcc/leetcode/acsl/q1295>`_
    can be used for quickly start LeetCode exercise.
..

Task 3. Digital Electronics
