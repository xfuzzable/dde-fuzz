#!/bin/bash
echo "Project Paht is $@."
if [ ! -d $@ ]
then 
    echo "target path not exist."
    exit 1
fi
python3 createCmake.py $@
for loop in 1 2 3
do
    if [ ! -f ./CMakeLists.txt ]
    then 
        echo "wait cmakefile."
        echo "sleep 1s."
        sleep 1
    fi
done
mkdir -p build
cd build
cmake .. -DCMAKE_C_COMPILER=xfuzz-cc -DCMAKE_CXX_COMPILER=xfuzz-c++ -DCMAKE_CXX_COMPILER_ID=Clang -DCMAKE_CXX_COMPILER_VERSION=12.0.0 -DCMAKE_CXX_STANDARD_COMPUTED_DEFAULT=14
make VERBOSE=1 -j