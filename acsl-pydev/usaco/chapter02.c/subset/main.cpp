/*
ID: odys.zh1
LANG: C++
TASK: subset
 */
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

/**
 Test 1: TEST OK [0.004 secs, 1364 KB]
 Test 2: TEST OK [0.004 secs, 1360 KB]
 Test 3: TEST OK [0.007 secs, 1336 KB]
 Test 4: TEST OK [0.004 secs, 1360 KB]
 Test 5: TEST OK [0.004 secs, 1356 KB]
 Test 6: TEST OK [0.004 secs, 1404 KB]
 Test 7: TEST OK [0.000 secs, 1376 KB]

 * Referenc: https://jvonk.github.io/usaco/2018/10/12/subset.html
 *
 * 1   2   3   4  ...  n-1   {n}   ...  s = {n(n-1) / 2}
 * A1  A2  A3  A4  ... An-1   An   ...   As
 * where ai is the number of ways can sum up to the value.
 *
 * Now add n to the serials
 * 1   2   3   4  ...  n-1   n   ...  s' = (n+1)n / 2
 * A1  A2  A3  A4  ... An-1  An' ...   As'
 * where
 * An' = An + 1, because there is a new wAy, add by n;
 * A(n+1)' = A(n + 1) + 1, like above
 * ...
 * As' = As + 1, if As = 0, theer is only 1 way - add by n.
 * We need to find out As2, where s2 = s / 2, which is somewhere in the middle of ... .
 *
 * Conclusion:
 * Add like the above way from A1 to As2, stop at n.
 *
 * Ai beyond as2 are not needed. That's why algorithm of Tomikov stop at s.
 *
 * @brief main
 * @return
 */
// deprecated: brutal way, time limit exceed.
int combine(int N)
{
    int res = 0;
    int sum = N * (1 + N) / 2;
    if (sum % 2 != 0)
        res = 0; // no way
    else sum /= 2;
    int setsum = 0;
    for (long combine = 1; combine < (1L << N); combine++)
    {
        for (int cur = 0; cur < N; cur++)
            if ((combine & (1 << cur)) > 0)
                setsum += (cur + 1);  // cur == N_i
        if (setsum == sum) res++;
        if (setsum == sum) {
            for (int cur = 0; cur < N; cur++)
                if ((combine & (1 << cur)) > 0)
                    cout << (cur + 1) << " ";  // cur == N_i
            cout << endl;
        }
        setsum = 0;
    }
    return res/2;
}

ulong sumup(int N) {
    ulong s = N * (N + 1);
    if ((s & 0b11) > 0) return 0;
    ulong s2 = s / 4;

    vector<ulong> dp(s2 + 1, 0);
    dp[0] = 1;

    for (int i = 1; i <= N; i++)
    {
        ulong s2i = i * (i+1) / 2;
        s2i = s2i > s2 ? s2 : s2i;
        for (int j = s2i; j >= i; j--)
        {
            dp[j] += dp[j-i];
        }
    }

    return dp[s2];
}

int main()
{
    int N;
    ifstream fin;
    fin.open("subset.in");
    fin >> N;
    fin.close();

    // N = 39; // 1512776590
    // N = 31; // 8273610
    // N = 8;  // 7
    ulong res = sumup(N);
    // ulong res = combine(N);

    ofstream cout;
    cout.open("subset.out");
    cout << res / 2 << endl;
    cout.close();

    return 0;
}
