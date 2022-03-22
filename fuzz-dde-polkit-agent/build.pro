
TARGET = dde-polkit-agent-xfuzz
TEMPLATE = app
QT += core gui widgets dbus concurrent
CONFIG += link_pkgconfig c++11
PKGCONFIG += polkit-qt5-1 dframeworkdbus gsettings-qt dtkwidget
load(dtk_qmake)
QMAKE_CXXFLAGS += -fPIC
include($$PWD/src.pri)
message($$PWD/src.pri)
message($$DISTFILES)

SOURCES += \
        $$PWD/main.cpp


target.path = /usr/lib/polkit-1-dde

headers.path = /usr/include/dpa
headers.files = agent-extension-proxy.h agent-extension.h

INSTALLS += target qm_files headers

