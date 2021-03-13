#ifndef Q1130_H
#define Q1130_H

#include <vector>
#include <limits.h>

using namespace std;

class Solution {
public:
    int mctFromLeafValues(vector<int>& arr) {
        int res = 0;

        while (arr.size() >= 2) {
            int min = INT_MAX;
            int mnx = -1;
            int replace = 0;
            for (int i = 1; i < arr.size(); i++) {
                if (min > arr[i] * arr[i-1]) {
                    min = arr[i] * arr[i-1];
                    mnx = i;
                    replace = max(arr[i], arr[i-1]);
                }
            }
            res += min;
            arr[mnx - 1] = replace;
            arr.erase(arr.begin() + mnx);
        }
        return res;
    }
};

#endif // Q1130_H
