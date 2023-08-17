/**
ID: odys.zh1
LANG: C++
TASK: money
 */
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

// [k, v], k = coins count
vector<vector<long long>> dp;

/** dp({1..Ck}, v) = dp({1..Ck}, v - Ck) + dp({1..Ck-1}, v)
 * is the rephrasing of nway(n, k) = nway(n, k-1) + nway(n-c_k, k),
 * by Russ Cox, https://jvonk.github.io/usaco/2018/10/18/money.html
 *
 * According to addition pricipal, to count ways to get v with coins 1, 2, ..., Ck,
 * is equals ways with Ck at least once and ways without Ck.
 *
    dp({1, 2, ..., Ck}, v)
  = dp({1, 2, ..., Ck}, v - Ck) + dp({1, 2, ..., Ck-1}, v)


    dp({1, 2, ..., Ck}, v)
  = dp({1, 2, ..., Ck}, v - Ck - Ck-1) + dp({1, 2, ..., Ck-2}, v)

  dp({*}, -1) = 0
  dp({*}, 0) = 1
  dp({1}, v) = 1
  dp({1, 2}, v) = dp({1, 2}, v-2} + dp({1}, v)

  dp({1, 2, 5}, 7) = dp({1, 2, 5}, 7-5}                     + dp({1, 2}, 7)
                   = dp({1, 2, 5}, 7-5-2} + dp({1}, 7-5)    + dp({1, 2}, 7-2)                           + dp({1}, 7)
                   = 1                    + 1               + dp({1, 2}, 5-2) + dp({1}, 5)              + dp({1}, 7)
                   = 1                    + 1               + dp({1, 2}, 3-2) + dp({1}, 3) + dp({1}, 5) + dp({1}, 7)
                   = 1                    + 1               + 1               + 1          + 1          + 1
                   = 6
 with c5
 7 = 2 + 5,     dp({1, 2, 5}, 7-5-2)
   = 1 + 1 + 5, dp({1}, 7-5)

 without c5
 7 = 1 + 1 + 1 + 1 + 1 + 1 + 1,  dp({1}, 7)
   = 1 + 1 + 1 + 1 + 1 + 2,      dp({1}, 5)
   = 1 + 1 + 1 + 2 + 2,          dp({1}, 3)
   = 1 + 2 + 2 + 2,              dp({1,2}, 1)

 * @brief match
 * @param coins
 * @param V
 * @return
 */
long long match(vector<long long> coins, int V)
{
    int sx = coins.size();
    if (sx <= 0) return 0;

    if (V < 0) return 0;        // dp({*} -1) = 0
    else if (V == 0) return 1;
    else if (V < coins[0]) return 0;  // dp({*} 1) = 1
    else if (dp[sx][V] >= 0) return dp[sx][V];

    long long ways = 0;

    ways = match(coins, V - coins.back());
    coins.pop_back();
    ways += match(coins, V);
    dp[sx][V] = ways;
//    if (ways != 0)
//        cout << sx << ":" << V << "\t" << ways << endl;
    return ways;
}

int main()
{
    ifstream fin;
    fin.open("money.in");

    int C, V;
    fin >> C >> V ;

    vector<long long> coins;
    int c;
    for (int i = 0; i < C; i++)
    {
        fin >> c;
        coins.push_back(c);
    }

    // dp[coins[0]] = 1; // coins sorted ?
    dp = vector<vector<long long>>(C + 1, vector<long long>(V+1, -1));
    for (int c = 0; c <= C; c++)
        dp[c][0] = 1;

    sort(coins.begin(), coins.end());
    long long l = match(coins, V);

    ofstream cout;
    cout.open("money.out");
    cout << l << endl;
    cout.close();

    return 0;
}
