#ifndef SEMANTIER_H
#define SEMANTIER_H

#include <qdebug.h>
#include <qobject.h>
#include <QVariantMap>

class Semantier : public QObject
{
    Q_OBJECT

public:
    Semantier();
public slots:
    void slt_postPing(const QVariant &qvar) {
        qDebug() << "............";
        QVariantMap anson = qvar.toMap();
        qDebug() << "[CPP.slt_postPing] At C++ slot with message:\n"
                 << "jserv: " << anson["jserv"].toString() << "\n"
                 << "timestamp: " << anson["timestamp"].toString();
    }
};

#endif // SEMANTIER_H
