#ifndef Q024_H
#define Q024_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class Q024; }
QT_END_NAMESPACE

class Q024 : public QMainWindow
{
    Q_OBJECT

public:
    Q024(QWidget *parent = nullptr);
    ~Q024();

private slots:
    void on_LeftChanged();

private:
    Ui::Q024 *ui;
};
#endif // Q024_H
