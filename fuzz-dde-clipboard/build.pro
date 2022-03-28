#-------------------------------------------------
#
# Project created by QtCreator 2019-11-01T13:38:32
#
#-------------------------------------------------

QT       += core gui dbus gui-private
greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = dde-clipboard
TEMPLATE = app
CONFIG += c++11 link_pkgconfig
PKGCONFIG += dtkwidget dtkgui gio-qt dframeworkdbus


QMAKE_CXXFLAGS += -fPIC

include(src.pri)

message($$PWD/main.cpp)
SOURCES += \
        $$PWD/main.cpp


INSTALLS += TARGET
