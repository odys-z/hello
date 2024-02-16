/**
 * 697. Degree of an Array
 * https://leetcode.com/problems/degree-of-an-array
 */

#include <vector>
#include <cassert>
#include <map>
#include <iostream>

using namespace std;

struct Info
{
    int inf[3]; // index, frequence, length
};

class Solution {
public:
    int findShortestSubArray(vector<int>& nums) {
        map<int, Info> indx;
        int mn = nums.size(), fq = 0;

        for (int ix = 0; ix < nums.size(); ix++) {
            int n = nums[ix];
            if (indx.find(n) == indx.end()) {
                Info inf = { ix, 1, 1 };
                indx.emplace(pair<int, Info>(n, inf));

                if (fq < 1) {
                    mn = 1;
                    fq = 1;
                }
            }
            else {
                int dist = ix - indx[n].inf[0] + 1;
                indx[n].inf[2] = dist;

                indx[n].inf[1]++;
                int freq = indx[n].inf[1];

                if (fq < freq) {
                    mn = dist; // min(dist, mn);
                    fq = freq;
                }
                else if (fq == freq)
                    mn = min(dist, mn);
            }
        }
        return mn;
    }
};

int main() {
    Solution s;
    vector<int> nums;

    nums = vector<int>{ 2,1 };
    assert(1 == s.findShortestSubArray(nums));

    nums = vector<int>{ 1,2,2,3,1 };
    assert(2 == s.findShortestSubArray(nums));

    nums = vector<int>{ 1,2,2,3,2,7 };
    assert(4 == s.findShortestSubArray(nums));

    cout << "OK!" << endl;
    return 0;
}