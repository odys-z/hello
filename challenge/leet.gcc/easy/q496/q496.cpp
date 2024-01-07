/**
 * 496. Next Greater Element I
 * https://leetcode.com/problems/next-greater-element-i/description/ 
 *
 */

#include <vector>
#include <map>
#include <iostream>
#include <utility>
#include <numeric>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        map<int, int> map1;
        for (int n : nums1)
            map1[n] = -1;

        vector<int> stack{ INT_MAX };

        for (int i = nums2.size() - 1; i >= 0; i--) {
            int n = nums2[i];
            if (n < stack.back()) {
				if (map1.contains(n))
					map1[n] = stack.back() == INT_MAX ? -1 : stack.back();
                stack.push_back(n);
            }
            else {
                while (n > stack.back()) stack.pop_back();
				if (map1.contains(n))
					map1[n] = stack.back() == INT_MAX ? -1 : stack.back();
                stack.push_back(n);
            }
        }

        vector<int> res;
        for (int n : nums1)
            res.push_back(map1[n]);
        return res;
    }
};

string reduce(vector<int> v) {
    return reduce(next(v.begin()), v.end(), string("[") + to_string(v[0]), [](string a, int b) { return move(a) + "," + to_string(b); }) + string("]");
}

int main() {
    Solution s;
    vector<int> nums1, nums2;

    nums1 = vector<int>{ 4,1,2 };
    nums2 = vector<int>{ 1,3,4,2 };
    // cout << "[-1,3,-1]? " << reduce(s.nextGreaterElement(nums1, nums2)) << endl;

    nums1 = vector<int>{ 1,3,4,7,2,5,9 };
    nums2 = vector<int>{ 1,3,4,2,9,7,5 };
    cout << "[3,4,9,-1,9,-1,-1]?" << endl << reduce(s.nextGreaterElement(nums1, nums2)) << endl;
}