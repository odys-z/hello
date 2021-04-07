#include <QCoreApplication>
#include <QTextStream>

int main(int argc, char *argv[])
{
    // QCoreApplication a(argc, argv);
    // return a.exec();
    int c = 0;
    while (c < argc) {
        QTextStream(stdout) << argv[c] << endl;
        c++;
    }
    return 0;
}
