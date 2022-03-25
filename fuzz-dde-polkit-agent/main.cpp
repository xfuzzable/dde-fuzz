#include <DApplication>
#include <DLog>

#include <PolkitQt1/Subject>

#include "policykitlistener.h"
#include "accessible.h"

#include <QDebug>
#include <QDir>
#include <QFile>
#include <QStandardPaths>

DWIDGET_USE_NAMESPACE
DCORE_USE_NAMESPACE

//xfuzz main 
#include "errortooltip.h"
#include "xfuzz.h"

QApplication *app;

QString to_qstring(std::string &s) {
    return QString(s.c_str());
}

XFUZZ_CUSTOM_CONVERTER(to_qstring);

void test_init(){
    qputenv("QT_QPA_PLATFORM", "offscreen");
    static char* argv[] = {"./dde-polkit-agent-xfuzz", nullptr};
    int argc = 1;
    app = new QApplication(argc,argv);
}

void testErrorTooltip(QString &tooltipStr, QString &message) {
    qDebug() << message;
    ErrorTooltip *data = new ErrorTooltip(tooltipStr, nullptr);
    data->setMessage(message);
    qDebug() << data->text();
    delete data;
}


XFUZZ_TEST_ENTRYPOINT_WITH_INIT(
    testErrorTooltip, 
    test_init
);