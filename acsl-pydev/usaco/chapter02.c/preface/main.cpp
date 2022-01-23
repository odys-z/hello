/*
ID: odys.zh1
LANG: C++
TASK: preface
 */
#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>

using namespace std;

/* Test 1: TEST OK [0.007 secs, 1352 KB]
   Test 2: TEST OK [0.004 secs, 1348 KB]
   Test 3: TEST OK [0.004 secs, 1412 KB]
   Test 4: TEST OK [0.004 secs, 1424 KB]
   Test 5: TEST OK [0.007 secs, 1348 KB]
   Test 6: TEST OK [0.004 secs, 1420 KB]
   Test 7: TEST OK [0.007 secs, 1292 KB]
   Test 8: TEST OK [0.007 secs, 1352 KB]
*/

char digits[4][3] = { {'I', 'V', 'X'}, {'X', 'L', 'C'}, {'C', 'D', 'M'}, {'M', '?', '?'} };

// 10^0: I, II, III, IV, V, VI, VII, VIII, IX
// 10^1: X  XX  XXX  XL  L  LX  LXX  LXXX  XC
// 10^2: C  CC  CCC  CD  D  DC  DCC  DCCC  CM
// 10^3: M  MM  MMM  ?
vector<vector<short>> romandig = {
   {0, 0, 0}, // 10^0: I V X
   {0, 0, 0}, // 10^1: X L C
   {0, 0, 0}, // 10^2: C D M
   {0, 0, 0}  // 10^3: M ? ?
};
// C D I L M V X
// (2,0) (2,1)  (0,0) (1,1) (3,0) (0,1) (1,0)

vector<short> number(int digit, int p)
{
    digit %= (int)pow(10, p + 1);
    digit /= (int)pow(10, p);
    short I = (digit % 5) == 4 ? 1 : digit % 5;
    short V = digit >= 4 and digit < 9 ? 1 : 0;
    short X = digit == 9 ? 1 : 0;
    return vector<short> {I, V, X};
}

int main()
{
    //  5 -> I 7   V 2
    int N;
    ifstream fin;
    fin.open("preface.in");
    fin >> N;
    fin.close();

    for (int page = 1; page <= N; page++)
    for (int p = 0; p <= 3; p++) {
        vector<short> nums = number(page, p);
        romandig[p][0] += nums[0];
        romandig[p][1] += nums[1];
        romandig[p][2] += nums[2];
    }

    // X C M
    for (int x = 0; x < 3; x++)
    {
        romandig[x+1][0] += romandig[x][2];
        romandig[x][2] = 0;
    }

    // char names[] = { 'C', 'D', 'I', 'L', 'M', 'V', 'X' };
    // int seq[7][2] = { {2,0}, {2,1}, {0,0}, {1,1}, {3,0}, {0,1}, {1,0} };

    ofstream cout;
    cout.open("preface.out");

    for (int s = 0; s < 4; s++)
    for (int t = 0; t < 3; t++)
    {
        int count = romandig[s][t];
        if (count > 0)
            cout << digits[s][t] << " " << count << endl;
    }
    return 0;
}
