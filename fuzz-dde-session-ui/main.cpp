
#include "pincodedialog.h"
#include <DApplication>
#include <QDebug>
#include <QTranslator>
#include "xfuzz.h"

DWIDGET_USE_NAMESPACE
DCORE_USE_NAMESPACE

QApplication *app;

QString to_qstring(std::string &s) {
    return QString(s.c_str());
}

XFUZZ_CUSTOM_CONVERTER(to_qstring);

extern "C" void test_init(){
    qputenv("QT_QPA_PLATFORM", "offscreen");
    static char* argv[] = {"./dde-file-manager-xfuzz", nullptr};
    int argc = 1;
    app = new QApplication(argc,argv);
    app->setOrganizationName("deepin");
    app->setApplicationName("dde-bluetooth-dialog");
    QTranslator translator;
    translator.load("/usr/share/dde-session-ui/translations/dde-session-ui_" + QLocale::system().name());
    app->installTranslator(&translator);
}

void testPinCodeDialog(QString &pinCode,  QString &devicepath, QString &starttime,  bool cancelable) {
    PinCodeDialog dialog(pinCode, devicepath, starttime, cancelable);
}

XFUZZ_TEST_ENTRYPOINT_WITH_INIT(
    testPinCodeDialog, 
    test_init
);