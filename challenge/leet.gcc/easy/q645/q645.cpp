
/**
 *
 */

#include <vector>
#include <iostream>
#include <bitset>
#include <cassert>
#include <algorithm>
#include <numeric>

using namespace std;

class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int duplicate = 0,
            sum = accumulate(nums.begin(), nums.end(), 0),
            n = nums.size();
        bitset<10001> bits;

        for (size_t i = 0; i < n; i++) {
            if (bits.test(nums[i])) {
                duplicate = nums[i];
                break;
            }
            bits.set(nums[i]);
        }

        // S + dup - mis = sum
        // where S = n(n+1) /2
        // mis = S - sum + dup
        int mis = n * (n + 1) / 2 - sum + duplicate;
        return vector<int>{duplicate, mis};
    }
};

int main() {

    Solution s;
    vector<int> nums;

    nums = vector<int>{ 2,2,1,4,3 };
    vector<int> res = s.findErrorNums(nums);
    assert(2 == res[0]);
    assert(5 == res[1]);

    nums = vector<int>{ 1, 2, 2, 4 };
    res = s.findErrorNums(nums);
    assert(2 == res[0]);
    assert(3 == res[1]);

    nums = vector<int>{ 3,2,3,4,6,5 };
    res = s.findErrorNums(nums);
    assert(3 == res[0]);
    assert(1 == res[1]);

    cout << "OK!" << endl;
    return 0;
}