#include <q1404.h>
#include <QtTest>

int main()
{
    int ok = 0;
    Q1404* s = new Q1404();
    assert(13 == s->numSteps("1101"));
    ok++;

    return ok;
}
