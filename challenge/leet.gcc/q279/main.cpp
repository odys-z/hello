/**
 * Q 279. Perfect Squares
 * https://leetcode.com/problems/perfect-squares/
 *
 * Reference Solution:
 * https://leetcode.com/problems/perfect-squares/discuss/71637/Java-solution-O(n12)-time-and-O(1)-space
 *
 * Lagrange's four-square theorem
 * - all numbers can be represented as 4 square number's sum
 * https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem#Historical_development;
 *
 * Legendre's three-square theorem
 * - number can only be sum of 3 numbers can not be the form of 4^n(8m + 7)
 * https://en.wikipedia.org/wiki/Legendre%27s_three-square_theorem
 *
 * A number can be a sum of 2 squares, if and only if the number of prime divisor p mod 4 = 3 is evern.
 * https://math.stackexchange.com/a/787826
 * Since n's divisor <= n^(1/2), n < 10^4, only a few prime divisors are cared about.
 * [3, 7, 11, 19, 23, 31, 43, 47, 59, 67, 71, 79, 83]
 *
 * In hexadecimal, a number can be a squere, the unit digit can only be 0, 4, 9.
 * Which rules out 3/4 of tests.
 * https://www.johndcook.com/blog/2008/11/17/fast-way-to-test-whether-a-number-is-a-square/
 **/
#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <assert.h>

using namespace std;

class Solution {
public:
    /**10%, 25ms
     * @brief numSquares
     * @param n
     * @return
     */
    int numSquares(int n) {

        int m = n;
        while ((m & 3) == 0)
        {
            if ((m & 0x3f) == 0)
                m >>= 4;
            m >>= 2;
        }
        if ((m % 8) == 7)
            return 4;

        vector<int> prime1 = {3, 7, 11, 19, 23, 31, 43, 47, 59, 67, 71, 79, 83};
        vector<int> prime2 = {9, 49, 121, 361, 529, 961, 1849, 2209, 3481, 4489, 5041, 6241, 6889};
        set<int> squares = {1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,361,400,441,
                            484,529,576,625,676,729,784,841,900,961,1024,1089,1156,1225,1296,1369,
                            1444,1521,1600,1681,1764,1849,1936,2025,2116,2209,2304,2401,2500,2601,
                            2704,2809,2916,3025,3136,3249,3364,3481,3600,3721,3844,3969,4096,4225,
                            4356,4489,4624,4761,4900,5041,5184,5329,5476,5625,5776,5929,6084,6241,
                            6400,6561,6724,6889,7056,7225,7396,7569,7744,7921,8100,8281,8464,8649,
                            8836,9025,9216,9409,9604,9801,10000};

        if (squares.find(n) != squares.end())
            return 1;

        int szmod3 = prime2.size();
        for (int p = 0; p < szmod3; p++)
        {
            if (n > prime2[p]) break;
            int rem = n % prime2[p];
            if (rem == 0 and rem % prime1[p] != 0)
                return 2;
        }

        // sorted
        int n_2 = n >> 1;
        for (int a : squares)
        {
            if (a > n_2) break;
            if (squares.find(n - a) != squares.end())
                return 2;
        }
        return n > 2 ? 3 : n;

    }

    /**20%, 391ms
     * Graph:
     * Node n is the root.
     * Edge is the squares to be summed.
     * A node is edge sum from leaf the node.
     *
     * @brief numSqueresBfs
     * @param n
     * @return
     */
    int numSqueresBfs(int n)
    {
        if (n <= 3) return n;
        set<int> edges = { 1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,361,400,
                           441,484,529,576,625,676,729,784,841,900,961,1024,1089,1156,1225,1296,
                           1369,1444,1521,1600,1681,1764,1849,1936,2025,2116,2209,2304,2401,2500,
                           2601,2704,2809,2916,3025,3136,3249,3364,3481,3600,3721,3844,3969,4096,
                           4225,4356,4489,4624,4761,4900,5041,5184,5329,5476,5625,5776,5929,6084,
                           6241,6400,6561,6724,6889,7056,7225,7396,7569,7744,7921,8100,8281,8464,
                           8649,8836,9025,9216,9409,9604,9801,10000 };
        set<bool> visd;
        // vector<bool> visd(10000, false) - according tests, this is actually using less memory.

        queue<int> q, q_;
        q.push(n);
        int step = 0;
        visd.insert(n);

        while (q.size() > 0)
        {
            step++;
            q_ = q;
            while (q_.size() > 0)
            {
                int me = q_.front(); q_.pop(); visd.insert(me);
                for ( int nxt: edges )
                {
                    if (nxt > me) break; // set is sorted by default
                    else if (nxt == n)
                        return step;
                    if (me == nxt)
                        return step;

                    int neibr = me - nxt;
                    if (visd.find(neibr) != visd.end())
                    {
                        q.push(neibr);
                    }
                }
            }
        }

        return step;
    }
};

int main()
{

    Solution s;
    s.numSqueresBfs(6);
    for (int i= 1; i < 10000; i*=2)
    {
        cout << i << " : " << s.numSquares(i) << " " << s.numSqueresBfs(i) << endl;
        cout << i + 1 << " : " << s.numSquares(i + 1) << " " << s.numSqueresBfs(i + 1) << endl;
    }

    for (int i = 1; i <= 10000; i+= i % 23)
        assert(s.numSquares(i) == s.numSqueresBfs(i));

    return 0;
}
