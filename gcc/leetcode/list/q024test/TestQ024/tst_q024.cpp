#include <QtTest>

#include "tst_q024.h"


q024::~q024()
{  }

q024::q024()
{
    this->q24 = new q024();
}

void q024::test_case1()
{
    QFAIL("... ###### ------------");
}

//QTEST_APPLESS_MAIN(q024)

// #include "tst_q024.moc"
