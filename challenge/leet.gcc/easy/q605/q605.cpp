/**
* 605. Can Place Flowers
* https://leetcode.com/problems/can-place-flowers/description/
*/

#include <vector>
#include <iostream>
#include <numeric>
#include <algorithm>
#include <cassert>

using namespace std;

class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        if (flowerbed.size() <= 1) return flowerbed[0] == 0;

        int prv = 0, c = 0, res = 0;

        auto plot = flowerbed.begin();
        c = *plot == 0? 2 : 0;
        plot++;
        while (plot != flowerbed.end()) {
            if (!*plot) c++;
            else {
                if (c > 0)
				    res += (c + 1) / 2 - 1;
				c = 0;
            }
            plot++;
        }
        
        res += c / 2;

        return res >= n;
    }
};

int main() {
    Solution s;
    vector<int>f;

    f = vector<int>{ 1,0,0,0,1 };
    assert(1 == s.canPlaceFlowers(f, 1));
    assert(0 == s.canPlaceFlowers(f, 2));

    f = vector<int>{ 1,0,0,0,1,0 };
    assert(1 == s.canPlaceFlowers(f, 1));
    assert(0 == s.canPlaceFlowers(f, 2));

    f = vector<int>{ 1,0,0,0,1,0,0 };
    assert(1 == s.canPlaceFlowers(f, 2));
    assert(0 == s.canPlaceFlowers(f, 3));

    f = vector<int>{ 0,1,0,0,0,1,0,0 };
    assert(1 == s.canPlaceFlowers(f, 2));
    assert(0 == s.canPlaceFlowers(f, 3));

    f = vector<int>{ 0,0,1,0,0,0,1,0,0 };
    assert(1 == s.canPlaceFlowers(f, 3));
    assert(0 == s.canPlaceFlowers(f, 4));

    f = vector<int>{ 0,0,1,0,0,0,0,1,0,0 };
    assert(1 == s.canPlaceFlowers(f, 3));
    assert(0 == s.canPlaceFlowers(f, 4));

    f = vector<int>{ 0,0,1,0,0,0,0,0,1,0,0 };
    assert(1 == s.canPlaceFlowers(f, 4));
    assert(0 == s.canPlaceFlowers(f, 5));

    f = vector<int>{ 0,0,0,1,0,0,0,0,0,1,0,0 };
    assert(1 == s.canPlaceFlowers(f, 4));
    assert(0 == s.canPlaceFlowers(f, 5));

    f = vector<int>{ 0,0,0,0,1 };
    assert(1 == s.canPlaceFlowers(f, 2));
    assert(0 == s.canPlaceFlowers(f, 3));

    f = vector<int>{ 0,0,0,0,0,1 };
    assert(1 == s.canPlaceFlowers(f, 2));
    assert(0 == s.canPlaceFlowers(f, 3));

    cout << "OK!" << endl;
    return 0;
}