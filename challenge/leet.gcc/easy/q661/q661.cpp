/**
 * 661. Image Smoother
 * https://leetcode.com/problems/image-smoother/description/ 
 */

#include <vector>
#include <iostream>
#include <numeric>
#include <string>

using namespace std;

class Solution {
public:
    void reducerow(vector<int>& v, vector<int>& buf) {
        if (v.size() > 1) {
            buf[0] = v[0] + v[1];

            for (int i = 1; i < v.size() - 1; i++)
                buf[i] = v[i - 1] + v[i] + v[i + 1];

            buf[v.size() - 1] = v[v.size() - 2] + v[v.size() - 1];
        }
        else buf[0] = v[0];
    }

    vector<vector<int>> imageSmoother(vector<vector<int>>& img) {
        int m = img.size(), n = img[0].size();
        vector<vector<int>> buf;

        for (int r = 0; r < m; r++) {
            vector<int> brow(n);
            reducerow(img[r], brow);
            buf.push_back(brow);
        }

        int d0 = max(m, n) == 1 ? 1 : min(m, n) == 1 ? 2 : 4;
        int dx = min(m, n) == 1 ? 3 : 6;
        int di = 9;

        for (int c = 0; c < n; c++) {
            // collectcol(c, buf);
            img[0][c] = (m > 1 ? buf[0][c] + buf[1][c] : buf[0][c]) / (c == 0 or c == n-1 ? d0 : dx);

            for (int r = 1; r < m - 1; r++) {
                img[r][c] = (buf[r - 1][c] + buf[r][c] + buf[r + 1][c]) / (c == 0 or c == n-1 ? dx : di);
            }
            if (m > 1)
                img[m - 1][c] = (buf[m - 2][c] + buf[m - 1][c]) / (c == 0 or c == n-1 ? d0 : dx);
        }

        return img;
    }
};

string reduce(vector<int> v) {
    return reduce(next(v.begin()), v.end(), string("[") + to_string(v[0]),
        [](string a, int b) { return move(a) + "," + to_string(b); }) + string("]");
}

string reduce(vector<vector<int>> v) {
    return reduce(next(v.begin()), v.end(), string("[") + reduce(v[0]),
        [](string a, vector<int> b) { return move(a) + "," + reduce(b); }) + string("]");
}

int main() {
    Solution s;
    vector<vector<int>> v;

    v = vector<vector<int>>{ vector<int>{ 1,2 }, vector<int>{2,3}, vector<int>{4,5} };
    cout << "[[2,2],[2,2],[3,3]] ?" << endl << reduce(s.imageSmoother(v)) << endl;
}
