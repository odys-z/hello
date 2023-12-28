/**
 * https://leetcode.com/problems/plus-one/
 */

#include <vector>
#include <iostream>
#include <string>
#include <numeric>

using namespace std;

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int c = 1;
        auto i = digits.end();
        while(i != digits.begin() && c > 0) {
            --i;
            int c0 = (*i + c) / 10;
            *i = (*i + c) % 10;
            c = c0;
        }
        if (c > 0)
            digits.insert(digits.begin(), c);
        return digits;
    }
};

int main() {
    Solution s;
    vector<int> v{1, 2, 3};
    s.plusOne(v);
    string v0;
    cout << reduce(v.begin(), v.end(), v0, [](string a, int b) {
        return move(a) + to_string(b);
    }) << endl;

    v = vector<int>{9};
    s.plusOne(v);
    cout << reduce(v.begin(), v.end(), v0, [](string a, int b) {
        return move(a) + to_string(b);
    }) << endl;
}
