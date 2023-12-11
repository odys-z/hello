#include <iostream>
#include <vector>
#include <set>

using namespace std;

class Solution {
public:
    bool isparlindrome(string &s, set<string> &dp) {
        if (s.length() == 0)
            return false;
        else if (dp.count(s) || s.length() == 1)
            return true;

        if (s.length() > 1)
            for (int i = 0; i < s.length(); i++)
                if (s.at(i) != s.at(s.length() - 1 - i))
                return false;

        dp.insert(s);
        return true;
    }

    vector<vector<string>> partition(string s, set<string>& dp) {
        vector<vector<string>> res;
        for (int x = 1; x <= s.length(); x++) {
            string ls = s.substr(0, x);
            string rs = s.substr(x, s.length() - x);

            if (isparlindrome(ls, dp)) {
				if (isparlindrome(rs, dp))
					res.push_back(vector<string>{ls, rs});

				vector<vector<string>> rres = partition(rs, dp);
				for (vector<string>& rightpars : rres)
					rightpars.insert(rightpars.begin(), ls);

				res.insert(res.end(), rres.begin(), rres.end());

            }
        }
        return res;
    }

    vector<vector<string>> partition(string s) {
        vector<vector<string>> res;
        set<string> dp;
        res = partition(s, dp);
		if (isparlindrome(s, dp))
			res.push_back(vector<string>{s});
        return res;
    }
};

class Solution2 {

public:
    vector<vector<string>> res;

    bool isparlindrome(string &s, set<string> &dp) {
        if (dp.count(s) || s.length() == 1)
            return true;

        if (s.length() > 1)
            for (int i = 0; i < s.length(); i++)
                if (s.at(i) != s.at(s.length() - 1 - i))
                return false;

        dp.insert(s);
        return true;
    }

    void backtrack(int x, string s, vector<string> &buf, set<string> &dp) {
        if (x >= s.length()) {
            this->res.push_back(buf);
            return;
        }
        else
        for (int px = x+1; px <= s.length(); px++) {
            string p = s.substr(x, px - x);
            if (isparlindrome(p, dp)) {
                buf.push_back(p);
                backtrack(px, s, buf, dp);
                buf.pop_back();
            }
        }
    }

    vector<vector<string>> partition(string s) {
        vector<string> buf;
        set<string> dp;
        backtrack(0, s, buf, dp);
        return this->res;
    }
};

int main()
{
    Solution2 s;
    vector<string> qs{ "aab", "b", "aa", "aba", "abcaa", "abaaba"};
    for (string q : qs) {
		cout << endl << q << endl;
		for (vector<string> ps : s.partition(q)) {
			for (string p : ps)
				cout << p << ", ";
			cout << endl;
		}
        s.res.clear();
    }
    return 0;
}
