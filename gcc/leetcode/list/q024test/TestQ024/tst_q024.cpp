#include <QtTest>

#include "tst_q024.h"


Q024test::~Q024test()
{  }

Q024test::Q024test()
{
    this->s = new Solution();
}

void Q024test::test_case()
{
    QFAIL("... ###### ------------");
}

//QTEST_APPLESS_MAIN(q024)

// #include "tst_q024.moc"
