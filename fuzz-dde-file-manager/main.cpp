
#include "dfileiodeviceproxy.h"
#include <DApplication>
#include <QString>
#include <QDebug>

using namespace DFM_NAMESPACE;

QApplication *app;

extern "C" void xfuzz_before_test(){
    qputenv("QT_QPA_PLATFORM", "offscreen");
    static char* argv[] = {"./dde-file-manager-xfuzz", nullptr};
    int argc = 1;
    app = new QApplication(argc,argv);
}

extern "C" void xfuzz_test_one(char *Data, size_t DataSize) {
    if (DataSize == 0){
        return;
    }
    DFileIODeviceProxy *device = new DFileIODeviceProxy();
    device->open(QIODevice::ReadWrite | QIODevice::Truncate);
    device->waitForReadyRead(1);
    device->waitForBytesWritten(1);
    device->write(Data,DataSize);
    device->bytesToWrite();
    device->bytesAvailable();
    device->seek(0);
    device->read(Data,DataSize);
    device->atEnd();
    device->reset();
    device->bytesToWrite();
    device->bytesAvailable();
    delete device;
}
