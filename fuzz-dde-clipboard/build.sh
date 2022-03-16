#!/bin/bash
echo "Project Paht is $@"
echo "$PWD"
h="/"
projectPath=$PWD$h$@
echo "Project Paht is $projectPath"
cp $projectPath/dde-clipboard/main.cpp  $projectPath/dde-clipboard/main.cpp.back
cp $PWD/main.cpp $projectPath/dde-clipboard
mkdir -p build
cd build
qmake $projectPath
make CC=xfuzz-cc CXX=xfuzz-c++ LINK=xfuzz-c++ V=1 -j
cp $projectPath/dde-clipboard/main.cpp.back $projectPath/dde-clipboard/main.cpp  
rm -f $projectPath/dde-clipboard/main.cpp.back