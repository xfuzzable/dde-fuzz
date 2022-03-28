#include "cupsmodule.h"
#include "xfuzz.h"

void testCupsmodule(char *str, char *str2, char *user, char *server, int port, int e, int level) {
    cups_modelSort(str, str2);
    cups_setUser(user);
    cups_setServer(server);
    cups_setPort(port);
    cups_setEncryption(e);
    cups_getUser();
    cups_getServer();
    cups_getPort();
    cups_getEncryption();
    cups_ppdSetConformance(level);
}

XFUZZ_TEST_ENTRYPOINT(testCupsmodule);