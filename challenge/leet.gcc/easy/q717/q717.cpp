/**
 *
 */

#include <vector>
#include <iostream>
#include <cassert>

using namespace std;

class Solution {
public:
    bool isOneBitCharacter(vector<int>& bits) {
        bool c = false;
        for (int i = 0; i < bits.size(); i++)
            if (bits[i] == 1)
                c = false, i++;
            else c = true;
        return c;
    }
};

int main() {
    Solution s;
    vector<int> bits;

    bits = vector<int>{0};
    assert( s.isOneBitCharacter(bits));

    bits = vector<int>{1,0};
    assert(!s.isOneBitCharacter(bits));

    bits = vector<int>{1,1,0};
    assert( s.isOneBitCharacter(bits));

    bits = vector<int>{1,1,0,1,1};
    assert(!s.isOneBitCharacter(bits));

    bits = vector<int>{1,1,0,0};
    assert( s.isOneBitCharacter(bits));

    bits = vector<int>{1,0,1,0};
    assert(!s.isOneBitCharacter(bits));

    cout << "OK" << endl;
    return 0;
}