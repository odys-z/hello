#include <iostream>
#include <q1130.h>

using namespace std;

int main()
{
    Solution s;
    vector<int> v = {6, 2, 4};
    cout << s.mctFromLeafValues(v) << endl;  // 32
    vector<int> w = {6,1,5,5,5,5,5,15,6};
    cout << s.mctFromLeafValues(w) << endl;  // 315
    return 0;
}
