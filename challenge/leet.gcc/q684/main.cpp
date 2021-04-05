#include <iostream>

#include <q684.h>

using namespace std;

int main()
{
    Solution q;
    vector<vector<int>> v = { {1, 2}, {2, 3}, {1, 3} };
    cout << "expecting 1, 3: " << endl;
    for (int n : q.findRedundantConnection(v)) {
        cout<< n << " ";
    }
    cout << endl << "OK !" << endl;
    return 0;
}
