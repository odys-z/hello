/*
ID: odys.zh1
LANG: C++
TASK: runround
 */
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

/*
   Test 1: TEST OK [0.004 secs, 1360 KB]
   Test 2: TEST OK [0.021 secs, 1364 KB]
   Test 3: TEST OK [0.007 secs, 1412 KB]
   Test 4: TEST OK [0.011 secs, 1356 KB]
   Test 5: TEST OK [0.165 secs, 1408 KB]
   Test 6: TEST OK [0.088 secs, 1352 KB]
   Test 7: TEST OK [0.277 secs, 1364 KB]
 */

vector<int> spread(int n)
{
    vector<int> digits;
    while (n > 0)
    {
        digits.insert(digits.begin(), n % 10);
        n /= 10;
    }
    return digits;
}

int repack(vector<int> digits) {
    int v = 0;
    for (int d : digits)
        v = v * 10 + d;
    return v;
}

/**
 UNIQUE digits
*/

/**
 * @param count
 * @return digits sum, -1 if not a unique digits number
 */
int sumDigits(vector<int> digits)
{
    int sm = 0;
    for (ulong x = 0; x < digits.size(); x++)
        sm += digits[x];
    return sm;
}

int countDigits(int x)
{
    int c = 0;
    while (x > 0)
    {
        c++;
        x /= 10;
    }
    return c;
}

/**
 * @brief isRound
 * @param digits [most-significant, .. unit-digit]
 * @return
 */
bool isRound(vector<int> digits)
{
    //        10 ^ 0 low ...   4  5
    int masks[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    int used[]  = {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1 };

    int d = digits.size();
    for (int x = 0; x < d; x++)
    {
        if (masks[x] != 0 or digits[x] == 0 or used[digits[x]] >= 0 or (digits[x] % d) == 0)
            return false;
        masks[x] = digits[x];
        used[digits[x]] = digits[x];
    }

    // run
    int p = 0;
    while (masks[p] != 0)
    {
        int step = masks[p];
        masks[p] = 0;
        p += step;
        p %= d;
    }

    for (int x = 0; x < d; x++)
        if (masks[x] > 0)
            return false;
    return p % d == 0;
}

int runround(int N)
{
    vector<int> digits = spread(N);
    int sm = sumDigits(digits);

    while(!isRound(digits))
    {
        N++;
        digits = spread(N);
        sm = sumDigits(digits);
    }

    int d = countDigits(N);
    while (!isRound(digits))
    {
        N += d;
        d = countDigits(N);
        digits = spread(N);
        sm = sumDigits(digits);
    }

    return repack(digits);
}

int main()
{
    int N;
    ifstream fin;
    fin.open("runround.in");
    fin >> N;
    fin.close();

    int res = runround(++N);

    ofstream cout;
    cout.open("runround.out");
    cout << res << endl;
    cout.close();

    return 0;
}
