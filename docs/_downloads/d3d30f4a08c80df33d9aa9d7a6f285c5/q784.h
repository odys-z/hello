#ifndef Q784_H
#define Q784_H

#include <vector>
#include <string>

using namespace std;

/** 70.57%
 * @brief The Solution class
 */
class Solution {
public:
    vector<string> letterCasePermutation(string S) {
        vector<string> res;
        int l = S.length();

        if (l == 0) {
            res.push_back("");
            return res;
        }

        vector<string> tracks = letterCasePermutation(S.substr(0, l-1));
        char last = S.at(l - 1);
        bool isdigit = '0' <= last && last <= '9';
        for (string trk : tracks) {
            if (isdigit)
                res.push_back(trk + last);
            else {
                res.push_back(trk + (char)toupper(last));
                res.push_back(trk + (char)tolower(last));
            }
        }
        return res;
    }
};

#endif // Q784_H
