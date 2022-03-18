#!/usr/bin/python
import os 
import sys 


joinPath = os.path.join


def getSourceHeader(path):
    hFiles = []
    cppFiles = []
    for i in os.listdir(path):
        if "." not in i:
            continue
        if i.split(".")[1] == "h":
            hFiles.append(joinPath(path, i))
        elif i.split(".")[1] == "cpp":
            if i != "main.cpp":
                cppFiles.append(joinPath(path, i))
    return hFiles, cppFiles


def getFileList(path):
    absPath = os.path.abspath(path)
    print("The path you entered is {}".format(absPath))
    ddePath = joinPath(absPath, "utils")
    hFiles, cppFiles = getSourceHeader(ddePath)
    return ddePath, hFiles, cppFiles


def writePri(ddePath, hFiles, cppFiles):
    with open("src.pri", "w") as f:
        f.write("INCLUDEPATH += \\\n")
        f.write("\t{}\n".format(ddePath))
        f.write("SOURCES += \\\n")
        for i in cppFiles:
            f.write("\t{}\\\n".format(i))
        f.write("\n\nHEADERS += \\\n")
        for i in hFiles:
            f.write("\t{}\\\n".format(i))


def main():
    if len(sys.argv) < 2:
        print("Please enter the path where the dde-device-formatter project is located.")
        return 1
    if len(sys.argv) > 2:
        print("Has extra parameters.")
        return 1
    ddePath, hFiles, cppFiles = getFileList(sys.argv[1])
    writePri(ddePath, hFiles, cppFiles)
    return 0


if __name__ == "__main__":
    main()