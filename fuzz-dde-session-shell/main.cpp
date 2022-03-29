#include "accessibilitycheckerex.h"
#include "appeventfilter.h"
#include "dbuslockagent.h"
#include "dbuslockfrontservice.h"
#include "dbusshutdownagent.h"
#include "dbusshutdownfrontservice.h"
#include "lockcontent.h"
#include "lockframe.h"
#include "lockworker.h"
#include "modules_loader.h"
#include "multiscreenmanager.h"
#include "propertygroup.h"
#include "sessionbasemodel.h"

#include <DApplication>
#include <DGuiApplicationHelper>
#include <DLog>
#include <DPlatformTheme>

#include <QDBusInterface>

#include <unistd.h>

#include "deepinauthframework.h"
#include "xfuzz.h"
#include <vector>
DCORE_USE_NAMESPACE
DWIDGET_USE_NAMESPACE

DApplication *app = nullptr;

QString to_qstring(std::string &s) {
    return QString(s.c_str());
}

XFUZZ_CUSTOM_CONVERTER(to_qstring);

void test_init(){
    qputenv("QT_QPA_PLATFORM", "offscreen");
    static char* argv[] = {"./dde-session-shell-xfuzz", nullptr};
    int argc = 1;
    #if (DTK_VERSION < DTK_VERSION_CHECK(5, 4, 0, 0))
        app = new DApplication(argc, argv);
    #else
        app = DApplication::globalApplication(argc, argv);
    #endif
}

void testDeepinAuthFramework(QString &account, QString &token, int flag, QString &path, int type, std::vector<int> method) {
    ArrayInt arrayMethod;
    for(int i : method){
        arrayMethod.append(i);
    }
    DeepinAuthFramework * auth = new DeepinAuthFramework;
    auth->CreateAuthenticate(account);
    auth->SendToken(token);
    auth->DestoryAuthenticate();
    auth->GetFrameworkState();
    auth->GetSupportedMixAuthFlags();
    auth->GetPreOneKeyLogin(flag);
    auth->GetLimitedInfo(account);
    auth->GetSupportedEncrypts();
    auth->GetFuzzyMFA(account);
    auth->GetMFAFlag(account);
    auth->GetPINLen(account);
    auth->GetFactorsInfo(account);
    auth->GetPrompt(account);
    auth->SetPrivilegesEnable(account, path);
    auth->SetPrivilegesDisable(account);
    auth->AuthSessionPath(account);
    auth->setEncryption(type, arrayMethod);
    auth->authSessionExist(account);
    auth->isDeepinAuthValid() ;
}


XFUZZ_TEST_ENTRYPOINT_WITH_INIT(
    testDeepinAuthFramework, 
    test_init
);