

#include <DApplication>
#include <QString>
#include <QDebug>
#include "roundedbutton.h"



QApplication *app;

extern "C" void xfuzz_before_test(){
    qputenv("QT_QPA_PLATFORM", "offscreen");
    static char* argv[] = {"./dde-launcher-xfuzz", nullptr};
    int argc = 1;
    app = new QApplication(argc,argv);
}

extern "C" void xfuzz_test_one(char *Data, size_t DataSize) {
    QByteArray databuf = QByteArray(Data, DataSize);
    const QString s1(databuf);
    RoundedButton button;
    button.setText(s1);
}
