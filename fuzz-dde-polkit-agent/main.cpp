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

QApplication *app;

extern "C" void xfuzz_before_test(){
    qputenv("QT_QPA_PLATFORM", "offscreen");
    static char* argv[] = {"./dde-polkit-agent-xfuzz", nullptr};
    int argc = 1;
    app = new QApplication(argc,argv);
}

extern "C" void xfuzz_test_one(char *Data, size_t DataSize) {
    if (DataSize == 0) {return;}
    const QByteArray databuf = QByteArray(Data, DataSize);
    const QString message(databuf);
    qDebug() << message;
    ErrorTooltip *data = new ErrorTooltip(message, nullptr);
    data->setMessage(message);
    qDebug() << data->text();
    delete data;
}
