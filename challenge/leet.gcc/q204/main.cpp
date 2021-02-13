#include <iostream>

#include "q204.h"
using namespace std;

int main()
{
    Q204* q204 = new Q204;
    cout << "5    (2)    :\t" << q204->countPrimes(5) << endl;
    cout << "20   (8)    :\t" << q204->countPrimes(20) << endl;
    cout << "21   (8)    :\t" << q204->countPrimes(21) << endl;
    cout << "24   (9)    :\t" << q204->countPrimes(24) << endl;
    cout << "12548(1499) :\t" << q204->countPrimes(12548) << endl;
    return 0;
}
