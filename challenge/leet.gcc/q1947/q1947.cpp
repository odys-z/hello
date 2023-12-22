/*
 * 1947. Maximum Compatibility Score Sum
 * https://leetcode.com/problems/maximum-compatibility-score-sum/description/
 */
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int track(vector<vector<int>>& simi, int colvisit, vector<vector<int>>& students, vector<vector<int>>& mentors,
        int r, int R, int C) {

        int ans = 0;
        if (r < 0) return ans;

        for (int i = 0; i < R; i++) {
            int bit = 1 << i;
            if ((colvisit & bit) == 0)
                ans = max(ans, track(simi, colvisit | bit, students, mentors, r - 1, R, C) + simi[r][i]);
        }
        return ans;
    }

    int similar(vector<int>& mentor, vector<int>& student) {
        int sim = 0;
        for (int c = 0; c < mentor.size(); c++)
            sim += mentor[c] == student[c] ? 1 : 0;
        return sim;
    }

    int maxCompatibilitySum(vector<vector<int>>& students, vector<vector<int>>& mentors) {
        int R = mentors.size();
        vector<vector<int>> simi(R);

        for (int m = 0; m < R; m++)
            for (vector<int>& s : students)
                simi[m].push_back(similar(mentors[m], s));

        return track(simi, 0, students, mentors, R - 1, R, mentors[0].size());
    }
};

int main() {
    Solution sol;
    vector<vector<int>> s, m;
    s = vector<vector<int>>{ vector<int> {1,1,0}, vector<int> {1,0,1}, vector<int> {0,0,1} };
    m = vector<vector<int>>{ vector<int> {1,0,0}, vector<int> {0,0,1}, vector<int> {1,1,0} };
    cout << "8? " << sol.maxCompatibilitySum(s, m);
}
