/**
 * 594. Longest Harmonious Subsequence
 * https://leetcode.com/problems/longest-harmonious-subsequence/description/
 */

#include <vector>
#include <iostream>
#include <map>

using namespace std;

class Solution {
public:
    int findLHS(vector<int>& nums) {
        map<int, int> counter;
        for (int n : nums) {
            if (counter.contains(n))
                counter[n] += 1;
            else counter[n] = 1;
        }

        int mx = 0;
        for (auto &[k, v] : counter) {
            if (counter.contains(k + 1))
                mx = max(mx, v + counter[k + 1]);
        }
        return mx;
    }
};

int main() {

    Solution s;
    vector<int> nums;

    nums = vector<int>{ 1,3,2,2,5,2,3,7 };
    cout << "5 ? " << s.findLHS(nums) << endl;

    nums = vector<int>{ 1,2,3,4 };
    cout << "2 ? " << s.findLHS(nums) << endl;

    nums = vector<int>{ 1,1,1,1 };
    cout << "0 ? " << s.findLHS(nums) << endl;

    return 0;
}