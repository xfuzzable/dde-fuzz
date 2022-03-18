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
    dde-session
    dde-session-ui
    dde-session-shell
    dde-wayland
)

if [ $# == 0 ]
then
    for app in ${apps[*]};
    do 
        echo "install $app"
        apt source $app -y
        apt build-dep $app -y
    done
else
    for app in "$@";
    do
        echo "install $app"
        apt source $app -y 
        apt build-dep $app -y 
    done
fi




