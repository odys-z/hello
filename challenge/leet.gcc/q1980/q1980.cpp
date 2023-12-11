/**
* 1980. Find Unique Binary String
* https://leetcode.com/problems/find-unique-binary-string/description/
n == nums.length
1 <= n <= 16
nums[i].length == n
nums[i] is either '0' or '1'.
All the strings of nums are unique.
*/

#include <string>
#include <vector>
#include <set>
#include <iostream>
#include <numeric>
#include <format>

using namespace std;

class Solution {
public:
    template<typename... Args>
    inline string formt(const std::format_string<Args...> fmt, Args&&... args)
    {
        return vformat(fmt.get(), std::make_format_args(args...));
    }

    string findDifferentBinaryString(vector<string>& nums) {
        set<int> hash;
        for (string n : nums)
            hash.insert(stoi(n));
        for (int i = 0; i < 1 << nums.size(); i++)
            if (hash.find(i) == hash.end()) {
                string s;
                /*
                snprintf(&f[0], 5, "%%0%dd", (int)nums.size());
                char* ccx = new char[f.length() + 1];
                // Copy contents
                std::copy(f.begin(), f.end(), ccx);

                snprintf(&s[0], nums.size() + 2, ccx, i);
                */

                // string f = format(":0{}", nums.size());
                string f = ":02";
                cout << f << endl;
                s = this->formt("{:2d}", i);
                return s;
            }
        return "NAN";
    }
};

class Cantor {
public:

    /**
     * Cantor diagnal argument: https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument 
     */
    string findDifferentBinaryString(vector<string>& nums) {
        string res;

        for (int i = 0; i < nums.size(); i++) {
            res += to_string('1' - nums[i][i]);
        }
        return res;
    }
};

int main() {

	Cantor s;

	vector<string> v{ "00", "10" };

    cout << endl;
    string x = s.findDifferentBinaryString(v);
    cout << x << endl;

	return 0;
}
