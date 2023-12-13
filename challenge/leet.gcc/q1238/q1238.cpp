/**
 * 1238. Circular Permutation in Binary Representation
 * https://leetcode.com/problems/circular-permutation-in-binary-representation/description/
 * 
 * A simple solution in python3:
 * [start ^ i ^ i >> 1 for i in range(1 << n)]
 * see
 * https://leetcode.com/problems/circular-permutation-in-binary-representation/solutions/414203/java-c-python-4-line-gray-code/comments/532223
 * 
 */

#include <vector>
#include <set>
#include <string>
#include <numeric>
#include <iostream>
#include <assert.h>

using namespace std;

class Solution {
public:
    int gtob(int g, int n) {
        int b = 0;
        for (; g; g = g >> 1)
            b ^= g;
        return b;
    }

    int btog(int b, int n) {
        return (b ^= (b >> 1)); // | (b & 1 << n - 1);
    }

    bool even(int n) {
        int b;
        b = n ^ (n >> 1);
        b = b ^ (b >> 2);
        b = b ^ (b >> 4);
        b = b ^ (b >> 8);
        b = b ^ (b >> 16);
        return (b & 1) == 0;
    }

    int nxtg(int g, int n) {
        if (even(g)) {
            return g ^ 1;
        }
        else return g == 1 << n-1 ? 0 : g ^ ((g & -g) << 1);
    }

    vector<int> circularPermutation(int n, int start) {
        vector<int> p0(1 << n, start);
        for (int i = 1; i < 1 << n; i++) {
            p0[i] = start = nxtg(start, n);
        }
        return p0;
    }
};

int main() {
    auto delimeter = [](string a, int b) {
        return move(a) + "," + to_string(b);
    };

    Solution s;

    vector<int> gray3{ 0b000, 0b001, 0b011, 0b010, 0b110, 0b111, 0b101, 0b100 };
    for (int i = 0; i < gray3.size(); i++)
        cout << gray3[i] << " : " << s.btog(i, 3) << endl;

    cout << "------" << endl;
    for (int i = 0; i < 1 << 3; i++)
        cout << i << " : " << s.gtob(gray3[i], 3) << endl;

    cout << "------" << endl;
    cout << gray3[0] << " : " << s.btog(0, 3) << endl;
    for (int i = 1; i < 1 << 3; i++)
        cout << gray3[i] << " : " << s.nxtg(gray3[i-1], 3) << endl;

    vector<int> v = s.circularPermutation(3, 2);
    cout << "expecting: 2,6,7,5,4,0,1,3" << endl;
    cout << "           " << accumulate(next(v.begin()), v.end(), to_string(v[0]), delimeter);

    return 0;
}