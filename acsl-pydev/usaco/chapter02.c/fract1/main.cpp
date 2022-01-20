/*
ID: odys.zh1
LANG: C++
TASK: frac1
 */
#include <iostream>
#include <fstream>

using namespace std;

/**
 * n, d = l.n + r.n, l.d + r.d
 *
   0/1                                                           1/1
                               1/2
                  1/3                      2/3
        1/4              2/5         3/5                 3/4
    1/5      2/7     3/8    3/7   4/7   5/8       5/7         4/5
 *
 * But what's behind this?
 *
 * @brief main

   Test 1: TEST OK [0.004 secs, 1356 KB]
   Test 2: TEST OK [0.004 secs, 1344 KB]
   Test 3: TEST OK [0.004 secs, 1364 KB]
   Test 4: TEST OK [0.004 secs, 1344 KB]
   Test 5: TEST OK [0.007 secs, 1384 KB]
   Test 6: TEST OK [0.004 secs, 1364 KB]
   Test 7: TEST OK [0.011 secs, 1352 KB]
   Test 8: TEST OK [0.028 secs, 1356 KB]
   Test 9: TEST OK [0.052 secs, 1360 KB]
   Test 10: TEST OK [0.088 secs, 1344 KB]
   Test 11: TEST OK [0.235 secs, 1348 KB]
 */
int N = 0;


void midAcc(ostream& o, int ln, int ld, int rn, int rd) {
    int n = ln + rn;
    int d = ld + rd;

    if (n > d || d > N)
        return ;
    midAcc(o, ln, ld, n, d);

    o << n << '/' << d << endl;

    midAcc(o, n, d, rn, rd);
}


int main()
{
    // cin >> N;
    ifstream fin;
    fin.open("frac1.in");
    fin >> N;
    fin.close();

    ofstream fout;
    fout.open("frac1.out");

    fout << 0 << "/" << 1 << endl;
    // midAcc(cout, 0, 1, 1, 1);
    midAcc(fout, 0, 1, 1, 1);
    fout << 1 << "/" << 1 << endl;

    fout.close();
    return 0;
}
