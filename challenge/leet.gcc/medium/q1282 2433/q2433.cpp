/**
 * 2433. Find The Original Array of Prefix Xor
 * https://leetcode.com/problems/find-the-original-array-of-prefix-xor/ 
 */

#include <iostream>
#include "utils.h"

using namespace std;

class Solution {
public:
    vector<int> findArray(vector<int>& pref) {
        int prefix = pref[0];
        for (int i = 1; i < pref.size(); i++) {
            pref[i] ^= prefix;
            prefix ^= pref[i];
        }

        return pref;
    }
};

/*
int main() {
    Solution s;
    vector<int> nums1;

    nums1 = vector<int>{ 5,2,0,3,1 };
    cout << "[5,7,2,3,2]?" << endl << reducev(s.findArray(nums1)) << endl;

    cout << "OK" << endl;
    return 0;
}
*/
