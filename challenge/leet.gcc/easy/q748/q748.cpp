/***
 * 748. Shortest Completing Word
 * https://leetcode.com/problems/shortest-completing-word/description/
 */

#include <vector>
#include <map>
#include <iostream>
#include <cassert>

using namespace std;

class Solution {
public:
    string shortestCompletingWord(string licensePlate, vector<string>& words) {
        map<char, int> plate;
        for (char c : licensePlate) {
            if (!isalpha(c)) continue;
            c = tolower(c);

            if (plate.find(c) != plate.end())
                plate[c] += 1;
            else plate[c] = 1;
        }

        int minl = 16;
        string ans;
        for (string s : words) {
            if (s.size() < minl) {
                map<char, int> test;
                for (char c : s) {
                    c = tolower(c);
                    if (test.find(c) != test.end())
                        test[c] += 1;
                    else 
                        test[c] = 1;
                }

                bool like = true;
                for (pair<char, int> p : plate)
                    if (test.find(p.first) == test.end() || test[p.first] < plate[p.first]) {
                        like = false;
                        break;
                    }

                if (like) {
                    minl = s.size();
                    ans = s;
                }
            }
        }

        return ans;
    }
};

int main() {
    Solution s;
    string p;
    vector<string> words{ "step","steps","stripe","stepple" };

    assert("steps" == s.shortestCompletingWord("1s3 PSt", words));

    words = vector<string>{ "looks","pest","stew","show" };
    assert("pest" == s.shortestCompletingWord("1s3 456", words));

    words = vector<string>{ "vvu","wuv","xyzrst","abcde" };
    assert("" == s.shortestCompletingWord("Vv3 wu", words));

    words = vector<string>{ "vvu","Wuv", "uvW","xyzrst","abcde"};
    assert("Wuv" == s.shortestCompletingWord("V3 wu", words));

    cout << "ok" << endl;
}
