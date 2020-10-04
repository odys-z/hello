#ifndef Q1404_H
#define Q1404_H

#include <string>
#include <iostream>

using namespace std;

class Q1404
{
public:
    Q1404();
    int numSteps(string s) {
        int v = std::stoi(s, nullptr, 2);
        cout << v << endl;
        return v;
    }
};

#endif // Q1404_H
