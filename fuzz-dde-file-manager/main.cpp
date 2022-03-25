
#include "dfileiodeviceproxy.h"
#include <DApplication>
#include <QString>
#include <QDebug>

using namespace DFM_NAMESPACE;

#include "xfuzz.h"

QApplication *app;

extern "C" void test_init(){
    qputenv("QT_QPA_PLATFORM", "offscreen");
    static char* argv[] = {"./dde-file-manager-xfuzz", nullptr};
    int argc = 1;
    app = new QApplication(argc,argv);
}

void testDFileIODeviceProxy(char *Data, size_t DataSize) {
    if (DataSize == 0){
        return;
    }
    DFileIODeviceProxy *device = new DFileIODeviceProxy();
    device->open(QIODevice::ReadWrite | QIODevice::Truncate);
    device->write(Data,DataSize);
    device->read(Data,DataSize);
    delete device;
}

XFUZZ_TEST_ENTRYPOINT_WITH_INIT(
    testDFileIODeviceProxy, 
    test_init
);