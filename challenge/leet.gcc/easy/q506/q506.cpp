/**
 * 506. Relative Ranks
 * https://leetcode.com/problems/relative-ranks/description/ 
 */

#include <vector>
#include <string>
#include <iostream>
#include <numeric>
#include <algorithm>

using namespace std;

class Solution {
public:
    string tostr(int i) {
        if (i == 0)
            return string("Gold Medal");
        else if (i == 1)
            return string("Silver Medal");
        else if (i == 2)
            return string("Bronze Medal");
        else
            return to_string(i+1);
    }

    vector<string> findRelativeRanks(vector<int>& score) {
        vector<pair<int, int>> h;
        for (int s = 0; s < score.size(); s++) {
            h.push_back(pair<int, int>{score[s], s});
            push_heap(h.begin(), h.end(), [](pair<int, int>& a, pair<int, int> &b){
                return a.first < b.first;
            });
        }

        vector<string> res(score.size());
        int i = 0;
        while (h.size() > 0) {
            res[h.front().second] = tostr(i);
            i++;
            pop_heap(h.begin(), h.end());
            h.pop_back();
        }
        return res;
    }
};

string reduce(vector<string> v) {
    return v.size() > 0 ? reduce(
        next(v.begin()), v.end(), string("[") + v[0], [](string a, string b) { return move(a) + ", " + b; })
        + string("]")
        : "[]";
}

int main() {
    Solution s;
    vector<int> scores;

    scores = vector<int>{ 5,4,3,2,1 };
    cout << "[Gold Medal, Silver Medal, Bronze Medal, 4, 5] ?" << endl
        << reduce(s.findRelativeRanks(scores)) << endl;

    scores = vector<int>{ 10,3,8,9,4 };
    cout << "[Gold Medal, 5, Bronze Medal, Silver Medal, 4] ?" << endl
        << reduce(s.findRelativeRanks(scores)) << endl;

    return 0;
}