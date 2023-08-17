#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int hIndex(vector<int>& citations) {
        for (int i = citations.size() - 1; i >= 0; i--)
        {
            if (citations.size() - i >= citations[i])
                return citations.size() - i == citations[i] ? citations[i] : citations.size() - i -1;
                // return citations.size() - i -1;
        }
        return min(citations[0], (int)citations.size());
    }
};

int main()
{
    Solution s;
    vector<int> u = {11, 15};
    cout << "2: " << s.hIndex(u) << endl;

    vector<int> w = {2};
    cout << "1: " << s.hIndex(w) << endl;

    vector<int> v = {0, 1, 1, 2, 2};
    cout << "2: " << s.hIndex(v) << endl;

    v = {0, 1, 1, 21, 21};
    cout << "2: " << s.hIndex(v) << endl;
    return 0;
}
