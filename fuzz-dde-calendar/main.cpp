
#include <QString>
#include <QDebug>
#include <QByteArray>
#include "utils.h"
#include <QJsonDocument>
#include <QJsonArray>
#include "xfuzz.h"

//自定义转换函数，输入是任意数量的支持的类型（包括其他自定义类型）
QString to_qstring(std::string &s) {
  return QString(s.c_str());
}

XFUZZ_CUSTOM_CONVERTER(to_qstring);

void test(QString &s) {
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
}

XFUZZ_TEST_ENTRYPOINT(test);





