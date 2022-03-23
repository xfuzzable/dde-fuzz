QT       += dbus network

TARGET = dde-network-xfuzz
TEMPLATE = app

PKGCONFIG += dframeworkdbus gsettings-qt
CONFIG += c++11 link_pkgconfig
CONFIG -= app_bundle

DEFINES += QT_DEPRECATED_WARNINGS
include(projectPath.pri)
message("Project path " $$ABSPATH)
include($$ABSPATH/dde-network-utils/src.pri)
INCLUDEPATH += $$ABSPATH/dde-network-utils/

SOURCES += \
    main.cpp 




