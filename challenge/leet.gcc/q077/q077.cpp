#include <vector>
#include <iostream>
#include <numeric>
#include <string>

using namespace std;

/**
* 77. Combinations
* https://leetcode.com/problems/combinations/ 
*/

class Solution {
    vector<vector<int>> res;

public:
    void combine(int n, int k, int start, vector<int> &buf) {
        if (start == n || k == 0) {
            if (k == 0)
                res.push_back(buf);
            return;
        }

        vector<int> buff{ buf };
        for (int s = start; s < n; s++) {
			buff.push_back(s+1);  // v[s] = s+1
			combine(n, k-1, s+1, buff);
			buff.pop_back();
        }
    }

    vector<vector<int>> combine(int n, int k) {
        vector<int> buf{};
        combine(n, k, 0, buf);
        return res;
    }
};

class Solution2 {
    vector<vector<int>> res;

public:
    void combine(int n, int k, int start, vector<int> &buf, int depth) {
		if (k == 0) {
			res.push_back(buf);
            return;
        }
        if (start == n) {
            return;
        }

        for (int s = start; s < n; s++) {
            buf[depth] = s + 1;
			combine(n, k-1, s+1, buf, depth+1);
        }
    }

    vector<vector<int>> combine(int n, int k) {
        vector<int> buf(k);
        combine(n, k, 0, buf, 0);
        return res;
    }
};


int main() {
    auto delimeter = [](std::string a, int b) {
		return move(a) + ", " + to_string(b);
	};

    Solution2 s;
    for (vector<int> v : s.combine(4, 2)) {
        cout << endl << "[";
        cout << std::accumulate(next(v.begin()), v.end(), to_string(v[0]), delimeter);
        cout << "]";
    }

    return 0;
}
