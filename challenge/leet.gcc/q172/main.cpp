#include <iostream>
#include <vector>

#include "q172.h"
#include "../q658/q658/coutvectors.h"

using namespace std;

int main()
{
    Q172* q172 = new Q172;

    cout << "5:\t" << q172->trailingZeroes(5) << endl;
    cout << "25:\t" << q172->trailingZeroes(25) << endl;
    cout << "125:\t" << q172->trailingZeroes(125) << endl;
    cout << "625:\t" << q172->trailingZeroes(625) << endl;
    cout << "3125:\t" << q172->trailingZeroes(3125) << endl;

    cout << endl << "OK!" << endl;
    return 0;
}
