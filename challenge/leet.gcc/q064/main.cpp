#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int y1 = grid.size();
        for (int y = grid.size() - 1; 0 <= y; y--)
        {
            int x1 = grid[y].size();
            for (int x = grid[y].size() - 1; 0 <= x; x--)
            {
                if (x == x1 - 1 && y == y1 - 1)
                    continue;
                int goRight =  x < x1 - 1 ? grid[y][x+1] : 1000;
                int downway =  y < y1 - 1 ? grid[y+1][x] : 1001;
                grid[y][x] += min(goRight, downway);
            }
        }
        return grid[0][0];
    }
};

int main()
{
    Solution s;
    vector<vector<int>> g = {{1, 3, 1}, {1, 5, 1}, {4, 2, 1}};
    cout << s.minPathSum(g) << endl;

    vector<vector<int>> k = {{1, 2, 3}, {4, 5, 6}};
    cout << s.minPathSum(k) << endl;

    vector<vector<int>> t = {{1, 2, 3}, {4, 5, 6}, {4, 0, 1}};
    cout << s.minPathSum(t) << endl;
    return 0;
}
