QT       += core gui dbus gui-private x11extras
greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = dde-kwin-xfuzz
TEMPLATE = app
CONFIG += c++11 link_pkgconfig
PKGCONFIG += dtkwidget dtkgui gio-qt dframeworkdbus


QMAKE_CXXFLAGS += -fPIC

include(projectPath.pri)

INCLUDEPATH += \
	$$ABSPATH/plugins/kdecoration/
    
HEADERS += \
    $$ABSPATH/plugins/kdecoration/chameleontheme.h

SOURCES += \
    main.cpp \
    $$ABSPATH/plugins/kdecoration/chameleontheme.cpp


INSTALLS += TARGET