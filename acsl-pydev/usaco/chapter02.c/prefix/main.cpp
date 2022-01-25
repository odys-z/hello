/**
ID: odys.zh1
LANG: C++
TASK: prefix
 */
#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

/* Test 1: TEST OK [0.007 secs, 1348 KB]
   Test 2: TEST OK [0.007 secs, 1344 KB]
   Test 3: TEST OK [0.011 secs, 1360 KB]
   Test 4: TEST OK [0.014 secs, 1376 KB]
   Test 5: TEST OK [0.014 secs, 1356 KB]
   Test 6: TEST OK [0.126 secs, 3452 KB]
 */

int multilineToken(ifstream & fin, vector<string> & tokens, char delimiter, string endingline)
{
    string t;
    int cnt = 0;
    while(getline(fin, t))
    {
        istringstream inss(t);
        string w;
        while(getline(inss, w, delimiter))
        {
            if (w == endingline)
                return cnt;
            tokens.push_back(w);
            cnt++;
        }
    }
    return cnt;
}

int match(vector<string> & prefix, string sequence)
{
    vector<bool> flags(sequence.size(), false);
    flags[0] = true;
    ulong far = 0;
    for (ulong i = 0; i < sequence.length(); i++)
        if (flags[i])
            for (string fix : prefix)
                if ( sequence.compare(i, fix.length(), fix) == 0 )
                {
                    ulong l = fix.length();
                    flags[i + l] = true;
                    far = far > i + l ? far : i + l;
                }
    return far;
}

int main()
{
    ifstream fin;
    fin.open("prefix.in");

    vector<string> tokens;
    multilineToken(fin, tokens, ' ', ".");

    string sequence;
    string lin;
    while(getline(fin, lin))
        sequence += lin;

    int l = match(tokens, sequence);

//    for (string s : tokens)
//        cout << "[" << s << "]" << endl;
//    cout << endl << sequence << endl;

    ofstream cout;
    cout.open("prefix.out");
    cout << l << endl;
    cout.close();

    return 0;
}
