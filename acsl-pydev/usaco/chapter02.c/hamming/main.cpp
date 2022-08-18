/*
ID: odys.zh1
LANG: C++
TASK: hamming
 */
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <bitset>

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

/**
   Test 1: TEST OK [0.007 secs, 1360 KB]
   Test 2: TEST OK [0.004 secs, 1376 KB]
   Test 3: TEST OK [0.004 secs, 1408 KB]
   Test 4: TEST OK [0.004 secs, 1344 KB]
   Test 5: TEST OK [0.004 secs, 1336 KB]
   Test 6: TEST OK [0.004 secs, 1372 KB]
   Test 7: TEST OK [0.004 secs, 1348 KB]
   Test 8: TEST OK [0.007 secs, 1348 KB]
   Test 9: TEST OK [0.007 secs, 1360 KB]
   Test 10: TEST OK [0.007 secs, 1344 KB]
   Test 11: TEST OK [0.007 secs, 1348 KB]
 * @brief main
 * @return
 */
int main()
{
    //  64 8  7
    int N, B, D;
    ifstream fin;
    fin.open("hamming.in");
    // 16 7 3
    fin >> N >> B >> D;
    fin.close();

//    N = 10, B = 8, D = 4;

    // Can't find some better algorithsm ?
    // 7 11 13 14 19 21 22 25 26 28 35 37 38 41 42 44 49 50 52 56 67 69 70 73 74 76 81 82 84 88 97 98 100 104 112
//    vector<short> dists;
//    for (int i = 0; i < (1 << (B+1)); i++)
//    {
//        if (count(i) == 3)
//            dists.push_back(i);
//    }

//    set<short> codes;
//    codes.insert(0);
//    for (ulong i = 0; i < dists.size(); i++)
//    {
//        for (ulong j = i; j < dists.size(); j++)
//        {
//            [&]{
//                int x = i == j ? dists[i] : dists[i] ^ dists[j];
//                for (int c : codes) {
//                    if (count(c ^ x) < 3)
//                        return;
//                }
//                codes.insert(x);
//            }();
//        }
//    }
    set<short> codes;
    for (int i = 0; i < (2 << B); i++)
    {
        [&]{
            for (int c : codes) {
                if (count(c ^ i) < D)
                    return;
            }
            codes.insert(i);
        }();
        if (codes.size() >= N)
            break;
    }

    ofstream cout;
    cout.open("hamming.out");

    set<short>::iterator it = codes.begin();
    int cnt = 0;
    while (it != codes.end())
    {
        cout << *it;
        it++;
        cnt %= 10;
        if (cnt == 9)
            cout << endl;
        else if (it != codes.end())
            cout << " ";
        cnt++;
    }
    if ((cnt % 10) != 0)
        cout << endl;
    return 0;
}
