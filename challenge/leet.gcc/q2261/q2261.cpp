/**
 * 2261. K Divisible Elements Subarrays
 * https://leetcode.com/problems/k-divisible-elements-subarrays/description/
 */

#include <vector>
#include <set>
#include <unordered_set>
#include <string>
#include <iostream>
#include <numeric>

using namespace std;

class Solution {
    set<vector<int>> found;
public:
    vector<vector<int>> res;
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

    void countArrs(vector<int>& nums, vector<int>& countp, int start, int k) {
        if (start >= (int)nums.size())
            return;

        int k0 = 0;
        for (int s = start; s < nums.size(); s++) {
			for (int e = s; e < nums.size(); e++) {
				if (countp[e] - k0 > k)
					break;
				auto i = nums.begin();
				this->found.insert(vector<int>{i + s, i + e + 1});
			}
            k0 = countp[s];
        }
    }

    int countDistinct(vector<int>& nums, int k, int p) {
        vector<int> countp(nums);
       
        int k0 = 0;
        for (int i = 0; i < countp.size(); i++) {
            // countp[i] = countp[i] % p == 0 ? 1 : 0;
            countp[i] = countp[i] % p == 0 ? ++k0 : k0;
        }

        this->found = set<vector<int>>();
        vector<int> buf;
        countArrs(nums, countp, 0, k);
        return this->found.size();
    }
};

/**
* 
* https://leetcode.com/problems/k-divisible-elements-subarrays/discuss/1996294/O(n-2)%3A-Rabin-Karp-vs.-Trie
*/
class Solution2 {
public:
    const int P = 201;
    bool done = false;
    vector<size_t> powers;
    int countDistinct(vector<int>& nums, int k, int p) {
        if (!done) {
            done = 1;
            powers.assign(P, 1);

            for (int i = 1; i < P; ++i)
                powers[i] = powers[i - 1] * P;
        }

        int n = size(nums), ans = 0;
        unordered_set<size_t> set;
        vector<int> prefixDivisible(n + 1, 0);

        for (int i = 1; i <= n; ++i) {
            prefixDivisible[i] = prefixDivisible[i - 1] + (nums[i - 1] % p == 0);
        }

        for (int i = 0; i < n; ++i) {
            size_t hash = 0;
            for (int j = i; j < n; ++j) {
                hash += nums[j] * powers[j - i];
                if (prefixDivisible[j + 1] - prefixDivisible[i] > k) break;
                ans += set.insert(hash).second;
            }
        }
        return ans;
    }
};

class Solution3 {
public:
    int countDistinct(vector<int>& nums, int k, int p) {
        int n = size(nums), ans = 0;
        unordered_set<string> set;
        vector<int> countp(n + 1, 0);

        int k0 = 0;
        for (int i = 0; i < n; i++) {
            countp[i] = nums[i] % p == 0 ? ++k0 : k0;
        }

        char hash[201] = { 0 };
        k0 = 0;
        for (int i = 0; i < n; i++) {
            memset(hash, 0, 201);
            for (int j = i; j < n; ++j) {
                hash[j-i] = nums[j];
                if (countp[j] - k0 > k) break;
                ans += set.insert(hash).second;
            }
            k0 = countp[i];
        }
        return ans;
    }
};
int main() {
    auto join = [](string a, int b) {
        return move(a) + ", " + to_string(b);
        };

    Solution3 s;
    vector<int>v;
    v = vector<int> {3, 3, 4 };
    cout << "3? " << s.countDistinct(v, 1, 3) << endl;

    v = vector<int> {2, 3, 3, 4, 4, 5, 6, 7 };
    cout << "20? " << s.countDistinct(v, 1, 3) << endl;

    v = vector<int> { 2, 3, 3, 2, 2 };
    cout << "11? " << s.countDistinct(v, 2, 2) << endl;

    v = vector<int> { 1, 2, 3, 4 };
    cout << "10? " << s.countDistinct(v, 4, 1) << endl;
}