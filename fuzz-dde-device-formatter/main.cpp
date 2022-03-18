


#include <DApplication>
#include "udisksutils.h"
#include "fsutils.h"
#include <QString>
#include <iostream>

QApplication *app;

extern "C" void xfuzz_before_test(){
    qputenv("QT_QPA_PLATFORM", "offscreen");
    static char* argv[] = {"./dde-device-formatter", nullptr};
    int argc = 1;
    app = new QApplication(argc,argv);
}

extern "C" void xfuzz_test_one(char *Data, size_t DataSize) {
    if (DataSize == 0){
        return;
    }
    const QByteArray databuf = QByteArray(Data, DataSize);
    const QString s1(databuf);
    UDisksBlock *data = new UDisksBlock(s1);
    std::cout << "Type -> " << data->fsType().toStdString() << std::endl;
    std::cout << "Total -> " << data->sizeTotal() << std::endl;
    std::cout << "Used -> " << data->sizeUsed() << std::endl;
    delete data;
}

