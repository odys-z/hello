/**
 * 667. Beautiful Arrangement II
 * https://leetcode.com/problems/beautiful-arrangement-ii/description/
 */

#include <vector>
#include <iostream>
#include <string>
#include <numeric>

using namespace std;

class Solution {
    vector<int> res;
    void constrarr(int n0, int n1, int k) {
        if (k == 1) {
            while (n0 <= n1) {
				res.push_back(n0);
				n0++;
			}
			return;
        }

        if (k % 2 == 0) {
			res.push_back(n1);
            constrarr(n0, n1 - 1, k - 1);
        }
        else {
            res.push_back(n0);
            constrarr(n0 + 1, n1, k - 1);
        }
    }

public:
    vector<int> constructArray(int n, int k) {
        constrarr(1, n, k);
        return this->res;
    }
};

int main() {
    auto join = [](std::string a, int b) {
		return move(a) + ", " + to_string(b);
	};

    Solution s;
    cout << "[1, 3, 2] ? " << endl;
    vector<int> v = s.constructArray(3, 2);
    cout << accumulate(next(v.begin()), v.end(), to_string(v[0]), join);
}