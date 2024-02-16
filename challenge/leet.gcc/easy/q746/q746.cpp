/**
 * 746. Min Cost Climbing Stairs
 * https://leetcode.com/problems/min-cost-climbing-stairs/description/
 */

#include <vector>
#include <cassert>
#include <iostream>

using namespace std;

class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        // [1,100,1,1,1,100,1,1,100,1]
        // [1,100,2,3,3,103,4,5,104,5]
        int s = cost.size();
        for (int i = 2; i < s; i++)
            cost[i] += min(cost[i - 1], cost[i - 2]);

        return min(cost[s - 1], cost[s - 2]);
    }
};

int main() {
    Solution s;
    vector<int> cost;

    cost = vector<int>{ 1,100,1,1,1,100,1,1,100,1 };
    assert(6 == s.minCostClimbingStairs(cost));

    cout << "ok" << endl;
}