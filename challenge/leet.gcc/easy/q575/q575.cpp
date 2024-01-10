/**
 * 575. Distribute Candies
 * https://leetcode.com/problems/distribute-candies/description/
 */

#include <vector>
#include <set>
#include <bitset>
#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:
    int distributeCandies(vector<int>& candyType) {
        set<int> types;
        for (int t : candyType)
            types.insert(t);
        return min(candyType.size() / 2, types.size());
    }

    int distributeCandies2(vector<int>& candyType) {
        bitset<100002> p;
        bitset<100001> n;

        for (int t : candyType)
            if (t >= 0) p.set(t);
            else n.set(-t);
        return min(p.count() + n.count(), candyType.size() / 2);
    }
};

int main() {
    Solution s;
    vector<int> v;

    v = vector<int>{ 1,1,2,2,3,3 };
    cout << "3? " << s.distributeCandies(v) << endl;
    cout << "3? " << s.distributeCandies2(v) << endl;

    v = vector<int>{ 6,6,6,6 };
    cout << "1? " << s.distributeCandies(v) << endl;
    cout << "1? " << s.distributeCandies2(v) << endl;


    v = vector<int>{1,-2,3,-4,-5,-6,-7,-8,-9,-10,100000,0,-100000,99999 };
    cout << "7? " << s.distributeCandies(v) << endl;
    cout << "7? " << s.distributeCandies2(v) << endl;
    return 0;
}
