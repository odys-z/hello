/**
 * 1415. The k-th Lexicographical String of All Happy Strings of Length n
 * 
 * https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/
 */

#include <string>
#include <iostream>
#include <vector>

using namespace std;

/**
 * 100%
 */
class Solution {
    int kth;
    int found;
    vector<char> res;

public:
    void getHappys(int n, int k, vector<char> &buf, int currChar, int depth) {
        if (k == 0) {
            found++;
            res = buf;
            return;
        }
        if (currChar == n)
            return;
 
        for (int s = 0; s < 3; s++) { // 3: only 'a', 'b', 'c'
            if (depth == 0 || buf[depth - 1] != s) {
                buf[depth] = s;
				getHappys(n, k - 1, buf, s, depth + 1);
				if (found == kth) return;
            }
        }
    }

    string getHappyString(int n, int k) {
        this->kth = k;
        this->found = 0;
        vector<char> buf(n);
        getHappys(n, n, buf, 0, 0);

        string s;
        if (found == kth) {
            auto i = res.begin();
            while (res.size() > 0 && i != res.end()) {
                s.push_back(*i + 'a');
                i++;
            }
        }
        return s;
    }
};

int main() {

    Solution s;
    cout << "cab? " << s.getHappyString(3, 9) << endl;
    cout << "aba? " << s.getHappyString(3, 1) << endl;
    cout << "c? " << s.getHappyString(1, 3) << endl;
    cout << "_? " << s.getHappyString(1, 4) << endl;
    return 0;
}