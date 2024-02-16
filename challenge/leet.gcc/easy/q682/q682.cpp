/**
 * 682. Baseball Game
 * https://leetcode.com/problems/baseball-game/ 
 */

#include <vector>
#include <string>
#include <iostream>
#include <numeric>
#include <algorithm>
#include <cassert>

using namespace std;

/** 100% */
class Solution {
public:
    int calPoints(vector<string>& operations) {
        vector<int> buf{ 0 };
        int p = 0;

        while (p < operations.size()) {
            if (operations[p] == "C") {
                buf.pop_back();
            }
            else if (operations[p] == "D") {
                buf.push_back(buf.back() * 2);
            }
            else if (operations[p] == "+") {
                int _2 = buf[buf.size() - 2];
                buf.push_back(buf.back() + _2);
            }
            else {
                buf.push_back(stoi(operations[p]));
            }
            p++;
        }

        return accumulate(buf.begin(), buf.end(), 0);
    }
};

int main() {
    Solution s;
    vector<string> ops;

    ops = vector<string>{ "1","2","3" };
    assert(6 == s.calPoints(ops));

    cout << "OK!";
}