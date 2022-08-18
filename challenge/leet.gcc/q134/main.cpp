#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        if (gas.size() == 1)
            return gas[0] >= cost[0] ? 0 : -1;

        int sum = 0;
        int start = -1;
        for (ulong i = 0; i < gas.size(); i++)
        {
            gas[i] -= cost[i];
        }

        for (ulong i = 0; i < gas.size() * 2; i++)
        {
            ulong ix = i % gas.size();
            if (sum + gas[ix] < 0)
            {
                if (ix < i)
                    return -1;
                else
                {   sum = 0;
                    continue;
                }
            }
            else
            {
                if (sum == 0)
                {
                    start = ix;
                }
                sum += gas[ix]; // sum >= 0
            }
        }
        return start;
    }

    int canCompleteCircuit2(vector<int>& gas, vector<int>& cost) {
        if (gas.size() == 1)
            return gas[0] >= cost[0] ? 0 : -1;

        int stop = gas.size() * 2;
        int sum = 0, maxsum = 0;
        int start = -1, maxstart = -1;
        for (int i = 0; i < stop; i++)
        {
            int step = i % gas.size();
            if (sum == 0)
            {
                start = step;
            }

            if (sum + gas[step] - cost[step] < 0)
            {
                sum = 0;
                start = step;
                maxsum = 0;
                maxstart = start;
                if (i > step)
                {
                    maxstart = -1;
                    break;
                }
            }
            else
            {   // keep start
                sum += gas[step] - cost[step];
                if (maxstart < 0)
                {
                    maxsum = sum;
                    maxstart = start;
                }
            }
        }
        return maxstart;
    }
};

int main()
{
    Solution s;

    // 1
    vector<int> gas  = {0, 2};
    vector<int> cost = {1, 1};
    cout << "1 : " << s.canCompleteCircuit(gas, cost) << endl;

    // 0 (11)
    gas  = {0, 3, 1, 1, 1, 2, 1, 0, 0, 1, 2, 1, 1, 1};
    cost = {1, 1, 2, 0, 1, 2, 0, 1, 1, 1, 3, 0, 1, 0};
    cout << "0/11 : " << s.canCompleteCircuit(gas, cost) << endl;

    // -1
    gas  = {1, 1};
    cost = {1, 2};
    cout << "-1 : " << s.canCompleteCircuit(gas, cost) << endl;

    // 1
    gas  = {1, 2};
    cost = {2, 1};
    cout << "1 : " << s.canCompleteCircuit(gas, cost) << endl;

    // 0
    gas  = {1};
    cost = {1};
    cout << "0 : " << s.canCompleteCircuit(gas, cost) << endl;

    // -1
    gas  = {1,2,3,4,0,5};
    cost = {3,4,5,1,1,2};
    cout << "-1 : " << s.canCompleteCircuit(gas, cost) << endl;

    // 3
    gas  = {1,2,3,4,5};
    cost = {3,4,5,1,2};
    cout << "3 : " << s.canCompleteCircuit(gas, cost) << endl;
    return 0;
}
