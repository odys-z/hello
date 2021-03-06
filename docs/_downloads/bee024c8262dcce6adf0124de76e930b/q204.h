#ifndef Q204_H
#define Q204_H

#include <vector>
using namespace std;

class Q204
{
public:
    Q204();

    /** 20.63%
     * @brief countPrimes
     * @param n
     * @return
     */
    int countPrimes(int n) {
        if (n <= 1) return 0;

        vector<int> prims(n+1);
        fill(prims.begin(), prims.end(), 1);
        prims[0] = prims[1] = prims[n] = 0;
        for (int i = 2; i < n; i++)
            for (int j = 2; j <= i; j++)
                if (i * j <= n)
                    prims[i * j] = 0;
                else break;

        int zeros = 0;
        for(int i = 2; i < n; i++) {
            zeros += prims[i];
        }
        return zeros;
    }
};

#endif // Q204_H
