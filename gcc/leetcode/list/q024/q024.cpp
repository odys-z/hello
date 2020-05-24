#include <QDebug>
#include <QJsonDocument>
#include <QJsonObject>
#include <QJsonValue>
#include <QJsonArray>

#include "q024.h"
#include "ui_q024.h"

Q024::Q024(QWidget *parent)
    : QMainWindow(parent) , ui(new Ui::Q024)
{
    ui->setupUi(this);
    connect(ui->plainRev, SIGNAL(textChanged()), this, SLOT(on_LeftChanged()));
    connect(ui->actNew, SIGNAL(triggered()), this, SLOT(onNew()));
}

Q024::~Q024()
{
    delete ui;
}


void Q024::on_LeftChanged()
{
    QString s = ui->plainRev->toPlainText();
    qInfo() << s;
    ui->editRight->setText(s);
    QTextCursor tmpCursor = ui->plainRev->textCursor();
    tmpCursor.movePosition(QTextCursor::Left, QTextCursor::MoveAnchor, 4);
    ui->plainRev->setTextCursor(tmpCursor);
}

void Q024::onNew()
{
    QFile f;
    f.setFileName(":/default.json");
    f.open(QIODevice::ReadOnly | QIODevice::Text);
    QString val;
    val = f.readAll();
    f.close();
//    ui->plainUp->setPlainText(val.toUtf8());
//    QJsonDocument d = QJsonDocument::fromJson(val.toUtf8());
    QString cse = parseCases(val);
    qInfo() << cse;
    ui->plainUp->setPlainText( cse );
}

QString Q024::parseCases(QString json) {
    QJsonDocument d = QJsonDocument::fromJson(json.toUtf8());
    QJsonObject j = d.object();
    QJsonArray cases = j.value(QString("cases")).toArray();
    qInfo() << cases;

    QString s = "";
    for (int i = 0; i < cases.size(); ++i) {
        QJsonObject e = cases[i].toObject();
        QJsonValue k = e.value("case");
        QJsonArray v = e.value("input").toArray();
        s += k.toString() + ": [ ";

        int j = 0;
        for (; j < v.size() - 1; ++j) {
            s += QString("%1, ").arg(v[j].toInt());
        }
        if (j < v.size())
            s += QString("%1 ").arg(v[j].toInt());
        s += "]\n";
    }
    return s;
}

