#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

vector<vector<int>> shares;

int main()
{
    ifstream fin;
    fin.open("cocom.in");

    int c;
    fin >> c;

    shares = vector<vector<int>>(c, vector<int>(c, 0));
    for (int k = 0; k < c; k++)
    {
        int i, j, p;
        fin >> i >> j >> p;
        shares[i][j] = c;

        vector<int> contrli;
        for (int t = 0; t < c; t++)
        {
            if (shares[t][i] > 0 and t != i)
            {
                contrli.push_back(t);
            }
        }

        while (contrli.size() > 0) {
            vector<int> contrlt;
            for (int t: contrli)
            {
                shares[t][j] += shares[t][i] * shares[i][j];
                if (shares[t][i] > 0 and t != i)
                {
                    contrlt.push_back(t);
                }
            }
            contrli = contrlt;
        }
    }

    ofstream cout;
    cout.open("cocom.out");
    for (ulong contlr = 0; contlr < shares.size(); contlr++)
        for (ulong co = 0; co < shares[contlr].size(); co++ )
            if (shares[contlr][co] > 0)
                cout << contlr << ' ' << co << endl;
    cout.close();
    return 0;
}
