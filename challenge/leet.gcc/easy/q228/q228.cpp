/**
 * 228. Summary Ranges
 * https://leetcode.com/problems/summary-ranges/description/
 */

#include <vector>
#include <iostream>
#include <string>
#include <numeric>
#include <format>

using namespace std;

class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> v;
        if (nums.size() == 0) return v;

        string s = "";
        int l = nums[0], r = nums[0];

        /*
        reduce(next(nums.begin()), nums.end(), nums[0], [&](int a, int b) {
            if (b == r + 1) 
                r = b;
            else {
                v.push_back(l == r ? to_string(l) : to_string(l) + "->" + to_string(r));
                l = b, r = b;
            }
            return b;
		});
        v.push_back(l == r ? to_string(l) : to_string(l) + "->" + to_string(r));
        */

        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] == r + 1)
                r = nums[i];
            else {
                v.push_back(l == r ? to_string(l) : to_string(l) + "->" + to_string(r));
                l = nums[i], r = nums[i];
            }
        }

        v.push_back(l == r ? to_string(l) : to_string(l) + "->" + to_string(r));
        return v;
    }
};

string reduce(vector<string> v) {
    return reduce(next(v.begin()), v.end(), string("[") + v[0],
        [](string a, string b) { return move(a) + ", " + b; }) + string("]");
}

int main() {
    Solution s;

    vector<int> v;

    v = vector<int> { 0, 1, 2, 4, 5, 7 };
    cout << "0->2, 4->5, 7?" << endl << reduce(s.summaryRanges(v)) << endl;

    v = vector<int> {1, 2};
    cout << "1->2 ?" << endl << reduce(s.summaryRanges(v)) << endl;

    v = vector<int>{1, 2, 4, 5};
    cout << "1->2, 4->5 ?" << endl << reduce(s.summaryRanges(v)) << endl;
}

