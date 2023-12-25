/**
 * 2698. Find the Punishment Number of an Integer
 * https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/
 */

#include <vector>
#include <map>
#include <set>
#include <utility>
#include <string>
#include <iostream>
#include <numeric>

using namespace std;

/**
 * [1, 9, 10, 36, 45, 55, 82, 91, 99, 100, 235, 297, 369, 370, 379, 414,
 * 657, 675, 703, 756, 792, 909, 918, 945, 964, 990, 991, 999, 1000]
 */
class Solution {
    int sum;
    vector<pair<int, int>> pairs {
        {1, 1}, { 9, 82 }, { 10, 182 }, { 36, 1478 }, { 45, 3503 }, { 55, 6528 }, { 82, 13252 }, { 91, 21533 }, { 99, 31334 },
        { 100, 41334 }, { 235, 96559 }, { 297, 184768 }, { 369, 320929 }, { 370, 457829 }, { 379, 601470 }, { 414, 772866 },
        { 657, 1204515 }, { 675, 1660140 }, { 703, 2154349 }, { 756, 2725885 }, { 792, 3353149 }, { 909, 4179430 }, { 918, 5022154 },
        { 945, 5915179 }, { 964, 6844475 }, { 990, 7824575 }, { 991, 8806656 }, { 999, 9804657 }, { 1000, 10804657 }
    };

public:

    vector<int> convert(int sqr) {
		vector<int> digits;
		while (sqr > 0) {
			int d = sqr % 10;
			digits.insert(digits.begin(), d);
			sqr /= 10;
		}
        return digits;
    }

    void track(int i, int depth, int subsum, vector<int>& digits) {
        if (depth > digits.size()) {
            return;
        }

        if (depth == digits.size() && subsum == i) {
            this->sum += i * i;
            throw this->sum;
        }

        int sub = 0;
        for (int j = depth; j < digits.size(); j++) {
            sub = sub * 10 + digits[j];
            if (subsum + sub > i) return;
            track(i, j + 1, subsum + sub, digits);
        }
    }

    void dp(int n) {
        int acc = 0;
        pairs = vector<pair<int, int>>{ pair<int, int>{1, 1} };

        for (int i = 1; i <= n; i++) {
            this->sum = 0;
            vector<int> digits = convert(i * i);
            try {
                track(i, 0, 0, digits);
            }
            catch (int mx) {
                pairs.push_back(pair(i, acc += mx));
            }
        }
        cout << endl << "vector<pair<int, int>> pairs {" << endl
            << reduce(pairs.begin() + 2, pairs.end(), "{" + to_string(pairs[0].first) + ", " + to_string(pairs[1].second) + "}",
                [](string a, pair<int, int> b) { return move(a) + ",\n" + "{" + to_string(b.first) + ", " + to_string(b.second) + "}"; })
            << "};" << endl;
    }

    int punishmentNumber(int n) {
        // dp(1000);

        int l = 0, m = (pairs.size() - 1) / 2, r = pairs.size() - 1;

        while (l < r) {
            if (n < pairs[m].first)
                r = m - 1;
            else 
                l = m;
            m = (l + r + 1) / 2;
        }

        if (l >= r-1)
            return pairs[r].second;

        return pairs[pairs.size() - 1].second;
    };
};

class Solution2 {
public:
    // [6: {1: True, 29: True, 6: True}, ...]
    // vector<map<int, bool>> dp;

    int sum;

    vector<int> convert(int sqr) {
		vector<int> digits;
		while (sqr > 0) {
			int d = sqr % 10;
			digits.insert(digits.begin(), d);
			sqr /= 10;
		}
        return digits;
    }

    void track(int i, int depth, int subsum, vector<int>& digits) {
        if (depth > digits.size()) {
            return;
        }

        /*
        if (dp[depth].find(subsum) != dp[depth].end()) {
            // cout << i << " " << subsum << endl;
            return;
        }
        */

        if (depth == digits.size() && subsum == i) {
            this->sum += i * i;
            // dp[depth].insert({i, true});
            throw this->sum;
        }

        int sub = 0;
        for (int j = depth; j < digits.size(); j++) {
            sub = sub * 10 + digits[j];
            if (subsum + sub > i) return;
            track(i, j + 1, subsum + sub, digits);
        }
    }

    int punishmentNumber(int n) {
        this->sum = 0;
        // dp = vector<map<int, bool>>(n+1);
        for (int i = 1; i <= n; i++) {
            vector<int> digits = convert(i * i);
            try {
                track(i, 0, 0, digits);
            }
            catch (int mx) {}
        }
        return this->sum;
    }
};

int main() {

    Solution s;
    cout << endl;
    cout << "1478? " << s.punishmentNumber(37) << endl;
    cout << "182 ? " << s.punishmentNumber(10) << endl;
    cout << "6528? " << s.punishmentNumber(66) << endl;
}
