/*
ID: odys.zh1
LANG: C++
TASK: concom
 */

#include <iostream>
#include <fstream>
#include <vector>
#include <assert.h>

#define _101 7

using namespace std;

vector<vector<double>> shares(_101, vector<double>(_101, 0));

int main()
{
    ifstream fin;
    fin.open("concom.in");

    int c;
    fin >> c;
    assert(c > 0);
    c++;

    // shares = vector<vector<int>>(c, vector<int>(c, 0));
    for (int k = 0; k < c; k++)
    {
        int i, j, p;
        fin >> i >> j >> p;
        shares[i][j] = p;
        vector<int> contrli;
        contrli.push_back(i);

        int check = 0;
        while (contrli.size() > 0 and check < _101) {
            check++;
            vector<int> contrlt;
            for (int con: contrli)
            for (int t = 1; t < c; t++)
            {
                if (t == con or t == j or t == i)
                    continue;
                shares[t][j] += (shares[t][con] * shares[con][j] / 100);
                if (shares[t][j] > 0)
                {
                    contrlt.push_back(t);
                }
            }
            contrli = contrlt;
            contrlt.clear();
        }
        contrli.clear();
    }

    ofstream cout;
    cout.open("concom.out");
    for (ulong contlr = 0; contlr < shares.size(); contlr++)
        for (ulong co = 0; co < shares[contlr].size(); co++ )
            if (shares[contlr][co] > 50)
                cout << contlr << ' ' << co << endl;
    cout.close();
    return 0;
}
