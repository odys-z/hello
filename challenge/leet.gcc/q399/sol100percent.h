#ifndef SOL100PERCENT_H
#define SOL100PERCENT_H

#endif // SOL100PERCENT_H

#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <set>

/**
 * 100.00% 0ms, 55.39% 4ms
 *
 * @brief The Solution class
 */
class Variable100 {
public:
    map<string, double> mulwith;
    string name;
    double val; // my value for returned as sub graph's evaluated
    bool visited;

    /**For declaring before finding when initializing
     * https://stackoverflow.com/a/13570219/7362888
     * @brief Variable
     */
    Variable100() : name(""), val(1.0), visited(false) {}

    Variable100(string name) : name(name), val(1.0), visited(false)
    { }

    void addEdge(string n, double v)
    {
        if (n != name)
            mulwith.insert(pair<string, double>(n, v));
    }
};

