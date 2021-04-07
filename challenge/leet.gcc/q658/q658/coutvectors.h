#ifndef COUTVECTORS_H
#define COUTVECTORS_H

#include <vector>
#include <iostream>
#include <iterator>

using namespace std;

class CoutVectors
{
public:
    CoutVectors();

    static void ints(vector<int> vec) {
        vector<char> str;
        for(int a : vec) {
            str.insert(str.end(), a + 0x30);
        }
        cout << "[";
        std::copy(str.begin(), str.end(), std::ostream_iterator<char>(std::cout, ", "));
        cout << "]";
    }

    static void ints(vector<vector<int>> vvec) {
        cout << "[";
        for (vector<int> vec : vvec) {
            ints(vec);
            cout << " ";
        }
        cout << "]" << endl;
    }


    static void strs(vector<string> vec) {
        cout << "[";
        for(string s : vec) {
            cout << "'" << s << "', ";
        }
        cout << "]";

    }
};

#endif // COUTVECTORS_H
