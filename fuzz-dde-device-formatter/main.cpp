


#include <DApplication>
#include "udisksutils.h"
#include "fsutils.h"
#include <ddiskmanager.h>

#include <QString>
#include <QDebug>
#include "xfuzz.h"

QApplication *app;


QString to_qstring(std::string &s) {
    return QString(s.c_str());
}

XFUZZ_CUSTOM_CONVERTER(to_qstring);

void test_init(){
    qputenv("QT_QPA_PLATFORM", "offscreen");
    static char* argv[] = {"./dde-device-formatter", nullptr};
    int argc = 1;
    app = new QApplication(argc,argv);
}

void testFsUtils(QString &s) {
    int x = FsUtils::maxLabelLength(s);
    qDebug() << "x -> " << x;
}

XFUZZ_TEST_ENTRYPOINT_WITH_INIT(
    testFsUtils, 
    test_init
);