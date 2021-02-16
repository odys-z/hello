#ifndef INTER_H
#define INTER_H

#include <string>
#include <iostream>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

class AscInter
{
public:
    /** SAMPLE INPUT:                             <--	     SAMPLE OUTPUT:
        1. 1314159265		   |	 3 (14 15 92 6 5)	  |  1. 3 5 6 29 51
        2. 11223344			   |	 1 (223 34 4)		  |  2. 1 4 43 322
        3. 225897257		   |	25 (8 972 57)		  |  3. 25 75 279
        4. 412342987656784352  |  1234 (29876 5678 4352)  |  4. 1234 2534 8765 67892
        5. 33984567176534321   |   398 (45671 7653 4321)  |  5. 398 1234 3567 17654
     * @brief leastNums
     * @param snum
     * @return
     */
    string leastNums(string snum) {
        vector<int> res;
        size_t l = size_t(stoi(snum.substr(0, 1)));
        int least = stoi(snum.substr(1, l));
        snum = snum.substr(l+1);
        snum = string(snum.rbegin(), snum.rend());  // reverse
        size_t i = 0;
        while (least != INT_MIN) {
            res.push_back(least);

            // find next least
            int nxt = INT_MIN;
            while (l+i-1 <= snum.size()) {
                if (l > 1 and snum[i] == '0') {
                    i += 1;
                    continue;
                }
                nxt = stoi(snum.substr(i, l));
                if (nxt <= least)
                    l += 1;
                else {
                    i += l;
                    break;
                }
            }
            if (nxt != INT_MIN and least < nxt)
                least = nxt;
            else least = INT_MIN;
        }

        // join int vector into string
        std::stringstream result;
        auto it = res.begin();
        result << (int)*it++;
        for (; it != res.end(); it++) {
            result << ' ';
            result << (int)*it;
        }
        string restr = result.str();

        // cout << restr;
        return restr;
    }
};

#endif // INTER_H
