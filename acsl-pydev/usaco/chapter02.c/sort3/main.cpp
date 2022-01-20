/*
ID: odys.zh1
LANG: C++
TASK: sort3
 */
#include <iostream>
#include <fstream>

using namespace std;


int countpq( int counts[], int len, int seq[])
{
    int count = 0;
    int medals[] = {1, 2, 3};
    for (int medal : medals) {
        int right = counts[medal];
        int x = counts[medal - 1];
        while (x < right)
        {
            if (medal != seq[x])
            {
                bool found = false;
                // try medal area
                for (int y = counts[seq[x] - 1]; y < len; y++)
                {
                    if (seq[y] == medal) {
                        seq[y] = seq[x];
                        seq[x] = medal; right = y;
                        count++;

//                        cout << x << " '" << y << " ";
//                        for (int c = 0; c < len; c++)
//                            cout << seq[c] << ' ' ;
//                        cout << endl;


                        found = true;
                        break;
                    }
                }
                if (!found)
                {
                    for (int y = right; y < len; y++)
                    {
                         if (seq[y] == medal) {
                            seq[y] = seq[x];
                            seq[x] = medal; right = y;
                            count++;

//                            cout << x << " '" << y << " ";
//                            for (int c = 0; c < len; c++)
//                                cout << seq[c] << ' ' ;
//                            cout << endl;


                            found = true;
                            break;
                         }
                    }
                }
            }
            x++;
        }
    }

    return count;
}

int main()
{

//   int len = 9;
//   int seq[] = {2, 2, 1, 3, 3, 3, 2, 3, 1};
//   //           1  1  2  2  2  3  3  3  3
//   //              1  2  3 -start
//   //                 1  2  3 -end
//   int counts[] = {0, 2, 5, 9};

     int len;
     ifstream fin;
     fin.open("sort3.in");
     fin >> len;
     int seq[len];
     int counts[] = {0, 0, 0, 0};
     for (int i = 0; i < len; i++) {
         fin >> seq[i];
         counts[seq[i]] += 1;
     }
     fin.close();

     for (int i = 1; i < 4; i++) {
         counts[i] = counts[i - 1] + counts[i];
     }

    ////////////////////////////////////////
        cout << "      ";
        for (int c = 0; c < len; c++)
            cout << seq[c] << ' ' ;
        cout << endl;

    int c = countpq(counts, len, seq);
    ofstream fout;
    fout.open("sort3.out");
    fout << c << endl;
    fout.close();

    return 0;
}
