
#include <DApplication>
#include "chameleontheme.h"
#include "xfuzz.h"


QT_USE_NAMESPACE

QApplication *app;

QString to_qstring(std::string &s) {
    return QString(s.c_str());
}

XFUZZ_CUSTOM_CONVERTER(to_qstring);

void test_init(){
    qputenv("QT_QPA_PLATFORM", "offscreen");
    static char* argv[] = {"./dde-kwin-xfuzz", nullptr};
    int argc = 1;
    app = new QApplication(argc,argv);
}

void testChameleonTheme(const QString &text) {
    ChameleonTheme *ct  = ChameleonTheme::instance();
    ct->setTheme(text);
    ct->theme();
    ct->themeConfig();
}

XFUZZ_TEST_ENTRYPOINT_WITH_INIT(
    testChameleonTheme, 
    test_init
);