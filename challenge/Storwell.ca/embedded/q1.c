#include <stdlib.h>
#include <iostream>
using namespace std;

void squires(int, int);

int main(int argc, char *argv[])
{
    cout << "Question 1" << endl;
    if (3 != argc) {
        cout << "useage: q1 N M" << endl;
        exit(-1);
    }

    

    int n = atoi(argv[1]);
    int m = atoi(argv[2]);

    squires(n, m);
}

void squires(int n, int m) {
    int t;

    if (n < m) {
        t = n; n = m; m = t;
    }

    int q = n / m;
    int r = n - q * m;

    for (int i = 0; i < q; i++) {
        cout << m << "x" << m;
        if (i < q - 1)
            cout << ", ";
    }

    if (r > 0) {
        cout << ", ";
        squires(m, r);
    }
    cout << endl;
}
