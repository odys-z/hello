#include <iostream>
#include <vector>
#include <set>

#include <chrono>

using namespace std;
using namespace std::chrono;

/**
 * n=10, ms: 172
 * n=12, ms: 2897
 * n=14, ms: 40798
 * @brief The Solution class
 */
class Solution {
public:
    set<string> gen(int n) {
        set<string> pars;
        if (n == 1) {
            pars.insert("()");
            return pars;
        }
        else {
            set<string> v0 = gen(n - 1);
            set<string> pars;
            for (set<string>::iterator i = v0.begin(); i != v0.end(); i++)
                for (int j = 0; j < (*i).length() / 2 + 1; j++) {
                    string v = (*i);
                    pars.insert(v.insert(j, "()"));
                }
            return pars;
        }
    }

    vector<string> generateParenthesis(int n) {
        string p0 = "()";
        set<string> res = gen(n);
        return {res.begin(), res.end()};
    }
};

/**
 * n=10, ms: 495
 * n=12, ms: 8635
 * n=14, ms: 142734
 * @brief The Solution2 class
 */
class Solution2 {
public:
    set<vector<char>> gen(int n) {
        set<vector<char>> pars;
        if (n == 1) {
            pars.insert(vector{'(', ')'});
            return pars;
        }
        else {
            set<vector<char>> v0 = gen(n - 1);
            set<vector<char>> pars;
            for (set<vector<char>>::iterator i = v0.begin(); i != v0.end(); i++)
                for (int j = 0; j < (*i).size() / 2 + 1; j++) {
                    vector<char> v { (*i) };
                    v.insert(v.begin() + j, ')');
                    v.insert(v.begin() + j, '(');
                    pars.insert(v);
                }
            return pars;
        }
    }

    vector<string> generateParenthesis(int n) {
        vector<string> p0 {};
        set<vector<char>> res = gen(n);
        for (set<vector<char>>::iterator ri = res.begin(); ri != res.end(); ri++) {
            string s {ri->begin(), ri->end()};
            p0.push_back(s);
        }
        return p0;
    }
};

/**
 * n=10, ms: 91
 * n=12, ms: 1281
 * n=14, ms: 13634
 *
 * 100%
 * @brief The Solution3 class
 */
class Solution3 {
public:
    void gen(int n, int l, int r, string buf, vector<string> &res) {
        if (l + r == n*2) {
            res.push_back(buf);
            return;
        }

        if (l < n)
            gen(n, l+1, r, buf+"(", res);
        if (r < l)
            gen(n, l, r+1, buf+")", res);
        return;
    }

    vector<string> generateParenthesis(int n) {
        vector<string> res;
        gen(n, 0, 0, "", res);
        return res;
    }
};

int main()
{
    Solution3 s;
    cout << endl << 1 << endl;
    for (string p : s.generateParenthesis(1))
        cout << p << endl;

    cout << endl << 2 << endl;
    for (string p : s.generateParenthesis(2))
        cout << p << endl;

    cout << endl << 3 << endl;
    for (string p : s.generateParenthesis(3))
        cout << p << endl;

    milliseconds ms = duration_cast< milliseconds >(
        system_clock::now().time_since_epoch()
        );

    s.generateParenthesis(10);
    cout << "n=10, ms: " << (duration_cast< milliseconds >(
        system_clock::now().time_since_epoch()
                 ).count() - ms.count()) << endl;

    s.generateParenthesis(12);
    cout << "n=12, ms: " << (duration_cast< milliseconds >(
        system_clock::now().time_since_epoch()
                 ).count() - ms.count()) << endl;

    ms = duration_cast< milliseconds >(
        system_clock::now().time_since_epoch()
        );

    s.generateParenthesis(14);
    cout << "n=14, ms: " << (duration_cast< milliseconds >(
        system_clock::now().time_since_epoch()
                 ).count() - ms.count()) << endl;

    return 0;
}
