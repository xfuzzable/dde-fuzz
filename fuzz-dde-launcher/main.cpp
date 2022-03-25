

#include <DApplication>
#include <QString>
#include <QDebug>
#include "roundedbutton.h"
#include "xfuzz.h"

QApplication *app;

QString to_qstring(std::string &s) {
    return QString(s.c_str());
}

XFUZZ_CUSTOM_CONVERTER(to_qstring);

void test_init(){
    qputenv("QT_QPA_PLATFORM", "offscreen");
    static char* argv[] = {"./dde-launcher-xfuzz", nullptr};
    int argc = 1;
    app = new QApplication(argc,argv);
}

void testRoundedButton(QString &s) {
    RoundedButton button;
    button.setText(s);
}



XFUZZ_TEST_ENTRYPOINT_WITH_INIT(
    testRoundedButton, 
    test_init
);