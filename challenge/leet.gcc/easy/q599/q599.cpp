/**
 * 599. Minimum Index Sum of Two Lists
 * https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/
 */

#include <vector>
#include <map>
#include <string>
#include <iostream>
#include <numeric>

using namespace std;

class Solution {
public:
    vector<string> findRestaurant(vector<string>& list1, vector<string>& list2) {
        map<string, int> dp;

        for (int i = 0; i < list1.size(); i++) {
            dp[list1[i]] = i;
        }

        int mx = INT32_MAX;
        vector<string> ans;
        for (int i = 0; i < list2.size(); i++) {
            if (dp.count(list2[i])) {
                int ix = dp[list2[i]] + i;
				if (ix < mx) {
					mx = ix;
                    ans = vector<string>{};
					ans.push_back(list2[i]);
				}
				else if (ix == mx) {
					ans.push_back(list2[i]);
				}
            }
        }

        return ans;
    }
};

int main() {
    Solution s;
    vector<string> u, v, w;

    u = vector<string>{ "Shogun","Tapioca Express","Burger King","KFC" };
    v = vector<string>{ "Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun" };
    w = s.findRestaurant(u, v);
    cout << "[Shogun]?" << endl << "[" << reduce(next(w.begin()), w.end(), w[0], [](string a, string b) {return move(a) + ", " + b; }) << "]" << endl;

    u = vector<string>{ "Shogun","Tapioca Express","Burger King","KFC" };
    v = vector<string>{ "KFC","Shogun","Burger King" };
    w = s.findRestaurant(u, v);
    cout << "[Shogun]?" << endl << "[" << reduce(next(w.begin()), w.end(), w[0], [](string a, string b) {return move(a) + ", " + b; }) << "]" << endl;

    u = vector<string>{ "happy","sad","good" };
    v = vector<string>{ "sad","happy","good" };
    w = s.findRestaurant(u, v);
    cout << "[sad, happy]?" << endl << "[" << reduce(next(w.begin()), w.end(), w[0], [](string a, string b) {return move(a) + ", " + b; }) << "]" << endl;
}
