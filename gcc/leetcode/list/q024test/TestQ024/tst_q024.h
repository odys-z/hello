#include <QtTest>

#include "solution.h"

// add necessary includes here

class Q024test : public QObject
{
    Q_OBJECT

    Solution* s;

public:
    Q024test();
    ~Q024test();

    void test_case();

};
