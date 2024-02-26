/**
 * 1282. Group the People Given the Group Size They Belong To
 * https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
 */

#include <iostream>

#include "utils.h"

using namespace std;

class Solution {
public:
    vector<vector<int>> groupThePeople(vector<int>& groupSizes) {
        vector<vector<vector<int>>> res(501);
        for (int i = 0; i < groupSizes.size(); i++) {
            int sz = groupSizes[i];
            if (res[sz].size() == 0) {
                vector<int> g{};
                res[sz].push_back(g);
            }
            if (((vector<int>)res[sz][0]).size() >= sz) {
                vector<int> vect{ i };
                res[sz].insert(res[sz].begin(), vect);
            }
            else
                res[sz][0].push_back(i);
        }

        vector<vector<int>> resv;
        for (vector<vector<int>> r : res)
            if (r.size() > 0)
                for (vector<int> v : r)
                    resv.push_back(v);
        return resv;
    }
};

/*
int main() {
    Solution s;
    vector<int> n;

    n = vector<int>{ 3,3,3,3,3,1,3 };
    cout << "[[5],[0,1,2],[3,4,6]]?" << endl << reducev(s.groupThePeople(n)) << endl;

    cout << "OK" << endl;
    return 0;
}
*/
