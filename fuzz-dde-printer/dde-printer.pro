QT       -= core gui network dbus
greaterThan(QT_MAJOR_VERSION, 4): QT += widgets
CONFIG += c++11 link_pkgconfig
TARGET = dde-printer-xfuzz
TEMPLATE = app

DEFINES += CPPCUPS_LIBRARY
DEFINES += QT_DEPRECATED_WARNINGS QT_MESSAGELOGCONTEXT
PKGCONFIG += dtkwidget dtkgui

QMAKE_CFLAGS += -Wall -Wextra -Wformat=2 -Wno-format-nonliteral -Wshadow -fPIE -Wl,--as-needed,-O1
QMAKE_CXXFLAGS += -Wall -Wextra -Wformat=2 -Wno-format-nonliteral -Wshadow -fPIE -Wl,--as-needed,-O1
QMAKE_LFLAGS += -pie

LIBS += -lcups

include(projectPath.pri)

INCLUDEPATH += \
	$$ABSPATH/src/cppcups/

HEADERS += \
    $$ABSPATH/src/cppcups/cupsconnection.h \
    $$ABSPATH/src/cppcups/cppcups_global.h\
    $$ABSPATH/src/cppcups/cupsipp.h \
    $$ABSPATH/src/cppcups/cupsmodule.h\
    $$ABSPATH/src/cppcups/cupsppd.h \
    $$ABSPATH/src/cppcups/cupssnmp.h \
    $$ABSPATH/src/cppcups/snmp.h \
    $$ABSPATH/src/cppcups/types.h \
    $$ABSPATH/src/cppcups/mibpath.h


SOURCES += \
    $$ABSPATH/src/cppcups/cupsconnection.cc\
    $$ABSPATH/src/cppcups/cupsipp.cc\
    $$ABSPATH/src/cppcups/cupsmodule.cc\
    $$ABSPATH/src/cppcups/cupsppd.cc \
    $$ABSPATH/src/cppcups/cupssnmp.cpp \
    $$ABSPATH/src/cppcups/snmp.c\
    main.cpp


#DESTDIR += $$PWD

