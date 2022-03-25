#include <QPixmap>
#include <QDebug>
#include <QApplication>
#include <QString>
#include "themeappicon.h"
#include "xfuzz.h"

QApplication *app;

void test_init(){
    qputenv("QT_QPA_PLATFORM", "offscreen");
    static char* argv[] = {"./dde-dock-xfuzz", nullptr};
    int argc = 1;
    app = new QApplication(argc,argv);
}

void testThemeAppIcon(char *Data, size_t DataSize, bool reObtain) {
    if (DataSize == 0){
        return;
    }
    const QByteArray databuf = QByteArray(Data, DataSize);
    const QString iconName(databuf);
    QPixmap pix;
    auto result = ThemeAppIcon::getIcon(pix, iconName, reObtain);
    qInfo() << result;
}


XFUZZ_TEST_ENTRYPOINT_WITH_INIT(
    testThemeAppIcon, 
    test_init
);




