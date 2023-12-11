/**
 * 2305. Fair Distribution of Cookies
 * https://leetcode.com/problems/fair-distribution-of-cookies/description/
 */

#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

class Solution {
    int ans;
    int avg;

public:
    int distribute(vector<int> &cookies, int k, vector<int> &buf, int start) {
        if (start >= cookies.size())
            return *max_element(buf.begin(), buf.end());

        for (int c = 0; c < buf.size(); c++) {
            buf[c] += cookies[start];
            ans = min(ans, distribute(cookies, k, buf, start+1));
            if (ans == avg)
                throw ans;
            buf[c] -= cookies[start];
            if (buf[c] == 0) break;
        }
        return ans;
    }

    int distributeCookies(vector<int> &cookies, int k) {
        vector<int> buf(k);
        avg = reduce(cookies.begin(), cookies.end());
        avg /= k;
        ans = INT_MAX;
        try {
            return distribute(cookies, k, buf, 0);
        }
        catch (int ans) {
            return ans;
        }
    }
};

int main() {

    Solution s;
    vector<int> cookies{ 8,15,10,20,8 };
    cout << "31? " << s.distributeCookies(cookies, 2) << endl;
    cookies = vector<int>{ 6,1,3,2,2,4,1,2 };
    cout << "7? " << s.distributeCookies(cookies, 3) << endl;
    return 0;
}

