#include "semantier.h"
#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QQmlContext>
#include <QDir>

int main(int argc, char *argv[])
{
    QGuiApplication app(argc, argv);

    QQmlApplicationEngine engine;
    QObject::connect(
        &engine,
        &QQmlApplicationEngine::objectCreationFailed,
        &app,
        []() { QCoreApplication::exit(-1); },
        Qt::QueuedConnection);

    Semantier myClass;
    QObject::connect(&engine, &QQmlApplicationEngine::objectCreated,
                     &app, [&myClass](QObject *obj, const QUrl &objUrl) {
                         if (!obj) {
                             // Loading failed (check console for QML errors)
                             QCoreApplication::exit(-1);
                         } else {
                             // Successfully loaded: connect your signal now
                             QObject::connect(obj, SIGNAL(sig_postPing(QString)),
                                              &myClass, SLOT(slt_postPing(QString)));
                             qDebug() << "sig_postPing connected ...";
                         }
                     }, Qt::QueuedConnection);

    engine.rootContext()->setContextProperty("currentWorkingDirectory", QDir::currentPath());
    engine.rootContext()->setContextProperty("applicationBinaryDirectory", app.applicationDirPath());

    engine.loadFromModule("qtquiclient", "Main");

    // won't work - engine's root object is not ready
    // QObject *win = engine.rootObjects().at(0);

    // Semantier myClass;
    // QObject::connect(win, SIGNAL(sig_postPing(QString)),
    //                  &myClass, SLOT(slt_postPing(QString)));

    return app.exec();
}
