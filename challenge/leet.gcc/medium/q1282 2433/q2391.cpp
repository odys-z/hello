/***
 * 2391. Minimum Amount of Time to Collect Garbage
 * https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/description/
 */

#include <vector>
#include <algorithm>
#include <iostream>
#include <cassert>

using namespace std;

class Solution {
public:
    int garbageCollection(vector<string>& garbage, vector<int>& travel) {
        for (int t = 1; t < travel.size(); t++)
            travel[t] += travel[t - 1];

		int g0 = count_if(garbage[0].begin(), garbage[0].end(), [](char c) { return c == 'G'; });
		int p0 = count_if(garbage[0].begin(), garbage[0].end(), [](char c) { return c == 'P'; });
		int m0 = count_if(garbage[0].begin(), garbage[0].end(), [](char c) { return c == 'M'; });
        int tg = 0, tp = 0, tm = 0;

        for (int t = 1; t < garbage.size(); t++) {
            int g = count_if(garbage[t].begin(), garbage[t].end(), [](char c) { return c == 'G'; });
            int p = count_if(garbage[t].begin(), garbage[t].end(), [](char c) { return c == 'P'; });
            int m = count_if(garbage[t].begin(), garbage[t].end(), [](char c) { return c == 'M'; });

            tg = g > 0 ? travel[t-1] : tg;
            tm = m > 0 ? travel[t-1] : tm;
            tp = p > 0 ? travel[t-1] : tp;
            g0 += g;
            p0 += p;
            m0 += m;
        }

        return tg + tm + tp + g0 + m0 + p0;
    }
};

int main() {
    Solution s;
    vector<string> garbage;
    vector<int> travel;

    garbage = vector<string>{ "G","P","GP","GG" };
    travel = vector<int>{ 2, 4, 3 };
    assert(21 == s.garbageCollection(garbage, travel));


    garbage = vector<string>{ "MMM","PGM","GP" };
    travel = vector<int>{ 3, 10 };
    assert(37 == s.garbageCollection(garbage, travel));

    cout << "ok 2391" << endl;
    return 0;
}