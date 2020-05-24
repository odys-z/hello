#include <QDebug>
#include "q024.h"
#include "ui_q024.h"

Q024::Q024(QWidget *parent)
    : QMainWindow(parent) , ui(new Ui::Q024)
{
    ui->setupUi(this);
    connect(ui->plainLeft, SIGNAL(textChanged()), this, SLOT(on_LeftChanged()));
}

Q024::~Q024()
{
    delete ui;
}


void Q024::on_LeftChanged()
{
    QString s = ui->plainLeft->toPlainText();
    qInfo() << s;
    ui->editRight->setText(s);
    QTextCursor tmpCursor = ui->plainLeft->textCursor();
    tmpCursor.movePosition(QTextCursor::Left, QTextCursor::MoveAnchor, 4);
    ui->plainLeft->setTextCursor(tmpCursor);
}
