#ifndef Q797_H
#define Q797_H

#include <vector>
#include <iostream>

using namespace std;

/**
 * Runtime Error at LeetCode
=================================================================
==31==ERROR: AddressSanitizer: heap-use-after-free on address 0x6080000000d0 at pc 0x000000347b56 bp 0x7fff98a6b6f0 sp 0x7fff98a6b6e8
READ of size 8 at 0x6080000000d0 thread T0
    #4 0x7f6a375950b2  (/lib/x86_64-linux-gnu/libc.so.6+0x270b2)
0x6080000000d0 is located 48 bytes inside of 96-byte region [0x6080000000a0,0x608000000100)
freed by thread T0 here:
    #6 0x7f6a375950b2  (/lib/x86_64-linux-gnu/libc.so.6+0x270b2)
previously allocated by thread T0 here:
    #5 0x7f6a375950b2  (/lib/x86_64-linux-gnu/libc.so.6+0x270b2)
Shadow bytes around the buggy address:
  0x0c107fff7fc0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c107fff7fd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c107fff7fe0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c107fff7ff0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c107fff8000: fa fa fa fa 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c107fff8010: fa fa fa fa fd fd fd fd fd fd[fd]fd fd fd fd fd
  0x0c107fff8020: fa fa fa fa 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c107fff8030: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c107fff8040: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c107fff8050: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c107fff8060: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
  Shadow gap:              cc
==31==ABORTING
 * @brief The Q797 class
 */
class Q797 {
    vector<vector<vector<int>>> dfs(vector<vector<vector<int>>> &dp, vector<vector<int>> &graph) {
        int lastx = graph.size() - 1;

        for (int x = lastx - 1; 0 <= x; x--) {
            vector<vector<int>> *pathx = new vector<vector<int>>{};
            vector<int> &nxtNodes = graph[x];
            for (unsigned nxt = 0; nxt < nxtNodes.size(); nxt++) {
                int nxtNode = nxtNodes[nxt];
                if (nxtNode < 0) continue;  // unresolved path flag

                vector<vector<int>> &nxtPaths = dp[nxtNode];
                if (nxtPaths.size() == 0) {
                    // flag resolving path, then find it first
                    nxtNodes[nxt] = -1;

                    cout << "x: " << x << endl << "[";
                    for (vector<int> v : graph) for(int i : v) cout << i << " ";
                    cout << "]" << endl;

                    dp = dfs(dp, graph);
                    nxtNodes[nxt] = nxtNode;
                }

                for (vector<int> path : nxtPaths) {
                    vector<int> p = vector<int>(path);
                    p.insert(p.begin(), x);
                    pathx->push_back(p);
                }
            }
            dp[x] = *pathx;
        }
        return dp;
    }

public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {

        vector<vector<vector<int>>> dp(graph.size(), vector<vector<int>>{});

        int lastx = graph.size() - 1;
        dp[lastx] = vector<vector<int>>{};
        dp[lastx].push_back(vector<int>{lastx});

        dp = dfs(dp, graph);
        return dp[0];
    }
};

#endif // Q797_H
