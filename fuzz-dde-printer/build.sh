#!/bin/bash
echo "Project Paht is $@"

if [ ! -d $@ ]
then 
    echo "target path not exist."
    exit 1
fi

python3 createPri.py $@

for loop in 1 2 3
do
    if [ ! -f ./projectPath.pri ]
    then 
        echo "wait pri file."
        echo "sleep 1s."
        sleep 1
    fi
done

if [ ! -f ./projectPath.pri ]
then 
    exit 1
fi

mkdir -p build
cd build
qmake ..

make CC=xfuzz-cc CXX=xfuzz-c++ LINK=xfuzz-c++ VERBOSE=1 -j