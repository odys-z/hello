#include <iostream>

#include <vector>
#include "q797.h"
#include "../q658/q658/coutvectors.h"

using namespace std;

int main()
{
    Q797 q;

    vector<vector<int>> g = vector<vector<int>> {vector<int>{1, 2}, vector<int>{3}, vector<int>{3}, vector<int>{}};
    vector<vector<int>> dp0 = q.allPathsSourceTarget(g);

    CoutVectors::ints(dp0);

    g = vector<vector<int>> {vector<int>{2}, vector<int>{3}, vector<int>{1}, vector<int>{}};
    dp0 = q.allPathsSourceTarget(g);
    CoutVectors::ints(dp0);
    return 0;
}
