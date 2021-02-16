#include <QCoreApplication>
#include <iostream>

#include "coutvectors.h"
#include "q658.h"

using namespace std;

int main(int argc, char *argv[])
{
    // QCoreApplication a(argc, argv);
    Q658* q = new Q658();

    vector<int> arr {1, 2, 3};
    vector<int> reslt = q->findClosestElements(arr, 3, 2);
    CoutVectors::ints(reslt); // expect [1, 2, 3]

    arr = vector<int>{1, 2};
    reslt = q->findClosestElements(arr, 1, 2);
    CoutVectors::ints(reslt); // expect [1]

    cout << endl << "OK!" << endl;
    return 0;
}
