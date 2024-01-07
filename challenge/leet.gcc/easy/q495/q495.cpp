/**
 * 495. Teemo Attacking
 * https://leetcode.com/problems/teemo-attacking/description/ 
 */

#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int findPoisonedDuration(vector<int>& timeSeries, int duration) {
        int begin = timeSeries[0], end = timeSeries[0];
        int totl = 0;

        for (int n : timeSeries) {
            if (n >= end + duration) {
                totl += end + duration - begin;
                begin = n;
            }
            end = n;
        }
        totl += end + duration - begin;
        return totl;
    }
};

int main() {
    Solution s;
    vector<int> v;
    int d;
    
    v = vector<int>{ 1,2 };
    d = 2;
    cout << "3? " << s.findPoisonedDuration(v, d) << endl;

    v = vector<int>{ 1,2 };
    d = 3;
    cout << "4? " << s.findPoisonedDuration(v, d) << endl;

    return 0;
}
