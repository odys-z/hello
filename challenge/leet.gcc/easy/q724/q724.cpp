/***
 * https://leetcode.com/problems/find-pivot-index/
 * 724. Find Pivot Index
 */

#include <vector>
#include <iostream>
#include <cassert>

using namespace std;

class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return 0;

        vector<int> dp(n);
        dp[n - 1] = nums[n - 1];

        for (int j = n - 2; j >= 0; j--) {
            dp[j] = dp[j + 1] + nums[j];
        }
        
        if (dp[1] == 0) return 0;
        for (int i = 1; i < nums.size() - 1; i++) {
            if (nums[i - 1] == dp[i + 1])
                return i;
            nums[i] += nums[i - 1];
        }

        if (nums[n-2] == 0) return n-1;

        return -1;
    }
};

int main() {
    Solution s;
    vector<int> nums;

    nums = vector<int>{ 1 };
    assert(0 == s.pivotIndex(nums));

    nums = vector<int>{ 1,7,3,6,5,6 };
    assert(3 == s.pivotIndex(nums));

    nums = vector<int>{ 1,2,3 };
    assert(-1 == s.pivotIndex(nums));

    nums = vector<int>{ 2,1,-1 };
    assert(0 == s.pivotIndex(nums));

    cout << "OK" << endl;
}