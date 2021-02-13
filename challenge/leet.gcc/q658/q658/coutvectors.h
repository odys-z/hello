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
        // return this;
    }
};

#endif // COUTVECTORS_H
