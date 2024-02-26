
#include "utils.h"

string reducev(vector<int> const & v) {
    return v.size() == 0 ? "" : reduce(next(v.begin()), v.end(), string("[") + to_string(v[0]), [](string a, int b) { return move(a) + "," + to_string(b); }) + string("]");
}

string reducev(vector<vector<int>> const & v) {
    return v.size() == 0 ? "" : reduce(next(v.begin()), v.end(), string("[") + (v[0].size() > 0 ? reducev(v[0]) : ""), [](string a, vector<int> b) { return b.size() > 0 ? move(a) + ",\n" + reducev(b) : move(a); }) + string("]");
}
