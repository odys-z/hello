/**
 * 2610. Convert an Array Into a 2D Array With Conditions
 * https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description/
 */
#include <vector>
#include <map>
#include <iostream>

#include "utils.h"

using namespace std;

class Solution {
public:
    vector<vector<int>> findMatrix(vector<int>& nums) {
        vector<int> m(201);
        map<int, int> idx;
        vector<vector<int>> res;

        for (int n : nums) {
            int ix = m[n];
            m[n]++;

            if (idx.find(ix) == idx.end()) {
                idx[ix] = res.size();
                res.push_back(vector<int>{});
            }
            res[ix].push_back(n);
        }
        return res;
    }
};

/*
int main() {

    Solution s;
    vector<int> arr;
    
    arr = vector<int>{ 1,3,4,1,2,3,1 };
    cout << "[1,3,4,2], [1,3], [1] ?" << endl << reducev(s.findMatrix(arr)) << endl;

    arr = vector<int>{ 1,2,3,4 };
    cout << "[1,2,3,4] ?" << endl << reducev(s.findMatrix(arr)) << endl;

    cout << "ok" << endl;
    return 0;
}
*/