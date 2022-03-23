#include "networkmodel.h"

using namespace dde::network;

extern "C" void xfuzz_test_one(char *Data, size_t DataSize) {
    NetworkModel *nm = new NetworkModel();
    QByteArray databuf = QByteArray(Data, DataSize);
    const QString s(databuf);
    nm->proxy(s);
    nm->connectionUuidByPath(s);
    nm->connectionNameByPath(s);
    nm->connectionByUuid(s);
    nm->connectionByPath(s);
    nm->activeConnObjectByUuid(s);
    nm->autoProxyChanged(s);
    nm->proxyMethodChanged(s);
    nm->proxyIgnoreHostsChanged(s);
    nm->requestDeviceStatus(s);
    nm->chainsTypeChanged(s);
    nm->chainsAddrChanged(s);
    nm->chainsUsernameChanged(s);
    nm->chainsPasswdChanged(s);
    nm->needSecrets(s);
    delete nm;
}