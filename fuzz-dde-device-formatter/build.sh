#!/bin/bash
echo "Project Paht is $@"
python3 getPath.py $@
mkdir -p build
cd build
qmake ..
make CC=xfuzz-cc CXX=xfuzz-c++ LINK=xfuzz-c++ V=1 -j