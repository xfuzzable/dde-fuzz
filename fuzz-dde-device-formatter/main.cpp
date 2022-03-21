


#include <DApplication>
#include "udisksutils.h"
#include "fsutils.h"
#include <ddiskmanager.h>

#include <QString>
#include <QDebug>

QApplication *app;

extern "C" void xfuzz_before_test(){
    qputenv("QT_QPA_PLATFORM", "offscreen");
    static char* argv[] = {"./dde-device-formatter-xfuzz", nullptr};
    int argc = 1;
    app = new QApplication(argc,argv);
}

extern "C" void xfuzz_test_one(char *Data, size_t DataSize) {
    if (DataSize == 0){
        return;
    }
    const QByteArray databuf = QByteArray(Data, DataSize);
    const QString s1(databuf);
    int x = FsUtils::maxLabelLength(s1);
    qDebug() << "x -> " << x;
}
