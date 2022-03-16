
#!/bin/bash

for i in "$@";
do
    echo "install $i"
    apt source $i
    apt build-dep $i
done


