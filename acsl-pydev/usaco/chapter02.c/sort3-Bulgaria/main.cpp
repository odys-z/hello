/*
ID: odys.zh1
LANG: C++
TASK: sort3
 */
#include <iostream>
#include <fstream>

using namespace std;

int min (int a, int b) { return a < b ? a : b; }
int max (int a, int b) { return a > b ? a : b; }

int main()
{
    int len;
    ifstream fin;
    fin.open("sort3.in");
    fin >> len;
    int seq[len];
    // start 1, state 2, state 3, end 3
    int counts[4] = {0, 0, 0, 0};
    //                 1/1 2/1 3/1 x in 2     x in 3
    for (int i = 0; i < len; i++) {
        fin >> seq[i];
        counts[seq[i]] += 1;
    }
    fin.close();

//    int len = 6;
//    int seq[] = {1, 2, 3, 2, 3, 1};
//    int counts[] = {0, 2, 2, 2};

    int xofy[4][4] = { {0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0} };

    for (int i = 1; i < 4; i++) {
        counts[i] = counts[i - 1] + counts[i];
    }

    for (int j = 0; j < len; j++) {
        int v = seq[j];
        int buck = j < counts[1] ? 1 :
                   j < counts[2] ? 2 :
                   3;
        xofy[buck][v] += 1;
    }

    ofstream fout;
    fout.open("sort3.out");
    fout <<  + min(xofy[1][3], xofy[3][1])
             + min(xofy[2][3], xofy[3][2])
             + min(xofy[1][2], xofy[2][1])
             + 2 * (max(xofy[1][2], xofy[2][1]) - min(xofy[1][2], xofy[2][1]))
         << endl;
    fout.close();

    return 0;
}
