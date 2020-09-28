#include <solution.h>
#include <QtTest>

int main()
{
    int ok = 0;
    Solution* s = new Solution();
    vector<int> r = {12,345,2,6,7896};
    assert(2 == s->findNumbers(r));
    ok++;

    r = {12};
    assert(1 == s->findNumbers(r));
    ok++;

    r = {0};
    assert(0 == s->findNumbers(r));
    ok++;

    r = {1};
    assert(0 == s->findNumbers(r));
    ok++;

    r = {10, 11};
    assert(2 == s->findNumbers(r));
    ok++;

    r = {100, 111, 110};
    assert(0 == s->findNumbers(r));
    ok++;

    r = {1000, 1111, 1110, 1010, 1000, 1100};
    assert(6 == s->findNumbers(r));
    ok++;

    r = {10000};
    r = {10000};
    assert(0 == s->findNumbers(r));
    ok++;

    r = {555,901,482,1771};
    assert(1 == s->findNumbers(r));
    ok++;

    r = {1,1,101,100,01,11,13,100000};
    assert(3 == s->findNumbers(r));
    ok++;

    return ok;
}
