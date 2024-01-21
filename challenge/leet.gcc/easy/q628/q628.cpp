/**
 * 628. Maximum Product of Three Numbers
 * https ://leetcode.com/problems/maximum-product-of-three-numbers
 */

#include <vector>
#include <iostream>
#include <cassert>

using namespace std;

class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        int a = -1001, b = -1001, c = -1001, y = 1001, z = 1001;

        for (int n : nums) {
            if (n < y)
                if (n < z) y = z, z = n;
                else y = n;
            if (n > c)
                if (n > b)
                    if (n > a) c = b, b = a, a = n;
                    else c = b, b = n;
                else c = n;
        }

        return max(a * b * c, a * y * z);
    }
};

int main() {
    Solution s;
    vector<int> nums;

    nums = vector<int>{ 1, 2, 3 };
    assert(6 == s.maximumProduct(nums));

    nums = vector<int>{ 0, 0, 0 };
    assert(0 == s.maximumProduct(nums));

    cout << "OK!" << endl;
}
