/**
 * 807. Max Increase to Keep City Skyline
 * https://leetcode.com/problems/max-increase-to-keep-city-skyline/description/
 */

#include <vector>
#include <iostream>
#include <numeric>
#include <cassert>

using namespace std;

class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        vector<int> col(n);
        vector<int> row(m);
        for (int rx = 0; rx < m; rx++) {
            vector<int> r = grid[rx];
            for (int cx = 0; cx < n; cx++) {
                row[rx] = max(r[cx], row[rx]);
                col[cx] = max(r[cx], col[cx]);
            }
        }

        int cost = 0;
        for (int rx = 0; rx < m; rx++) {
            vector<int> r = grid[rx];
            for (int cx = 0; cx < n; cx++) {
                cost += min(row[rx], col[cx]) - r[cx];
            }
        }
        return cost;
    }
};

/*
int main() {
    Solution s;
    vector<vector<int>> grid;

    grid = vector<vector<int>>{ {3,0,8,4},{2,4,5,7},{9,2,6,3},{0,3,1,0} };
    assert(35 == s.maxIncreaseKeepingSkyline(grid));

    grid = vector<vector<int>>{ {0,0,0,0},{0,0,0,0} };
    assert(0 == s.maxIncreaseKeepingSkyline(grid));

    cout << "ok" << endl;
    return 0;
}
*/
