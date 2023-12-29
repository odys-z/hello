/**
 * 119. Pascal's Triangle II
 * https://leetcode.com/problems/pascals-triangle-ii/description/
 */

#include <vector>
#include <iostream>
#include <string>
#include <numeric>

using namespace std;

class Solution {
public:
    vector<int> getRow(int rx) {
        if (rx == 0) return vector<int> {1};
        else if (rx == 1) return vector<int> {1, 1};
        else if (rx == 2) return vector<int> {1, 2, 1};
        else {
            vector<int> r2{ 1, 2, 1 };
            for (int r = 3; r <= rx; r++) {
                vector<int> r3{ 1 };
                for (int c = 0; c < (r-1) / 2; c++) {
                    r3.push_back(r2[c] + r2[c+1]);
                }
				if (r % 2 == 0)
					r3.push_back(r2[r/2 - 1] + r2[r/2 - 1]);
                r2 = r3;
            }
            r2.insert(r2.end(), rx % 2 == 0 ? next(r2.rbegin()) : r2.rbegin(), r2.rend());
            return r2;
        }
    }
};

class Reference {
public:
    vector<int> getRow(int n) {
        vector<int> v;
        long long ans = 1;
        v.push_back(ans);
        for (int i = 0; i < n; i++) {
            ans = ans * (n - i);
            ans = ans / (i + 1);
            v.push_back(ans);
        }
        return v;
    }
};

string reduce(vector<int> q) {
    return reduce(next(q.begin()), q.end(), string("[" + to_string(q[0])), [](string a, int b) { return a + ", " + to_string(b); }) + string("]");
}

int main() {

    Reference r;
    vector<int> t = r.getRow(5);
    cout << "reference:" << endl << reduce(t) << endl;

    Solution s;

    vector<int> v;

    v = s.getRow(3);
    cout << "3 ? " << endl << reduce(v) << endl;

    v = s.getRow(4);
    cout << "4 ? " << endl << reduce(v) << endl;

    v = s.getRow(5);
    cout << "5 ? " << endl << reduce(v) << endl;

    v = s.getRow(6);
    cout << "6 ? " << endl << reduce(v) << endl;

    return 0;
}