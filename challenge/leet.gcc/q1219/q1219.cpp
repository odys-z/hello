/*
* 1219. Path with Maximum Gold
* https://leetcode.com/problems/path-with-maximum-gold/description/
*/

#include <vector>
#include <iostream>
#include <numeric>

using namespace std;

class Solution {
public:
    int max = 0;

    void bfs(vector<vector<int>>& buf, int r, int c, int gold, int R, int C) {
        if (r < 0 || r >= R || c < 0 || c >= C || buf[r][c] <= 0) return;
        
        int g0 = buf[r][c];
        gold += buf[r][c];
        buf[r][c] = -1;
        if (gold > max) max = gold;

		bfs(buf, r + 1, c, gold, R, C);
		bfs(buf, r - 1, c, gold, R, C);
		bfs(buf, r, c - 1, gold, R, C);
		bfs(buf, r, c + 1, gold, R, C);
        buf[r][c] = g0;
    }

    int getMaximumGold(vector<vector<int>>& grid) {

        max = 0;
        for (int r = 0; r < grid.size(); r++)
        for (int c = 0; c < grid[0].size(); c++) {
            if (grid[r][c] > 0) {
                bfs(grid, r, c, 0, grid.size(), grid[0].size());
            }
        }
        return max;
    }
};

int main() {
    Solution s;
    vector<vector<int>> g;
    
    g = vector<vector<int>>{
        vector<int> {0,0,0,0,0,0,0,0,0},
        vector<int> {0,3,3,3,3,3,3,3,0},
        vector<int> {0,3,4,0,0,0,4,3,0},
        vector<int> {0,3,0,3,3,3,0,3,0},
        vector<int> {0,0,0,3,0,3,0,3,0},
        vector<int> {0,0,0,3,0,0,4,3,0},
        vector<int> {0,0,4,3,3,3,3,3,0},
        vector<int> {0,0,4,4,4,0,0,0,0}
    };
    cout << "72 + 19? " << s.getMaximumGold(g) << endl;

    g = vector<vector<int>> {
        vector<int>{1,0,7},
        vector<int>{2,0,6},
        vector<int>{3,4,5},
        vector<int>{0,3,0},
        vector<int>{9,0,20}
    };
    cout << "28? " << s.getMaximumGold(g) << endl;

    s.max = 0;
    g = vector<vector<int>> {
        vector<int>{0,6,0},
        vector<int>{5,8,7},
        vector<int>{0,9,0},
    };
    cout << "24? " << s.getMaximumGold(g) << endl;

}

