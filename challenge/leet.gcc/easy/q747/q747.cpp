/**
 * 747. Largest Number At Least Twice of Others
 * https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/
 */

#include <vector>
#include <iostream>
#include <cassert>

using namespace std;

class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        int nxt = 0, mx = 0;

        for (int i = 1; i < nums.size(); i++) {
            int n = nums[i];
            if (n > nxt) {
                if (n > nums[mx])
                    nxt = nums[mx], mx = i;
                else
                    nxt = n;
            }
        }

        return nums[mx] >= 2 * nxt ? mx : -1;
    }
};

int main() {
    Solution s;
    vector<int> nums{ 3,6,1,0 };
    assert(1 == s.dominantIndex(nums));

    nums = vector<int>{ 2,1 };
    assert(0 == s.dominantIndex(nums));

    nums = vector<int>{ 1,2,3,4 };
    assert(-1 == s.dominantIndex(nums));

    cout << "ok" << endl;
    return 0;
}