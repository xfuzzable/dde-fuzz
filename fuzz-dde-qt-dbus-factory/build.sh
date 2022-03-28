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

python3 createTestCode.py $@

for loop in 1 2 3
do
    if [ ! -f ./main.cpp ]
    then 
        echo "wait create main.cpp file."
        echo "sleep 1s."
        sleep 1
    fi
done

if [ ! -f ./main.cpp ]
then 
    echo "main.cpp not exist."
    echo "exit."
    exit 1
fi

mkdir -p build
cd build
qmake ..

make CC=xfuzz-cc CXX=xfuzz-c++ LINK=xfuzz-c++ VERBOSE=1 -j