/**
 * https://leetcode.com/problems/binary-search/
 * 704. Binary Search
 */

#include <vector>
#include <iostream>
#include <cassert>

using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int a = 0, b = nums.size() / 2, c = nums.size();
        while (b != a && b != c) {
            if (target == nums[b])
                return b;
            else if (target < nums[b])
                c = b, b = (a + c) / 2;
            else 
                a = b, b = (a + c) / 2;
        }
        return nums[b] == target ? b : -1;
    }
};

int main() {
    Solution s;
    vector<int> nums;

    nums = vector<int>{ -1,0,3,5,9,12 };
    assert(4 == s.search(nums, 9));
    assert(-1 == s.search(nums, 2));
    assert(-1 == s.search(nums, -2));
    assert(5 == s.search(nums, 12));
    assert(-1 == s.search(nums, 22));

    nums = vector<int>{ 1 };
    assert(0  == s.search(nums, 1));
    assert(-1 == s.search(nums, 2));
    assert(-1 == s.search(nums, 0));

    nums = vector<int>{ 1, 100 };
    assert(-1  == s.search(nums, 3));
    assert(1  == s.search(nums, 100));
    assert(0  == s.search(nums, 1));
    assert(-1  == s.search(nums, 0));

    cout << "ok!" << endl;
}
