/**
 * 500. Keyboard Row
 * https://leetcode.com/problems/keyboard-row/description/
 *
 */
#include <vector>
#include <map>
#include <iostream>
#include <numeric>

using namespace std;

class Solution {
public:
    vector<string> findWords(vector<string>& words) {
        map<char, int> dic{
            {'q',0}, {'w',0}, {'e',0}, {'r',0}, {'t',0}, {'y',0}, {'u',0}, {'i',0}, {'o',0}, {'p',0},
            {'Q',0}, {'W',0}, {'E',0}, {'R',0}, {'T',0}, {'Y',0}, {'U',0}, {'I',0}, {'O',0}, {'P',0},
            {'a',1}, {'s',1}, {'d',1}, {'f',1}, {'g',1}, {'h',1}, {'j',1}, {'k',1}, {'l',1},
            {'A',1}, {'S',1}, {'D',1}, {'F',1}, {'G',1}, {'H',1}, {'J',1}, {'K',1}, {'L',1},
            {'z',2}, {'x',2}, {'c',2}, {'v',2}, {'b',2}, {'n',2}, {'m',2},
            {'Z',2}, {'X',2}, {'C',2}, {'V',2}, {'B',2}, {'N',2}, {'M',2} };

        vector<string> res;
        for (string w : words) {
            int row = -1;
            for (char c : w)
                if (row == -1) row = dic[c];
                else if (row != dic[c]) {
                    row = -1;
                    break;
                }
            if (row >= 0)
                res.push_back(w);
        }
        return res;
    }
};

string reduce(vector<string>& s) {
    return reduce(next(s.begin()), s.end(), s[0],
        [](string a, string b) {return move(a) + ", " + b; });
}

int main() {
    Solution s;
    vector<string> words;

    words = vector<string>{ "Q","qp","qa","sx","CV","XCVBNM","XCVBNMo" };
    cout << "Q, qp, CV, XCVBNM?" << endl << reduce(s.findWords(words)) << endl;
}
