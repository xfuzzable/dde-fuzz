#!/bin/bash
if test ${#@} == 0
then
    echo "Please input a project path."
    echo "exit."
    exit 1
else
    echo "Project Paht is $@."
fi

if [ ! -d $@ ]
then 
    echo "target path not exist."
    echo "exit."
    exit 1
fi

python3 getPath.py $@

for loop in 1 2 3
do
    if [ ! -f ./projectPath.pri ]
    then 
        echo "wait projectPath.pri ..."
        echo "sleep 1s."
        sleep 1
    fi
done

if [ ! -f ./projectPath.pri ]
then 
    echo "projectPath.pri not exist."
    echo "exit."
    exit 1
fi

mkdir -p build
cd build
qmake ..
make CC=xfuzz-cc CXX=xfuzz-c++ LINK=xfuzz-c++ VERBOSE=1 -j