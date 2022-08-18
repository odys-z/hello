/*
ID: odys.zh1
LANG: C++
TASK: ttwo
 */
#include <iostream>
#include <fstream>
#include <vector>
#include <assert.h>
#include <set>
#include <string>

//#define DEBUGttwo

using namespace std;

/**
   Test 1: TEST OK [0.007 secs, 1344 KB]
   Test 2: TEST OK [0.007 secs, 1344 KB]
   Test 3: TEST OK [0.004 secs, 1360 KB]
   Test 4: TEST OK [0.004 secs, 1344 KB]
   Test 5: TEST OK [0.007 secs, 1340 KB]
   Test 6: TEST OK [0.004 secs, 1332 KB]
   Test 7: TEST OK [0.004 secs, 1356 KB]
   Test 8: TEST OK [0.004 secs, 1336 KB]
   Test 9: TEST OK [0.004 secs, 1376 KB]
 * @brief The Farmer class
 */
class Farmer
{
    vector<int> dir = {0, -1};
    vector<int> xy = {-1, -1};
    vector<vector<char>> &map;

public:
    Farmer(vector<vector<char>> &map) : map(map) { }

    Farmer(vector<vector<char>> &map, int x0, int y0) : map(map)
    {
        this->dir = {0, -1}; // north, +y = down
        this->xy = {x0, y0};
    }

    // 2 ^ 7 = 128, 7 + 7 + 2 = 16, 16 + 16 = 32
    long long foot()
    {
        return ((long long)this->xy[0] * 128 * 4 + this->xy[1]) * 4 + this->dir[0] * 2 + this->dir[1];
    }

    void go(int x, int y)
    {
        this->xy = {x, y};
        this->dir = {0, -1};
    }

    long long move()
    {
        int x1 = this->xy[0] + this->dir[0];
        int y1 = this->xy[1] + this->dir[1];
        if (x1 < 0 or y1 < 0 or x1 >= 10 or y1 >= 10)
             turn90();
        else if (x1 < 0 or y1 < 0 or x1 >= 10 or y1 >= 10)
             turn90();
        else if (map[x1][y1] == '*')
             turn90();
        else
            this->xy = {x1, y1};

         return foot();
    }

    void turn90()
    {
        // [ 1, 0 ] -> [ 0, 1 ]
        // [ 0, 1 ] -> [-1, 0 ]
        // [-1, 0 ] -> [ 0,-1 ]
        // [ 0,-1 ] -> [ 1, 0 ]
        int dx = dir[0], dy = dir[1];
        if (dx == 1 and dy == 0)
            dir = { 0, 1 };
        else if (dx == 0 and dy == 1)
            dir = { -1, 0 };
        else if (dx == -1 and dy == 0)
            dir = { 0, -1 };
        else if (dx == 0 and dy == -1)
            dir = { 1, 0 };
    }

    bool met(Farmer with)
    {
        return this->xy[0] == with.xy[0] and this->xy[1] == with.xy[1];
    }

#ifdef DEBUGttwo
    void print()
    {
        cout << xy[1] << " : " << xy[0] << " " << ((dir[1] == -1) ? "^" : (dir[1] == 1) ? "_" : (dir[0] == 1) ? ">" : "<");
    }
#endif
};

int trek(Farmer john, Farmer cow)
{
    set<long long> footprint;
    int minutes = 0;
    long long step = 0;
    while(footprint.find(step) == footprint.end())
    {
        if (john.met(cow))
            return minutes;
        footprint.insert(step);
        step = john.move() * 128 * 4 * 128 * 4+ cow.move();
        minutes++;
#ifdef DEBUGttwo
        cout << minutes << "\t"; john.print(); cout << "    "; cow.print(); cout << endl;
        cout << hex << "\t" << step / 128 * 128 * 4 * 4 << "  " << step % 128 * 128 * 4 * 4 << endl;
#endif
    }
    return 0;
}

int main()
{
    ifstream fin;
    fin.open("ttwo.in");

    vector<vector<char>> pasture(10, vector<char>(10, '.'));
    Farmer fj(pasture);
    Farmer cow(pasture);

    for (int y = 0; y < 10; y++)
    for (int x = 0; x < 10; x++)
    {
        fin >> pasture[x][y];
        if (pasture[x][y] == 'F')
        {
            fj.go(x, y);
        }
        else if (pasture[x][y] == 'C')
        {
            cow.go(x, y);
        }
    }
    fin.close();

    ofstream cout;
    cout.open("ttwo.out");
    cout << trek(fj, cow) << endl;

    return 0;
}
