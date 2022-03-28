#!/usr/bin/python
import os 
import sys 


insertCode = "\n#ifndef FUZZ\n"

appendCode = """
#else

#include <vector>
#include <string>
#include "xfuzz.h"

void testDbus(std::vector<std::string> vec)
{
    int argc = vec.size();
    QStringList arguments;
    arguments.reserve(argc + 1);
    arguments.append("./qdbusxml2cpp-fix");
    for (int i = 0; i < argc; ++i) {
        arguments.append(QString::fromLocal8Bit(vec[i].c_str()));
    }

    parseCmdLine(arguments);

    QDBusIntrospection::Interfaces interfaces = readInput();
    cleanInterfaces(interfaces);

    if (!proxyFile.isEmpty() || adaptorFile.isEmpty())
        writeProxy(proxyFile, interfaces);

    if (!adaptorFile.isEmpty())
        writeAdaptor(adaptorFile, interfaces);

    return;
}

XFUZZ_TEST_ENTRYPOINT(testDbus);

#endif
"""


filepath = os.path.abspath(__file__)


def writeCode(lines):
    with open(os.path.join(os.path.dirname(filepath), "main.cpp"), "w") as f:
        f.writelines(lines)


def readCode(codeFilename):
    with open(codeFilename, "r") as f:
        lines = f.readlines()
        mainLine = 0
        for index, value in enumerate(lines):
            if "main" in value and "int" in value and "char" in value:
                mainLine = index
                break
        lines.insert(mainLine-1, insertCode)
        lines.append(appendCode)
        return lines 


def main():
    if len(sys.argv) < 2:
        print("Please enter the path where the dde-qt-dbus-factory project is located.")
        return 1
    if len(sys.argv) > 2:
        print("Has extra parameters.")
        return 1
    absPath = os.path.abspath(sys.argv[1])
    codeFilename = os.path.join(absPath, "tools/qdbusxml2cpp/qdbusxml2cpp.cpp")
    lines = readCode(codeFilename)
    writeCode(lines)
    return 0


if __name__ == "__main__":
    main()