
#include <QString>
#include <QDebug>
#include <QByteArray>
#include "utils.h"
#include <QJsonDocument>
#include <QJsonArray>



extern "C" void xfuzz_test_one(char *Data, size_t DataSize) {
    if (DataSize == 0){
        return;
    }
    //qInfo() << Data;
    QByteArray qba = QByteArray(Data, DataSize);
    QString s(qba);

// int main(int argc, char* argv[]){
//     if (argc > 2){
//         return 0;
//     }
//     QString s(argv[1]);
    qInfo() << s;
    Utils * ut = new Utils();
    auto qdt = ut->fromconvertData(s);
    qInfo() << qdt;
    auto qs = ut->toconvertData(qdt);
    qInfo() << qs;
    auto qdt1 = ut->fromconvertiIGData(s);
    qInfo() << qdt1;
    auto qs1 = ut->toconvertData(qdt1);
    qInfo() << qs;
    delete ut;

    //return 0;
}


