#include <iostream>

#include <vector>
#include <cstdlib>

using namespace std;

class Solution {
public:
    long long maxPoints(vector<vector<int>>& points) {
        int max_y = 0;
        int y1 = points.size();
        for (int y = 1; y < y1; y++) {
            int x1 = points[y].size();
            max_y = 0;
            for (int x = 0; x < x1; x++)
            {
                points[y][x] = maxp(y, x, points);
                max_y = max(max_y, points[y][x]);
            }
        }
        return max_y;
    }

    long long maxp(long y, long x, vector<vector<int>> points) {
        int maxyx = 0;
        for (ulong c = 0; c < points[y].size(); c++)
        {
            maxyx = max(maxyx, points[y-1][c] - abs(x - c))
        }
    }
};

int main()
{
    Solution s;
    vector<vector<int>> points = { {1, 5}, {2,3}, {4,2} };
    cout << "11 : " << s.maxPoints(points) << endl;
    return 0;
}
