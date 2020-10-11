#ifndef Q1404_H
#define Q1404_H

#include <string>
#include <iostream>

using namespace std;

class Q1404_ACSL_Easy
{
public:
    Q1404_ACSL_Easy();

    int numSteps(string s) {
        int c = 0;
        int v = stoi(s, nullptr, 2);
        // cout << v << endl;
        while (v != 1)
        {
            if ((v & 1) == 1)
                v ++;
            else v = v >> 1;
            c++;
        }
        return c;
    }
};

/**
 * @brief The Q1404 class
 * https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/
 *
 * 1404. Number of Steps to Reduce a Number in Binary Representation to One
 * Medium
 *
 */
class Q1404
{
public:
    Q1404();

    /** s can longer than 32
     *
     * Runtime: 0 ms, faster than 100.00% of C++ online submissions for
     * Number of Steps to Reduce a Number in Binary Representation to One.
     *
     * Memory Usage: 6.7 MB, less than 25.39% of C++ online submissions for
     * Number of Steps to Reduce a Number in Binary Representation to One.
     */
    int numSteps(string s) {
        int c = 0;
        int ix = s.length() - 1;
        while(ix >= 0)
        {
            if (ix == 0 && s[ix] == '1') // it's '1'
                break;

            c++;

            if (s[ix] == '1')
            {
                int overflow = inc(s, ix);
                if (overflow > 0)
                {   c += ix + 1;
                    break;
                }
            }
            else ix--;
        }
        return c;
    }

    // return overflow
    int inc(string& s, int ix) {
        s[ix] = '0';
        int carry = 1;
        ix--;

        while(carry == 1 && ix >= 0)
        {
            if (s[ix] == '1')
            {
                s[ix] = '0';
                carry = 1;
            }
            else
            {
                s[ix] = '1';
                carry = 0;
            }
            ix--;
        }

        return carry;
    }
};

#endif // Q1404_H
