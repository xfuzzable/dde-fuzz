#!/usr/bin/python
import os 
import sys 

cmakeLists = """
cmake_minimum_required(VERSION 3.7)
project(dde-control-center)
find_package(DtkCMake REQUIRED)
set(STRONG_PASSWORD false)
set(AllowEnableMultiScaleRatio false)
set(AllowCloudSync true)
add_definitions(-DWINDOW_MODE)

set(CMAKE_VERBOSE_MAKEFILE ON)
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_CXX_FLAGS "-g -Wall -Wl,--as-need -fPIE")
ADD_DEFINITIONS(-DQT_NO_KEYWORDS)
if (DEFINED ENABLE_MIEEE)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -mieee")
endif()

set(DEFINED_LIST
DISABLE_OPACITY_ANIMATION
DISABLE_CLOUD_SYNC
DISABLE_SYS_UPDATE
DISABLE_AUTHENTICATION
DISABLE_ACCOUNT
DISABLE_DISPLAY
DISABLE_DEFAULT_APPLICATIONS
DISABLE_PERSONALIZATION
DISABLE_BLUETOOTH
DISABLE_SOUND
DISABLE_DATETIME
DISABLE_POWER
DISABLE_MOUSE
DISABLE_KAYBOARD
DISABLE_WACOM
DISABLE_SYSINFO
DISABLE_SYS_UPDATE_SOURCE_CHECK
DISABLE_SYS_UPDATE_MIRRORS
DISABLE_MAIN_PAGE
DISABLE_RECOVERY
DCC_ENABLE_ADDOMAIN
DCC_DISABLE_KBLAYOUT
DCC_DISABLE_LANGUAGE
DCC_DISABLE_POWERSAVE
DCC_DISABLE_FEEDBACK
DCC_DISABLE_ROTATE
DCC_DISABLE_MIRACAST
DCC_DISABLE_TIMEZONE
DCC_DISABLE_GRUB
DCC_KEEP_SETTINGS_LIVE
DCC_COMMUNITY_LICENSE
)

find_package(PkgConfig REQUIRED)
find_package(DtkWidget REQUIRED)
find_package(DtkGui REQUIRED)
find_package(DtkCMake REQUIRED)
find_package(PolkitQt5-1)
find_package(Qt5 COMPONENTS
    Core
    Widgets
    Concurrent
    X11Extras
    DBus
    Multimedia
    Svg
REQUIRED)

pkg_check_modules(XCB_EWMH REQUIRED xcb-ewmh x11 xext)
pkg_check_modules(DFrameworkDBus REQUIRED dframeworkdbus)
pkg_check_modules(QGSettings REQUIRED gsettings-qt)
pkg_check_modules(Gio-2.0 REQUIRED gio-2.0)

if (NOT DEFINED DISABLE_RECOVERY)
    pkg_search_module(UDisk2 REQUIRED udisks2-qt5)
    include_directories(AFTER ${UDisk2_INCLUDE_DIRS})
endif()

set(BIN_NAME dde-control-center-xfuzz)

set(PROJET_PATH dde-control-center-project-abspath)
set(FUZZ_PROJET_PATH fuzz-dde-control-center-xfuzz-project-abspath)
add_executable(${BIN_NAME} ${FUZZ_PROJET_PATH}/main.cpp ${PROJET_PATH}/src/frame/widgets/basiclistmodel.cpp ${PROJET_PATH}/include/widgets/basiclistmodel.h)

target_include_directories(${BIN_NAME} PUBLIC
    ${PROJET_PATH}/include
    ${DtkWidget_INCLUDE_DIRS}
    ${XCB_EWMH_INCLUDE_DIRS}
    ${DFrameworkDBus_INCLUDE_DIRS}
    ${Qt5Gui_PRIVATE_INCLUDE_DIRS}
    ${PROJECT_BINARY_DIR}
    ${QGSettings_INCLUDE_DIRS}
    ${Gio-2.0_INCLUDE_DIRS}
    ${Qt5X11Extras_INCLUDE_DIRS}
)
target_link_libraries(${BIN_NAME} PRIVATE
    ${XCB_EWMH_LIBRARIES}
    ${DFrameworkDBus_LIBRARIES}
    ${DtkWidget_LIBRARIES}
    ${Qt5Widgets_LIBRARIES}
    ${Qt5Concurrent_LIBRARIES}
    ${Qt5X11Extras_LIBRARIES}
    ${Qt5DBus_LIBRARIES}
    ${Qt5Multimedia_LIBRARIES}
    ${QGSettings_LIBRARIES}
    ${Gio-2.0_LIBRARIES}
    ${Qt5Svg_LIBRARIES}
    ${DEEPIN_PW_CHECK}
    ${SHMN_VIDEO}
    crypt
    ${LIBS}
    PolkitQt5-1::Agent
)
"""


def main():
    if len(sys.argv) < 2:
        print("Please enter the path where the dde-control-center project is located.")
        return 1
    if len(sys.argv) > 2:
        print("Has extra parameters.")
        return 1
    filedir = os.path.dirname(os.path.abspath(__file__))
    absPath = os.path.abspath(sys.argv[1])
    newfile = cmakeLists.replace("dde-control-center-project-abspath", absPath)
    newfile = newfile.replace("fuzz-dde-control-center-xfuzz-project-abspath", filedir)
    with open(os.path.join(filedir, "CMakeLists.txt"), "w+") as f:
        f.write(newfile)
    return 0


if __name__ == "__main__":
    main()