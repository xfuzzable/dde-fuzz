#-------------------------------------------------
#
# Project created by QtCreator 2016-12-07T09:33:51
#
#-------------------------------------------------

QT       += core gui concurrent network x11extras dbus

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = dde-device-formatter-xfuzz
TEMPLATE = app

PKGCONFIG += x11 udisks2-qt5 dtkwidget dtkgui

CONFIG += c++11 link_pkgconfig

QMAKE_CXXFLAGS += -fPIC
include(src.pri)
SOURCES += \
        $$PWD/main.cpp

PREFIX = ./install 
BINDIR = $$PREFIX/bin
SHAREDIR = $$PREFIX/share/$${TARGET}
DESKTOPFILEDIR = $$PREFIX/share/applications

target.path = $$BINDIR

INSTALLS += target 
