#ifndef Q684_H
#define Q684_H

#include <vector>
#include <stdlib.h>

using namespace std;

class Dsu {
    vector<int> parent;
    vector<int> rank;

public:
    Dsu (int N) {
        parent = vector<int>(N + 1);
        rank = vector<int>(N + 1);
        for (int i = 0; i < N + 1; i++) {
            parent[i] = i;
            rank[i] = 0;
        }
    }

    int getU(int x) {
        while (parent[x] != x)
            x = parent[x];
        return x;
    }

    bool connect(int x, int y) {
        x = getU(x);
        y = getU(y);
        if (x == y) return false;

        if (rank[x] < rank[y]) {
            parent[x] = y;
            rank[y] += 1;
        }
        else{
            parent[y] = x;
            rank[x] += 1;
        }
        return true;
    }
};

class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        Dsu dsu(edges.size());
        for (vector<int> e : edges) {
            if (!dsu.connect(e[0], e[1]))
                return e;
        }
        return vector<int>();
    }
};

#endif // Q684_H
