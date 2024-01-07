/**
 * 448. Find All Numbers Disappeared in an Array
 * https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
 */
#include <vector>
#include <set>
#include <iostream>
#include <string>
#include <numeric>

using namespace std;

class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        set<int>s;
        vector<int>res;
        for (int i = 0; i < nums.size(); i++) 
            s.insert(nums[i]);

        for (int i = 1; i <= nums.size(); i++)
            if (!s.contains(i))
                res.push_back(i);

        return res;
    }
};

class Solution2 {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        nums.insert(nums.begin(), 0);

        int k = 1, n = nums.size();
        while (k < n) {
            int vk = nums[k];
            if (vk == k)
                nums[vk] = 0;
            else 
                while (vk != 0) {
                    int vx = nums[vk];
                    nums[vk] = 0;
                    vk = vx;
                }
            k++;
        }

        vector<int> res;
        for (int i = 1; i < n; i++) {
            if (nums[i] != 0)
                res.push_back(i);
        }
        return res;
    }
};

class Solution3 {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        nums.insert(nums.begin(), 0);

        int n = nums.size();
        for (int k = 1; k < n; k++) {
            int vk = nums[k];
            int vx = vk > 0 ? vk : -vk;
            if (nums[vx] > 0)
                nums[vx] = -nums[vx];
        }

        vector<int> res;
        for (int i = 1; i < n; i++) {
            if (nums[i] > 0)
                res.push_back(i);
        }
        return res;
    }
};


int main() {
    Solution3 s;
    vector<int> v;
    v = vector<int>{1,1};
    v = s.findDisappearedNumbers(v);
    cout << "[2] ? " << (v.size() > 0 ? reduce(next(v.begin()), v.end(), string("[") + to_string(v[0]), [](string a, int b) {return move(a) + ", " + to_string(b); }) + string("]") : string("[]")) << endl;

    v = vector<int>{ 4,3,2,4,8,2,3,1 };
    v = s.findDisappearedNumbers(v);
    cout << "[5, 6, 7] ? " << (v.size() > 0 ? reduce(next(v.begin()), v.end(), string("[") + to_string(v[0]), [](string a, int b) {return move(a) + ", " + to_string(b); }) + string("]") : string("[]")) << endl;

    v = vector<int>{ 4,3,2,7,8,2,3,1 };
    v = s.findDisappearedNumbers(v);
    cout << "[5, 6] ? " << (v.size() > 0 ? reduce(next(v.begin()), v.end(), string("[") + to_string(v[0]), [](string a, int b) {return move(a) + ", " + to_string(b); }) + string("]") : string("[]")) << endl;

    return 0;
}