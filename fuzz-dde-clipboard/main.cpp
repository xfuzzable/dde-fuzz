#include "itemdata.h"
#include <stddef.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <string>
#include <stdlib.h>
#include <DApplication>

QApplication *app;

extern "C" void xfuzz_before_test(){
    qputenv("QT_QPA_PLATFORM", "offscreen");
    static char* argv[] = {"./dde-clipboard", nullptr};
    int argc = 1;
    app = new QApplication(argc,argv);
}

extern "C" void xfuzz_test_one(char *Data, size_t DataSize) {
    const QByteArray databuf = QByteArray(Data, DataSize);
    ItemData *data = new ItemData(databuf);
    if (data->type() == Unknown) {
        delete data;
        return;
    }
    delete data;
}
