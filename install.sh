#!/bin/bash

apps=(dde-calendar
    dde-clipboard
    dde-control-center
    dde-device-formatter
    dde-dock
    dde-file-manager
    dde-file-manager-integration
    dde-introduction
    dde-kwin
    dde-launcher
    dde-network-utils
    dde-polkit-agent
    dde-printer
    dde-qt-dbus-factory
    dde-session-shell
    dde-session-ui
    dde-wayland
)

function install_all(){
    for app in ${apps[*]};
    do 
        echo "install $app"
        apt source $app -y
        apt build-dep $app -y
    done
}

if test ${#@} == 0
then
    echo "Please enter one or more app names."
    echo "The app names that can be entered are as follows"
    for app in ${apps[*]};
    do
        echo "$app"
    done
    read -p "Whether to install all?[y/n]" yn
    case $yn in
    [Yy]* ) echo "install all"; install_all;;
    [Nn]* ) echo "exit"; exit;;
    * ) echo "Please answer y or n.";;
    esac
fi

if [ $# != 0 ]
then
    for app in "$@";
    do
        echo "install $app"
        apt source $app -y 
        apt build-dep $app -y 
    done
fi




