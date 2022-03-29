#!/usr/bin/python
import os 
import sys 

cmakeLists = """
cmake_minimum_required(VERSION 3.13.4)
project(dde-session-shell C CXX)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}  -g -Wall -pthread -Wl,--as-need -fPIE -Wl,-E")
SET(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS} -O0 -ggdb")
SET(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS} -O3")
set(CMAKE_MODULE_PATH PROJECT_SOURCE_DIR/cmake/modules)

# 增加安全编译参数
set(SECURITY_COMPILE, "-fstack-protector-strong -D_FORTITY_SOURCE=1 -z noexecstack -pie -fPIC -z lazy")
set(CMAKE_CXX_FLAGS, "${CMAKE_CXX_FLAGS} ${SECURITY_COMPILE}")
set(CMAKE_C_FLAGS, "${CMAKE_C_FLAGS} ${SECURITY_COMPILE}")

# coverage option
# cmake -DENABLE_COVERAGE=ON ..
OPTION (ENABLE_COVERAGE "Use gcov" OFF)
MESSAGE(STATUS ENABLE_COVERAGE=${ENABLE_COVERAGE})
if (ENABLE_COVERAGE)
    SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fprofile-arcs -ftest-coverage")
    SET(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fprofile-arcs -ftest-coverage")
    #SET(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -fprofile-arcs -ftest-coverage")
endif()

if (${CMAKE_SYSTEM_PROCESSOR} MATCHES "mips64")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3 -ftree-vectorize -march=loongson3a -mhard-float -mno-micromips -mno-mips16 -flax-vector-conversions -mloongson-ext2 -mloongson-mmi")
endif()

set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -pie")

# if (NOT (${CMAKE_BUILD_TYPE} MATCHES "Debug"))
#     set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Ofast")

#     # generate qm
#     execute_process(COMMAND bash "translate_generation.sh"
#                     WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})
# endif ()

# Find the library
find_package(PAM REQUIRED)
find_package(PkgConfig REQUIRED)
find_package(DtkWidget REQUIRED)
find_package(DtkCMake  REQUIRED)
find_package(DtkCore REQUIRED)
find_package(Qt5 COMPONENTS
    Core
    Widgets
    Concurrent
    X11Extras
    DBus
    Xml
    Svg
    Network
REQUIRED)

pkg_check_modules(XCB_EWMH REQUIRED xcb-ewmh x11 xi xcursor xfixes xrandr xext xtst)
pkg_check_modules(DFrameworkDBus REQUIRED dframeworkdbus)
pkg_check_modules(QGSettings REQUIRED gsettings-qt)
pkg_check_modules(Greeter REQUIRED liblightdm-qt5-3)

set(Qt_LIBS
    Qt5::Core
    Qt5::Gui
    Qt5::DBus
    Qt5::Widgets
    Qt5::X11Extras
    Qt5::Xml
    Qt5::Svg
)

function(generation_dbus_interface xml class_name class_file option)
    execute_process(COMMAND qdbusxml2cpp ${option} -p ${class_file} -c ${class_name} ${xml}
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR})
endfunction(generation_dbus_interface)

generation_dbus_interface(
    PROJECT_SOURCE_DIR/xml/com.deepin.daemon.Authenticate.xml
    AuthenticateInterface
    ${CMAKE_CURRENT_BINARY_DIR}/authenticate_interface
    -N
)

set(authority_DBUS_SCRS
    ${CMAKE_CURRENT_BINARY_DIR}/authenticate_interface.h
    ${CMAKE_CURRENT_BINARY_DIR}/authenticate_interface.cpp
)

generation_dbus_interface(
    PROJECT_SOURCE_DIR/xml/com.huawei.switchos.xml
    HuaWeiSwitchOSInterface
    ${CMAKE_CURRENT_BINARY_DIR}/switchos_interface
    -N
)

set(haweiswitchos_DBUS_SCRS
    ${CMAKE_CURRENT_BINARY_DIR}/switchos_interface.h
    ${CMAKE_CURRENT_BINARY_DIR}/switchos_interface.cpp
)

include_directories(PROJECT_SOURCE_DIR/src/global_util)
include_directories(PROJECT_SOURCE_DIR/src/global_util/dbus)
include_directories(PROJECT_SOURCE_DIR/src/global_util/keyboardmonitor)
include_directories(PROJECT_SOURCE_DIR/src/widgets)
include_directories(PROJECT_SOURCE_DIR/src/session-widgets)
include_directories(PROJECT_SOURCE_DIR/src/libdde-auth)
include_directories(PROJECT_SOURCE_DIR/interface)

aux_source_directory(PROJECT_SOURCE_DIR/src/global_util GLOBAL_UTILS)
aux_source_directory(PROJECT_SOURCE_DIR/src/global_util/dbus GLOBAL_UTILS_DBUS)
aux_source_directory(PROJECT_SOURCE_DIR/src/global_util/keyboardmonitor GLOBAL_UTILS_KEYBOARDMONITOR)
aux_source_directory(PROJECT_SOURCE_DIR/src/widgets WIDGETS)
aux_source_directory(PROJECT_SOURCE_DIR/src/session-widgets SESSION_WIDGETS)
aux_source_directory(PROJECT_SOURCE_DIR/src/libdde-auth AUTHENTICATE)
aux_source_directory(PROJECT_SOURCE_DIR/interface INTERFACE)

set(QRCS
    PROJECT_SOURCE_DIR/resources.qrc
    PROJECT_SOURCE_DIR/src/widgets/widgetsimages.qrc
    PROJECT_SOURCE_DIR/src/widgets/widgetstheme.qrc
)

set(LOCK_SRCS
    ${authority_DBUS_SCRS}
    ${transaction_DBUS_SCRS}
    ${GLOBAL_UTILS}
    ${GLOBAL_UTILS_DBUS}
    ${GLOBAL_UTILS_KEYBOARDMONITOR}
    ${WIDGETS}
    ${SESSION_WIDGETS}
    ${haweiswitchos_DBUS_SCRS}
    ${AUTHENTICATE}
    ${INTERFACE}
    PROJECT_SOURCE_DIR/src/dde-lock/lockframe.cpp
    PROJECT_SOURCE_DIR/src/dde-lock/lockworker.cpp
    PROJECT_SOURCE_DIR/src/dde-lock/dbus/dbuslockagent.cpp
    PROJECT_SOURCE_DIR/src/dde-lock/dbus/dbuslockfrontservice.cpp
    PROJECT_SOURCE_DIR/src/dde-lock/dbus/dbusshutdownagent.cpp
    PROJECT_SOURCE_DIR/src/dde-lock/dbus/dbusshutdownfrontservice.cpp
    main.cpp
)
add_executable(dde-session-shell-xfuzz
    ${LOCK_SRCS}
    ${QRCS}
)
target_include_directories(dde-session-shell-xfuzz PUBLIC
    ${PAM_INCLUDE_DIR}
    ${DTKWIDGET_INCLUDE_DIR}
    ${DTKCORE_INCLUDE_DIR}
    ${XCB_EWMH_INCLUDE_DIRS}
    ${DFrameworkDBus_INCLUDE_DIRS}
    ${Qt5Gui_PRIVATE_INCLUDE_DIRS}
    ${PROJECT_BINARY_DIR}
    ${QGSettings_INCLUDE_DIRS}
    ${Qt5X11Extras_INCLUDE_DIRS}
    PROJECT_SOURCE_DIR/src/dde-lock
    PROJECT_SOURCE_DIR/src/dde-lock/dbus
)
target_link_libraries(dde-session-shell-xfuzz PRIVATE
    ${Qt_LIBS}
    ${PAM_LIBRARIES}
    ${XCB_EWMH_LIBRARIES}
    ${DFrameworkDBus_LIBRARIES}
    ${DtkWidget_LIBRARIES}
    ${DtkCore_LIBRARIES}
    ${Qt5Widgets_LIBRARIES}
    ${Qt5Concurrent_LIBRARIES}
    ${Qt5X11Extras_LIBRARIES}
    ${Qt5DBus_LIBRARIES}
    ${Qt5Network_LIBRARIES}
    ${QGSettings_LIBRARIES}
)

"""


def main():
    if len(sys.argv) < 2:
        print("Please enter the path where the dde-session-shell project is located.")
        return 1
    if len(sys.argv) > 2:
        print("Has extra parameters.")
        return 1
    filedir = os.path.dirname(os.path.abspath(__file__))
    absPath = os.path.abspath(sys.argv[1])
    newfile = cmakeLists.replace("PROJECT_SOURCE_DIR", absPath)
    with open(os.path.join(filedir, "CMakeLists.txt"), "w+") as f:
        f.write(newfile)
    return 0


if __name__ == "__main__":
    main()