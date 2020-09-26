#ifndef SOLUTION_H
#define SOLUTION_H

#include <vector>

using std::vector;

/**
 * @brief Q1295 Sep 26, 2020<br>
 * Runtime: 8 ms, faster than 96.13% of C++ online submissions for Find Numbers with Even Number of Digits.<br>
 * Memory Usage: 10.1 MB, less than 23.18% of C++ online submissions for Find Numbers with Even Number of Digits.
 */
class Solution
{
public:
    Solution();

    int findNumbers(vector<int>& nums)
    {
        int cnt = 0;
        for(auto it = begin(nums); it != end(nums); ++it) {
            int n = *it;
            while (n >= 100) n /= 100;
            if (n >= 10)
                cnt++;
        }
        return cnt;
    }
};

#endif // SOLUTION_H
