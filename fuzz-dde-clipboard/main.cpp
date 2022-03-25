#include "itemdata.h"
#include <stddef.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <string>
#include <stdlib.h>
#include <DApplication>
#include "xfuzz.h"

QApplication *app;

void test_init(){
    qputenv("QT_QPA_PLATFORM", "offscreen");
    static char* argv[] = {"./dde-clipboard", nullptr};
    int argc = 1;
    app = new QApplication(argc,argv);
}

void testItemData(char *Data, size_t DataSize) {
    const QByteArray databuf = QByteArray(Data, DataSize);
    ItemData *data = new ItemData(databuf);
    if (data->type() == Unknown) {
        delete data;
        return;
    }
    delete data;
}

XFUZZ_TEST_ENTRYPOINT_WITH_INIT(
    testItemData, 
    test_init
);