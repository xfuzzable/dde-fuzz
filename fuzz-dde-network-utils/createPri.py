#!/usr/bin/python
import os 
import sys 

filepath = os.path.abspath(__file__)

def writePri(other):
    with open(os.path.join(os.path.dirname(filepath), "projectPath.pri"), "w") as f:
        for k in other.keys():
            f.write("{}={}\n".format(k, other[k]))

def main():
    if len(sys.argv) < 2:
        print("Please enter the path where the dde-file-manager project is located.")
        return 1
    if len(sys.argv) > 2:
        print("Has extra parameters.")
        return 1
    absPath = os.path.abspath(sys.argv[1])
    other = {"ABSPATH": absPath}
    writePri(other)
    return 0


if __name__ == "__main__":
    main()