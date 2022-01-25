/*
ID: odys.zh1
LANG: C++
TASK: lamps
 */
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <bitset>
#include <algorithm>

using namespace std;

/*
 * Tests shows that if C >= 3, all touched states are the same,
 * a little bit different from Russ Cox's analys.
 *
 * https://jvonk.github.io/usaco/2018/10/13/lamps.html
 *
 * Possible states:
    000000 001001
    010101 011100
    100011 101010
    110110 111111
  * It's obvious since button 1 & and button 2 can arrived at
  * 00, 01, 10, 11
  * And button 3 makes the first different for every 3 bits.
    x 0 0 x 0 0
    x 1 0 x 0 1
    x 0 1 x 1 0
    x 1 1 x 1 1
  *
  * So all possible states can be reached within 3 steps.
  *
   Test 1: TEST OK [0.004 secs, 1368 KB]
   Test 2: TEST OK [0.004 secs, 1408 KB]
   Test 3: TEST OK [0.004 secs, 1424 KB]
   Test 4: TEST OK [0.004 secs, 1356 KB]
   Test 5: TEST OK [0.007 secs, 1360 KB]
   Test 6: TEST OK [0.007 secs, 1408 KB]
   Test 7: TEST OK [0.004 secs, 1352 KB]
   Test 8: TEST OK [0.004 secs, 1364 KB]
 */

// low - hight significent
int buttons[4] = {0b111111, 0b101010, 0b010101, 0b100100};

set<int> touchs;


void dfs(int c, int current)
{
    if (c > 0)
        for (int b : buttons)
            dfs(c-1, current ^ b);
    else
        touchs.insert(current);
}

vector<string> lamps(int c, int current, int ons, int offs)
{
    vector<string> lines;
    dfs(c, current);

    for (int line : touchs)
        if ((line & ons) == ons and (line & offs) == 0)
        {
            bitset<6> v(line);
            string s = v.to_string();
            // reverse(s.begin(), s.end());
            lines.push_back(s);
        }
    sort(lines.begin(), lines.end());
    return lines;
}

void output(ostream & os, int N, string line)
{

    for (int repeat = 0; repeat < (N / 6); repeat += 1)
    {
        os << line;
    }

    if (N % 6 > 0)
        os << line.substr(0, N % 6) << endl;
}

void printGraph(int c, int s0) {
    dfs(c, s0);
    for (int s : touchs)
        cout << bitset<6>(s) << endl;
}

int main()
{
    int N, C, lamp;
    int ons = 0;
    int offs = 0;
    ifstream fin;
    fin.open("lamps.in");
    fin >> N >> C >> lamp;

    while (lamp >= 0)
    {
        ons |= 0b100000 >> ((lamp - 1) % 6);
        fin >> lamp;
    }

    fin >> lamp;
    while (lamp >= 0)
    {
        offs |= 0b100000 >> ((lamp - 1) % 6);
        fin >> lamp;
    }
    fin.close();

//    printGraph(1, 0b111111);
//    cout << endl;
//    touchs.clear();
//    printGraph(2, 0b111111);
//    cout << endl;
//    touchs.clear();
//    printGraph(3, 0b111111);
//    cout << endl;
//    touchs.clear();
    vector<string> lines = lamps(C > 3 ? 3 : C, 0b111111, ons, offs);

    ofstream cout;
    cout.open("lamps.out");

    if (lines.size() > 0)
        for (string line : lines)
            output(cout, N, line);
    else cout << "IMPOSSIBLE" << endl;
    cout.close();

    return 0;
}
