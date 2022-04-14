TARGET = dde-qt-dbus-factory-xfuzz

TEMPLATE = app
QT += core dbus-private

SOURCES += qdbusxml2cpp.cpp

DEFINES += FUZZ=1

#DESTDIR = $$PWD/../../bin/

CONFIG += c++11

load(dtk_qmake)

host_sw_64 {
    QMAKE_CXXFLAGS += -mieee
}
