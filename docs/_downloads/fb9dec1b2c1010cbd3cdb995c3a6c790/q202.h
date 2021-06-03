#ifndef Q202_H
#define Q202_H

#include <map>
#include <iostream>

using namespace std;

// 1: true, 0: false, -1: unkown
map<int, int> dp; //{{1, 1}, {10, 1}, {100, 1}};

/**
 * @brief 52.99%
 */
class Solution {
public:
    bool isHappy(int n) {
        dp = map<int, int> {{1, 1}, {10, 1}, {100, 1}, {1000, 1}, {10000, 1}};
        tryHappy(dp, n);
        return dp[n];
    };

    bool tryHappy(map<int, int> &dp, int n) {
        if (dp.count(n))
            return dp[n];
        else {
            dp[n] = -1;
            int e2sum = 0, n0 = n;

            while (n > 9) {
                int r = n % 10;
                e2sum += r * r;
                n /= 10;
            }
            e2sum += n * n;

            if (dp.count(e2sum) && dp[e2sum] == -1) {
                dp[e2sum] = 0;
                return 0;
            }

            int happy = tryHappy(dp, e2sum);
            dp[n0] = happy;
            return happy;
        }
    }
};
#endif // Q202_H
