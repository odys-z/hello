#ifndef Q024_H
#define Q024_H

#include <QMainWindow>

#include "singlist.h"

QT_BEGIN_NAMESPACE
namespace Ui { class Q024; }
QT_END_NAMESPACE

class Q024 : public QMainWindow
{
    Q_OBJECT

    QString parseCases(QString);

public:
    Q024(QWidget *parent = nullptr);
    ~Q024();

private slots:
    void on_LeftChanged();
    void onNew();

private:
    Ui::Q024 *ui;
};
#endif // Q024_H
