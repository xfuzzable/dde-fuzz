#include <DApplication>
#include <QDebug>

DCORE_USE_NAMESPACE
DWIDGET_USE_NAMESPACE

#include "bottombutton.h"
#include "xfuzz.h"

QApplication *app;

QString to_qstring(std::string &s) {
    return QString(s.c_str());
}

XFUZZ_CUSTOM_CONVERTER(to_qstring);

void test_init(){
    qputenv("QT_QPA_PLATFORM", "offscreen");
    static char* argv[] = {"./dde-introduction-xfuzz", nullptr};
    int argc = 1;
    app = new QApplication(argc,argv);
}



void testBottomButton(QString &text, int x, int y, int width, int height) {
    BottomButton *button = new BottomButton();
    button->setText(text);
    QRect rect(x, y, width, height);
    button->setRect(rect);
    delete button;
}


XFUZZ_TEST_ENTRYPOINT_WITH_INIT(
    testBottomButton, 
    test_init
);