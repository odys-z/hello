QT += testlib
QT -= gui

CONFIG += qt console warn_on depend_includepath testcase
CONFIG -= app_bundle

TEMPLATE = app

SOURCES +=  \
    main.cpp \
    tst_q024.cpp

HEADERS += \
    tst_q024.h

INCLUDEPATH += \
    ../../q024 \
    ../../../util/Singlist

LIBS += -L"../../../util/build" -lSinglist
