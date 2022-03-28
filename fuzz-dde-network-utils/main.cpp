#include "networkmodel.h"
#include "xfuzz.h"
using namespace dde::network;

QString to_qstring(std::string &s) {
    return QString(s.c_str());
}

XFUZZ_CUSTOM_CONVERTER(to_qstring);

void testNetworkModel(QString &s1, QString &s2, QString &s3, QString &s4, QString &s5, QString &s6, QString &s7, QString &s8, QString &s9, QString &s10, QString &s11, QString &s12) {
    NetworkModel *nm = new NetworkModel();
    nm->proxy(s1);
    nm->connectionByUuid(s2);
    nm->activeConnObjectByUuid(s3);
    nm->autoProxyChanged(s4);
    nm->proxyMethodChanged(s5);
    nm->proxyIgnoreHostsChanged(s6);
    nm->requestDeviceStatus(s7);
    nm->chainsTypeChanged(s8);
    nm->chainsAddrChanged(s9);
    nm->chainsUsernameChanged(s10);
    nm->chainsPasswdChanged(s11);
    nm->needSecrets(s12);
    delete nm;
}

XFUZZ_TEST_ENTRYPOINT(testNetworkModel);