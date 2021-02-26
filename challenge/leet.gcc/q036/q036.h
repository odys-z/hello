#ifndef Q036_H
#define Q036_H

#include <vector>
#include <iterator>
#include <set>

using namespace std;

/** 74.66%
 * @brief The Solution class
 */
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        set<char> krow[9], kcol[9], k3x3[9];

        for (unsigned rx = 0; rx < board.size(); rx++) {
            vector<char> r = board[rx];
            for (unsigned cx = 0; cx < r.size(); cx++) {
                char c = r[cx];
                if (c == '.' or c == ' ') continue;

                if (krow[rx].count(c) || kcol[cx].count(c))
                    return false;
                else {
                    int r33 = rx / 3, c33 = cx / 3;
                    set<char> *k33 = &(k3x3[r33 * 3 + c33]);
                    if (k33->count(c))
                        return false;
                    else {
                        krow[rx].insert(c);
                        kcol[cx].insert(c);
                        k33->insert(c);
                    }
                }
            }
        }
        return true;
    }
};

#endif // Q036_H
