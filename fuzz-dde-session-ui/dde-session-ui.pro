#-------------------------------------------------
#
# Project created by QtCreator 2017-01-03T16:41:12
#
#-------------------------------------------------

QT       += core gui dtkwidget

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = dde-session-ui-xfuzz
TEMPLATE = app
CONFIG += link_pkgconfig c++11
PKGCONFIG += dframeworkdbus gsettings-qt

# The following define makes your compiler emit warnings if you use
# any feature of Qt which as been marked as deprecated (the exact warnings
# depend on your compiler). Please consult the documentation of the
# deprecated API in order to know how to port your code away from it.
DEFINES += QT_DEPRECATED_WARNINGS

# You can also make your code fail to compile if you use deprecated APIs.
# In order to do so, uncomment the following line.
# You can also select to disable deprecated APIs only up to a certain version of Qt.
DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0
include(projectPath.pri)

INCLUDEPATH += \
	$$ABSPATH

SOURCES += main.cpp\
    $$ABSPATH/pincodedialog.cpp 

HEADERS  +=\
    $$ABSPATH/pincodedialog.h \
    $$ABSPATH/largelabel.h \
    

icons.path = /usr/share/icons/hicolor/scalable/devices

target.path = /usr/lib/deepin-daemon/
INSTALLS += target icons
