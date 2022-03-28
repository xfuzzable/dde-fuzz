#!/usr/bin/python
import os 
import sys 
import time

cmakeLists = """
cmake_minimum_required(VERSION 3.7)

set(VERSION 4.0)

project(dde-launcher)

#set(CMAKE_VERBOSE_MAKEFILE ON)
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_CXX_FLAGS "-g -Wall")                                                                                                               

# 增加安全编译参数
ADD_DEFINITIONS("-fstack-protector-strong -D_FORTITY_SOURCE=1 -z noexecstack -pie -fPIC -z lazy")

if (CMAKE_BUILD_TYPE STREQUAL "Debug")
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -g -fsanitize=address -O2")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g -fsanitize=address -O2")
endif()

if (DEFINED ENABLE_MIEEE)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -mieee")
endif()

if (DEFINED DISABLE_DRAG_ANIMATION)
    add_definitions(-DDISABLE_DRAG_ANIMATION)
endif ()

if (DEFINED WITHOUT_UNINSTALL_APP)
    add_definitions(-DWITHOUT_UNINSTALL_APP)
endif ()

set(BIN_NAME dde-launcher-xfuzz)

# Sources files
file(GLOB_RECURSE SRCS "dde-launcher-project-abspath/src/*.h" "dde-launcher-project-abspath/src/*.cpp")

list(REMOVE_ITEM SRCS "dde-launcher-project-abspath/src/main.cpp")

# Install settings
if (CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
    set(CMAKE_INSTALL_PREFIX /usr)
endif ()

# if (NOT (${CMAKE_BUILD_TYPE} MATCHES "Debug"))
#     set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Ofast")

#     # generate qm
#     execute_process(COMMAND bash "dde-launcher-project-abspath/translate_generation.sh"
#                     WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})
# endif ()

# dev
file(GLOB INTERFACES "dde-launcher-project-abspath/src/dbusinterface/*.h")

# Find the library
find_package(PkgConfig REQUIRED)
find_package(Qt5Widgets REQUIRED)
find_package(Qt5Concurrent REQUIRED)
find_package(Qt5X11Extras REQUIRED)
find_package(Qt5DBus REQUIRED)
find_package(DtkWidget REQUIRED)
find_package(Qt5Svg REQUIRED)
find_package(DtkCore REQUIRED)

pkg_check_modules(XCB_EWMH REQUIRED xcb-ewmh)
pkg_check_modules(DFrameworkDBus REQUIRED dframeworkdbus)
pkg_check_modules(QGSettings REQUIRED gsettings-qt)

include_directories(
    dde-launcher-project-abspath/src
    dde-launcher-project-abspath/src/boxframe
    dde-launcher-project-abspath/src/dbusinterface
    dde-launcher-project-abspath/src/dbusinterface/dbusvariant
    dde-launcher-project-abspath/src/dbusservices
    dde-launcher-project-abspath/src/delegate
    dde-launcher-project-abspath/src/global_util
    dde-launcher-project-abspath/src/model
    dde-launcher-project-abspath/src/skin
    dde-launcher-project-abspath/src/view
    dde-launcher-project-abspath/src/widgets
    dde-launcher-project-abspath/src/worker
)

aux_source_directory(dde-launcher-project-abspath/src SRC)
aux_source_directory(dde-launcher-project-abspath/src/boxframe BOXFRAME)
aux_source_directory(dde-launcher-project-abspath/src/dbusinterface DBUSINTERFACE)
aux_source_directory(dde-launcher-project-abspath/src/dbusinterface/dbusvariant DBUSVARIANT)
aux_source_directory(dde-launcher-project-abspath/src/dbusservices DBUSSERVICES)
aux_source_directory(dde-launcher-project-abspath/src/delegate DELEGATE)
aux_source_directory(dde-launcher-project-abspath/src/global_util GLOBAL_UTIL)
aux_source_directory(dde-launcher-project-abspath/src/model MODEL)
aux_source_directory(dde-launcher-project-abspath/src/skin SKIN)
aux_source_directory(dde-launcher-project-abspath/src/view VIEW)
aux_source_directory(dde-launcher-project-abspath/src/widgets WIDGETS)
aux_source_directory(dde-launcher-project-abspath/src/worker WORKER)

file(GLOB SRC_PATH
    ${SRC}
    ${BOXFRAME}
    ${DBUSINTERFACE}
    ${DBUSVARIANT}
    ${DBUSSERVICES}
    ${DELEGATE}
    ${GLOBAL_UTIL}
    ${MODEL}
    ${SKIN}
    ${VIEW}
    ${WIDGETS}
    ${WORKER}
    fuzz-dde-launcher-xfuzz-project-abspath/main.cpp
)

add_executable(${BIN_NAME}  ${SRCS} ${SRC_PATH} ${INTERFACES} dde-launcher-project-abspath/src/skin.qrc dde-launcher-project-abspath/src/widgets/images.qrc)
target_include_directories(${BIN_NAME} PUBLIC
    ${DtkWidget_INCLUDE_DIRS}
    ${DtkCore_INCLUDE_DIRS}
    ${XCB_EWMH_INCLUDE_DIRS}
    ${DFrameworkDBus_INCLUDE_DIRS}
    ${Qt5Gui_PRIVATE_INCLUDE_DIRS}
    ${QGSettings_INCLUDE_DIRS}
    ${PROJECT_BINARY_DIR}
)

target_link_libraries(${BIN_NAME} PRIVATE
    ${XCB_EWMH_LIBRARIES}
    ${DFrameworkDBus_LIBRARIES}
    ${DtkWidget_LIBRARIES}
    ${DtkCore_LIBRARIES}
    ${Qt5Widgets_LIBRARIES}
    ${Qt5Concurrent_LIBRARIES}
    ${Qt5X11Extras_LIBRARIES}
    ${Qt5DBus_LIBRARIES}
    ${QGSettings_LIBRARIES}
    ${Qt5Svg_LIBRARIES}
)

## qm files
file(GLOB QM_FILES "dde-launcher-project-abspath/translations/*.qm")
install(FILES ${QM_FILES} DESTINATION dde-launcher-project-abspath/share/dde-launcher/translations)

## dev files
install (FILES ${INTERFACES} DESTINATION include/dde-launcher)

## desktop file
install(FILES dde-launcher.desktop DESTINATION dde-launcher-project-abspath/share/applications/)
install(FILES dde-launcher-wapper DESTINATION bin PERMISSIONS OWNER_READ OWNER_WRITE OWNER_EXECUTE GROUP_READ GROUP_EXECUTE WORLD_READ WORLD_EXECUTE)

## services files
install(FILES dde-launcher-project-abspath/src/dbusservices/com.deepin.dde.Launcher.service DESTINATION /usr/share/dbus-1/services)

#schemas
install(FILES gschema/com.deepin.dde.launcher.gschema.xml DESTINATION share/glib-2.0/schemas)
install(CODE "execute_process(COMMAND glib-compile-schemas ${CMAKE_INSTALL_PREFIX}/share/glib-2.0/schemas)")

## icon
install(FILES data/deepin-launcher.svg DESTINATION /usr/share/icons/hicolor/scalable/apps)

# bin
install(TARGETS ${BIN_NAME} DESTINATION bin)

# config
dconfig_meta_files(APPID dde-launcher BASE ./configs FILES ./configs/default.json)

"""


def main():
    if len(sys.argv) < 2:
        print("Please enter the path where the dde-launcher project is located.")
        return 1
    if len(sys.argv) > 2:
        print("Has extra parameters.")
        return 1
    filedir = os.path.dirname(os.path.abspath(__file__))
    absPath = os.path.abspath(sys.argv[1])
    newfile = cmakeLists.replace("dde-launcher-project-abspath", absPath)
    newfile = newfile.replace("fuzz-dde-launcher-xfuzz-project-abspath", filedir)
    with open(os.path.join(filedir, "CMakeLists.txt"), "w+") as f:
        f.write(newfile)
    return 0


if __name__ == "__main__":
    main()