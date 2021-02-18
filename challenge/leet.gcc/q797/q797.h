#ifndef Q797_H
#define Q797_H

#include <vector>
using namespace std;

class Q797 {
    vector<vector<vector<int>>> dfs(vector<vector<vector<int>>> &dp, vector<vector<int>> graph) {
        int lastx = graph.size() - 1;

        for (int x = lastx - 1; 0 <= x; x--) {
            vector<vector<int>> pathx;
            vector<int> nxtNodes = graph[x];
            for (unsigned nxt = 0; nxt < nxtNodes.size(); nxt++) {
                int nxtNode = nxtNodes[nxt];
                if (nxtNode < 0) continue;  // unresolved path flag

                vector<vector<int>> nxtPaths = dp[nxtNode];
                if (nxtPaths.size() > 0) {
                    for (vector<int> path : nxtPaths) {
                        vector<int> p = vector<int>(path);
                        p.insert(p.begin(), x);
                        pathx.push_back(p);
                    }
                }
                else {
                    // flag resolving path, then find it first
                    nxtNodes[nxt] = -1;
                    dp = dfs(dp, graph);
                    nxtNodes[nxt] = nxtNode;
                }
            }
            dp[x] = pathx;
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
