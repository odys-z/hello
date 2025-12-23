#ifndef SEMANTIER_H
#define SEMANTIER_H

#include <qdebug.h>
#include <qobject.h>

class Semantier : public QObject
{
    Q_OBJECT

public:
    Semantier();
public slots:
    void slt_postPing(const QString &msg) {
        qDebug() << "............";
        qDebug() << "[CPP.slt_postPing] At C++ slot with message:" << msg;
    }
};

#endif // SEMANTIER_H
