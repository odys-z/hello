/*
 * 268. Missing Number
 * https://leetcode.com/problems/missing-number/
 */

#include <vector>
#include <iostream>
#include <numeric>
#include <string>

using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int sz = nums.size();
        int p = 0, sk = 0, bk = sz;

        while (sk < sz) {
            if (nums[sk] != 0) {
                nums[p] = nums[sk];
                p++, sk++;
            }
            else {
                --bk, sk++;
            }
        }
        while (p < sz)
            nums[p++] = 0;
    }
};

int main() {

    Solution s;
    vector<int> nums{0,1,0,3,11};
    s.moveZeroes(nums);
    cout << reduce(next(nums.begin()), nums.end(), to_string(nums[0]), [](string a, int b) { return move(a) + ", " + to_string(b); }) << endl;
};
