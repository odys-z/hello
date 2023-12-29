/**
 * 118. Pascal's Triangle
 * https://leetcode.com/problems/pascals-triangle/
 */

#include <vector>
#include <iostream>
#include <string>
#include <numeric>

using namespace std;

class Solution {
public:
    vector<vector<int>> getRow(int numRows) {
        vector<vector<int>> triangle{ vector<int>{1} };
        for (int r = 1; r < numRows; r++) {
            vector<int> row{ 1 };
            for (int c = 1; c < triangle[triangle.size() - 1].size(); c++) {
                row.push_back(triangle[r-1][c-1] + triangle[r-1][c]);
            }
            row.push_back(1);
            triangle.push_back(row);
        }
        return triangle;
    }
};

string reduce(vector<int> q) {
    return reduce(next(q.begin()), q.end(), string("[" + to_string(q[0])), [](string a, int b) { return a + ", " + to_string(b); }) + string("]");
}

int main() {
    Solution s;

    vector<vector<int>> v;

    v = s.getRow(1);
    cout << "1 ? " << endl << reduce(next(v.begin()), v.end(), string(reduce(v[0])), [](string p, vector<int>& q) { return move(p) + ",\n" + reduce(q); }) << endl;

    v = s.getRow(2);
    cout << "2 ? " << endl << reduce(next(v.begin()), v.end(), string(reduce(v[0])), [](string p, vector<int>& q) { return move(p) + ",\n" + reduce(q); }) << endl;

    v = s.getRow(3);
    cout << "3 ? " << endl << reduce(next(v.begin()), v.end(), string(reduce(v[0])), [](string p, vector<int>& q) { return move(p) + ",\n" + reduce(q); }) << endl;

    v = s.getRow(4);
    cout << "3 ? " << endl << reduce(next(v.begin()), v.end(), string(reduce(v[0])), [](string p, vector<int>& q) { return move(p) + ",\n" + reduce(q); }) << endl;

    v = s.getRow(5);
    cout << "3 ? " << endl << reduce(next(v.begin()), v.end(), string(reduce(v[0])), [](string p, vector<int>& q) { return move(p) + ",\n" + reduce(q); }) << endl;

    return 0;
}
