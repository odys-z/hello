/*
ID: odys.zh1
LANG: C++
TASK: hamming
 */
#include <iostream>
#include <fstream>
#include <vector>
#include <set>

using namespace std;

int count(int v)
{
    int counter[] = {1, 2, 4, 8, 16, 32, 64, 128, 256};

    int cnt = 0;
    for (int c : counter)
    {
        if ((c & v) > 0)
            cnt++;
    }

    return cnt;
}

int main()
{
    //  64 8  7
    int N, B, D;
    ifstream fin;
    fin.open("hamming.in");
    // 16 7 3
    fin >> N >> B >> D;
    fin.close();

    // 7 11 13 14 19 21 22 25 26 28 35 37 38 41 42 44 49 50 52 56 67 69 70 73 74 76 81 82 84 88 97 98 100 104 112
    vector<int> dists;
    for (int i = 0; i < (1 << (B+1)); i++)
    {
        if (count(i) == 3)
            dists.push_back(i);
    }

    vector<int> codes;
    codes.push_back(0);

    for (int dist : dists)
    {
        bool yes = true;
        for (int c : codes)
        {
            if (c == dist || count(c ^ dist) < D)
            {
                yes = false;
                break;
            }
        }
        if (yes)
            codes.push_back(dist);
        if (codes.size() >= (ulong) N)
            break;
    }

    ofstream cout;
    cout.open("hamming.out");

    for (int x = 0; x < codes.size() - 1; x++)
    {
        cout << codes[x];
        if (x % 10 != 9)
            cout << " ";
        else cout << endl;
    }
    cout << codes[codes.size() - 1] << endl;

    return 0;
}
