TARGET = dde-introduction-xfuzz
TEMPLATE = app
QT = core gui widgets dbus multimedia multimediawidgets
CONFIG += link_pkgconfig c++11
QT += dtkwidget
PKGCONFIG += dframeworkdbus libdmr gsettings-qt

QMAKE_CXXFLAGS+= -fPIE
QMAKE_LFLAGS += -pie

include(projectPath.pri)
message("Project path " $$ABSPATH)

HEADERS += \
    $$ABSPATH/src/widgets/bottombutton.h 

SOURCES += \
    main.cpp \
    $$ABSPATH/src/widgets/bottombutton.cpp 

INCLUDEPATH += $$ABSPATH/src/widgets/
