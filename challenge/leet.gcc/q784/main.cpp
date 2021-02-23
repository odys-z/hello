#include <iostream>
#include <vector>

#include "q784.h"
#include "../q658/q658/coutvectors.h"

using namespace std;

int main()
{
    Solution s;

    vector<string> reslt = s.letterCasePermutation("a1b2");
    cout << "case: 'a1b2'" << endl;
    cout << "expect: ['a1b2', 'a1B2', 'A1b2', 'A1B2']" << endl;
    cout << "actual: ";
    CoutVectors::strs(reslt);
    cout << endl;
    return 0;
}
