/**
 * 349. Intersection of Two Arrays
 * https://leetcode.com/problems/intersection-of-two-arrays/description/
 */

#include <vector>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <bitset>
#include <numeric>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        bitset<1001> bs;
        vector<int> res;
        for (int n : nums1) bs.set(n);
        for (int m : nums2) {
            if (bs[m] > 0)
                res.push_back(m);
            bs.set(m, false);
        }
        return res;
    }

    vector<int> intersection3(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        set<int> s1(nums1.begin(), nums1.end());
        set<int> s2(nums2.begin(), nums2.end());
        set<int> res;
        
        set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(), inserter(res,res.begin()));

        return vector<int>(res.begin(), res.end());
    }

    vector<int> intersection2(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        vector<int> res;
        
        auto i = nums1.begin(), j = nums2.begin(); 
        while (i != nums1.end() && j != nums2.end()) {
            if (*i < *j) i++;
            else if (*i > *j) j++;
            else {
                if (res.size() == 0 || res.back() < *j)
                    res.push_back(*j);
                i++, j++;
            }
        }

        return res;
    }

};

string reduce(vector<int> v) {
    return v.size() > 0 ? reduce(next(v.begin()), v.end(), string("[") + to_string(v[0]), [](string a, int b) {return move(a) + "," + to_string(b); }) + string("]")
        : string("[]");
}

int main() {
    Solution s;
    vector<int>a, b;
    a = vector<int>{ 1,2,2,1 };
    b = vector<int>{ 2,2 };
    cout << "[2]?" << endl << reduce(s.intersection(a, b)) << endl;
    cout << reduce(s.intersection2(a, b)) << endl;

    a = vector<int>{ 4,9,5 };
    b = vector<int>{ 9,4,9,8,4 };
    cout << "[4,9]?" << endl << reduce(s.intersection(a, b)) << endl;
    cout << reduce(s.intersection2(a, b)) << endl;
}