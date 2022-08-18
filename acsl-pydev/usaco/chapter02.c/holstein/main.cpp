/*
ID: odys.zh1
LANG: C++
TASK: holstein
 */
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

/**
   Test 1: TEST OK [0.004 secs, 1348 KB]
   Test 2: TEST OK [0.004 secs, 1348 KB]
   Test 3: TEST OK [0.004 secs, 1400 KB]
   Test 4: TEST OK [0.004 secs, 1400 KB]
   Test 5: TEST OK [0.004 secs, 1364 KB]
   Test 6: TEST OK [0.007 secs, 1424 KB]
   Test 7: TEST OK [0.007 secs, 1360 KB]
   Test 8: TEST OK [0.038 secs, 1352 KB]
   Test 9: TEST OK [0.025 secs, 1352 KB]
   Test 10: TEST OK [0.329 secs, 1400 KB]
 * @brief main
 * @return
 */

int maxv = 2 ^ 31;
int minScoops = maxv;

bool isEnough(vector<int> alreadyHas, int withx, int needings[], vector<vector<int>> vitamins)
{
    bool sutisfied = true;
    for (int v = 0; v < vitamins[withx].size(); v++)
    {
        sutisfied &= alreadyHas[v] + vitamins[withx][v] >= needings[v];
        if (!sutisfied) break;
    }
    return sutisfied;
}

vector<int> backtrack(vector<int> least, int withx, int needings[], vector<int> alreadyHas, int alreadyScoop, vector<vector<int>> vitamins) {

    if (withx >= least.size())
    {
        least[0] = least.size(); // types + 1
        return least;
    }

    least[withx] = withx;
    if (isEnough(alreadyHas, withx - 1, needings, vitamins))
    {
        least[0] = alreadyScoop + 1;
        return least;
    }

    vector<int> tryWithThis = alreadyHas;
    for (int v = 0; v < alreadyHas.size(); v++)
    {
        tryWithThis[v] = alreadyHas[v] + vitamins[withx - 1][v];
    }

    vector<int> scoopWith1 = backtrack(least, withx + 1, needings, tryWithThis, alreadyScoop + 1, vitamins);

    least[withx] = -1;
    vector<int> scoopWith0 = backtrack(least, withx + 1, needings, alreadyHas, alreadyScoop, vitamins);

    if (scoopWith0[0] < scoopWith1[0])
    {
        scoopWith0[withx] = -1;
        return scoopWith0;
    }
    else
    {
        scoopWith1[withx] = withx;
        // scoopWith1[0] += 1;
        return scoopWith1;
    }
}

int main()
{
    int V, types;
    ifstream fin;
    fin.open("holstein.in");
    fin >> V;
    int needings[V];
    for (int v = 0; v < V; v++)
    {
        fin >> needings[v];
    }

    fin >> types;
    // int vitamins[types][V];
    vector<vector<int>> vitamins;

    for (int t = 0; t < types; t++)
    {
        vector<int> vitype(V);
        for (int v = 0; v < V; v++)
        {
            fin >> vitype[v];
        }
        vitamins.push_back(vitype);
    }

    vector<int> least(types + 1, -1); // [scoops, -1 or 0..types]
    least[0] = 0;

    vector<int> alreadys(V, 0);   // already scooped amoount
    least = backtrack(least, 1, needings, alreadys, 0, vitamins);

    ofstream fout;
    fout.open("holstein.out");
    // fout << miniscoops << endl;
    int has1 = false;
    for (int c = 0; c < least.size(); c++) {
        if (least[c] >= 0) {
            if (has1)
                fout << ' ';
            has1 = true;
            fout << least[c];
        }
    }
    fout << endl;
    fout.close();

    return 0;
}
