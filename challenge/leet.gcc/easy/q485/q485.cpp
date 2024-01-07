/**
 * 485. Max Consecutive Ones
 * https://leetcode.com/problems/max-consecutive-ones/description/
 */

#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int count = 0, xc = 0;
        for (int n : nums) {
            if (n > 0) {
                count++;
                xc = xc > count ? xc : count;
            }
            else count = 0;
        }
        return xc;
    }
};

int main() {
    Solution s;
    vector<int> v;
    v = vector<int>{ 1,1,0,1,1,1 };
    cout << "3 ? " << s.findMaxConsecutiveOnes(v) << endl;

    v = vector<int>{ 1,0,1,1,0,1 };
    cout << "2 ? " << s.findMaxConsecutiveOnes(v) << endl;
    return 0;
}