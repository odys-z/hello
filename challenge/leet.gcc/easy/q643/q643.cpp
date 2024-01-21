/**
 * 643. Maximum Average Subarray I
 * https://leetcode.com/problems/maximum-average-subarray-i/
 */
#include <vector>
#include <cassert>
#include <numeric>

using namespace std;

class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double avg = double(accumulate(nums.begin(), nums.begin() + k, 0)) / k;
        double mx = avg;
        
        for (int i = k; i < nums.size(); i++) {
            avg += double(nums[i] - nums[i - k]) / k;
            if (mx < avg)
                mx = avg;
        }
        return mx;
    }
};

int main() {
    Solution s;
    vector<int> n;
    int k;

    n = vector<int>{ -1 }, k = 1;
    assert(-1 == s.findMaxAverage(n, k));

    n = vector<int>{ 1,12,-5,-6,50,3 }, k = 4;
    assert(12.75 == s.findMaxAverage(n, k));

    return 0;
}