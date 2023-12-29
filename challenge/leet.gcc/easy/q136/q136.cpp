/**
* Q136
* https://leetcode.com/problems/single-number/
*/
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int x = 0;
        for (int n : nums)
            x ^= n;
        return x;
    }
};

int main() {
    Solution s;
    vector<int> v{ 2, 2, 1 };
    cout << s.singleNumber(v) << endl;

    v = vector<int>{ 1 };
    cout << s.singleNumber(v) << endl;
}