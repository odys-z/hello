#include <iostream>

#include "q202.h"

using namespace std;

int main()
{
    Solution s;
    cout << "1 " << s.isHappy(1) << endl;
    cout << "2 " << s.isHappy(2) << endl;
    cout << "3 " << s.isHappy(3) << endl;
    cout << "7 " << s.isHappy(7) << endl;
    cout << "10 " << s.isHappy(10) << endl;
    cout << "18 " << s.isHappy(18) << endl;
    cout << "19 " << s.isHappy(19) << endl;
    cout << "20 " << s.isHappy(20) << endl;
    cout << "1999 " << s.isHappy(1999) << endl;
    cout << "299999 " << s.isHappy(299999) << endl;
    return 0;
}
