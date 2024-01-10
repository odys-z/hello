/**
 * 350. Intersection of Two Arrays II
 * https://leetcode.com/problems/intersection-of-two-arrays-ii/
 */
#include <vector>
#include <iostream>
#include <algorithm>
#include <numeric>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());

        vector<int> res;
        for (auto i = nums1.begin(), j = nums2.begin(); i != nums1.end() and j != nums2.end(); ) {
            if (*i < *j) i++;
            else if (*i > *j) j++;
            else {
                res.push_back(*i);
                i++, j++;
            }
        }
        return res;
    }
};

class Solution2 {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());

        vector<int> res;
        int i = 0, s1 = nums1.size(), j = 0, s2 = nums2.size();
        while (i < s1 and j < s2) {
            if (nums1[i] < nums2[j]) i++;
            else if (nums1[i] > nums2[j]) j++;
            else {
                res.push_back(nums1[i]);
                i++, j++;
            }
        }
        return res;
    }
};


string reduce(vector<int> v) {
    return string("[") + (v.size() > 0 ? reduce(next(v.begin()), v.end(), to_string(v[0]),
        [](string a, int b) {return move(a) + ", " + to_string(b); }) : "") + string("]");
}

int main() {
    Solution2 s;
    vector<int> n1;
    vector<int> n2;

    n1 = vector<int>{ 1,2,2,1 };
    n2 = vector<int>{ 1,2 };
    cout << "[1, 2] ?" << endl
        << reduce(s.intersect(n1, n2)) << endl;

    n1 = vector<int>{ 1,2 };
    n2 = vector<int>{ 1,2,2,1 };
    cout << "[1, 2] ?" << endl
        << reduce(s.intersect(n1, n2)) << endl;

}