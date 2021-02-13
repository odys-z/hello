#include <QCoreApplication>
#include <iostream>

#include "q658.h"

using namespace std;

int main(int argc, char *argv[])
{
    // QCoreApplication a(argc, argv);
    Q658* q = new Q658();
    vector<int> arr {1, 2};
    vector<int> reslt = q->findClosestElements(arr, 1, 2);
    // std::copy(arr.begin(), arr.end(), std::ostream_iterator<char>(std::cout, " "));
    cout << "OK!" << endl;
    return 0;
}
