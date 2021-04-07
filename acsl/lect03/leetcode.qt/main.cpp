#include <q1404.h>
#include <QtTest>

int testQ1404_ACSL()
{
    Q1404_ACSL_Easy* s = new Q1404_ACSL_Easy();
    int ok = 0;

    assert(0 == s->numSteps("1"));
    ok++;

    assert(6 == s->numSteps("1101"));
    ok++;

    assert(1 == s->numSteps("10"));
    ok++;

    assert(5 == s->numSteps("1111"));
    ok++;

    return ok;
}

int testQ1404()
{
    Q1404* s;
    int ok = 0;

    s = new Q1404();
    assert(0 == s->numSteps("1"));
    ok++;

    assert(6 == s->numSteps("1101"));
    ok++;

    assert(1 == s->numSteps("10"));
    ok++;

    assert(5 == s->numSteps("1111"));
    ok++;

    assert(9 == s->numSteps("11111111"));
    ok++;

    assert(9 == s->numSteps("011111111"));
    ok++;

    assert(19 == s->numSteps("011111111011111111"));
    ok++;

    assert(201 == s->numSteps("11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"));
    ok++;

    return ok;
}

int main()
{
    // return testQ1404_ACSL();
    return testQ1404();
}
