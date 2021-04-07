#ifndef Q1641_H
#define Q1641_H

#include <string.h>
#include <numeric>
using namespace std;

/**100.00%
 * @brief The Solution class
 */
class Solution {
public:
    int countVowelStrings(int n) {
        if (n < 1) return 0;
        else if (n == 1) return 5;
        else {
            long pn_1[] = {1, 1, 1, 1, 1};
            long pn[] = {0, 0, 0, 0, 0};
            int i = 2;
            while (i <= n) {
                for (int v = 0; v < 5; v++)
                    pn[v] = accumulate(pn_1+v, pn_1+5, pn[v]);
                swap(pn, pn_1);
                memset(pn, 0, sizeof(pn));
                i++;
            }
            n = 0;
            return accumulate(pn_1, pn_1+5, n);
        }
    }
};

#endif // Q1641_H
