/**
 * 1769. Minimum Number of Operations to Move All Balls to Each Box
 * https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/
*/

#include <vector>
#include <string>
#include <numeric>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<int> minOperations(string boxes) {

        size_t len = boxes.length();
        vector<vector<int>> right = vector<vector<int>>(len); // [[right-count, right-sum]]
        int ball = boxes[len - 1] == '0' ? 0 : 1;
        right[len - 1] = vector<int>{ 0, 0 };

        vector<int> ans = vector<int>(len);
        ans[len-1] = 0;

        for (int bx = len - 2; bx >= 0; bx--) {
            int right1 = boxes[bx + 1] == '0' ? 0 : 1;
            right[bx] = vector<int>{
                right[bx + 1][0] + right1, // count = right-count + [box+1]
                right[bx + 1][0] + right[bx + 1][1] + right1 // sum = right-sum + right-count + [box+1]
            };
        }

        int leftcnt = 0; // boxes[0] == '0' ? 0 : 1;
        int leftsum = 0;
        ans[0] = right[0][1];

        for (int bx = 1; bx < len; bx++) {
            int left1 = boxes[bx - 1] == '0' ? 0 : 1;
            leftsum += leftcnt + left1;
            leftcnt += left1;
            ans[bx] = leftsum + right[bx][1];
        }
        return ans;
    }
};

string reduce(vector<int> v) {
    return "[" + reduce(next(v.begin()), v.end(), to_string(v[0]), [](string a, int b) { return move(a) + "," + to_string(b); }) + "]";
}

int main() {

    Solution s;
    string boxes;

    boxes = "001011";
    cout << boxes << endl << "[11,8,5,4,3,4]?" << endl << reduce(s.minOperations(boxes)) << endl;

    boxes = "110";
    cout << boxes << endl << "[1,1,3]?" << endl << reduce(s.minOperations(boxes)) << endl;

    cout << "OK!" << endl;
    return 0;
}