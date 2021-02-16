#include <iostream>

#include "inter.h"

using namespace std;

int main()
{
    // 4
    // string s0 = string("1314159265");
    // cout << stoi(s0.substr(0, 1)) + stoi(s0.substr(1, 1)) << endl;
    AscInter q;
    string s = q.leastNums("1314159265");
    cout << "1314159265            expecting:           3 5 6 29 51 - " << s << endl;
    s = q.leastNums("11223344");
    cout << "11223344              expecting:            1 4 43 322 - " << s << endl;
    s = q.leastNums("225897257");
    cout << "225897257             expecting:             25 75 279 - " << s << endl;
    s = q.leastNums("412342987656784352");
    cout << "412342987656784352    expecting:  1234 2534 8765 67892 - " << s << endl;
    s = q.leastNums("33984567176534321");
    cout << "33984567176534321     expecting:   398 1234 3567 17654 - " << s << endl;

    s = q.leastNums("111235813213455");
    cout << "111235813213455       expecting:    1 5 54 312 318 532 - " << s << endl;
    s = q.leastNums("219782017");
    cout << "219782017             expecting:             19 71 287 - " << s << endl;
    s = q.leastNums("420165102");
    cout << "420165102             expecting:                  2016 - " << s << endl;
    s = q.leastNums("26625122455675318505");
    cout << "26625122455675318505  expecting: 66 505 813 5765 54221 - " << s << endl;
    s = q.leastNums("364311");
    cout << "364311                expecting:                   643 - " << s << endl;

    s = q.leastNums("105544332221");
    cout << "105544332221          expecting:     0 1 2 22 33 44 55 - " << s << endl;
    s = q.leastNums("10550440330022021");
    cout << "10550440330022021     expecting:     0 1 2 22 33 44 55 - " << s << endl;

    return 0;
}
