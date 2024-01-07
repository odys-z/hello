/**
 * 414. Third Maximum Number
 * https://leetcode.com/problems/third-maximum-number/description/
 */

#include <vector>
#include <set>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int partition(vector<int>& nums, int l, int r) {
        int p = nums[r];

        int left = l;
        for (int i = left; i <= r; i++) {
            if (nums[i] > p) {
                if (left < i)
                    swap(nums[i], nums[left]);
                left++;
            }
        }
        swap(nums[left], nums[r]);
        return left;
    }

    int kthMax(vector<int>& nums, int k, int l, int r) {
        int p = partition(nums, l, r);
        if (k - 1 == p - l) return nums[p];
        else if (k - 1 < p - l)
            return kthMax(nums, k, l, p - 1);
        else
            return kthMax(nums, k - 1 - (p - l), p + 1, r);
    }

    int thirdMax(vector<int>& nums) {
        set<int> s(nums.begin(), nums.end());
        nums = vector<int>(s.begin(), s.end());
        if (nums.size() == 1)
            return nums[0];
        else if (nums.size() == 2)
            return nums[0] > nums[1] ? nums[0] : nums[1];
        else
            return kthMax(nums, 3, 0, nums.size() - 1);
    }
};

class Solution2 {
public:

    int thirdMax(vector<int>& nums) {
        make_heap(nums.begin(), nums.end());
        set<int> s;

        int p;
        while (s.size() < 3 && nums.size() > 0) {
            p = nums.front();
            pop_heap(nums.begin(), nums.end());
            nums.pop_back();
            s.insert(p);
        }

        if (s.size() == 3)
            return p;
        else if (s.size() == 2) {
            int a = *s.begin(), b = *next(s.begin());
            return a > b ? a : b;
        }
        else if(s.size() == 1) {
            return *s.begin();
        }
        else
            return 0;
    }
};

int main() {
    Solution2 s;
    vector<int>v;

    v = vector<int>{ 3,2,1 };
    cout << "1?" << s.thirdMax(v) << endl;

    v = vector<int>{ 1,2 };
    cout << "2?" << s.thirdMax(v) << endl;

    v = vector<int>{ 1,1,2 };
    cout << "2?" << s.thirdMax(v) << endl;

    v = vector<int>{ 2,2,3,1 };
    cout << "1?" << s.thirdMax(v) << endl;

    v = vector<int>{ 1,4,2,3 };
    cout << "2?" << s.thirdMax(v) << endl;

    v = vector<int>{ 0, 1, 5, 7, 2 };
    cout << "2?" << s.thirdMax(v) << endl;
}
