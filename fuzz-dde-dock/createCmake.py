#!/usr/bin/python
import os 
import sys 

cmakeLists = """
cmake_minimum_required(VERSION 3.7)
project(dde-dock)
set(BIN_NAME dde-dock-xfuzz)

if (CMAKE_BUILD_TYPE STREQUAL "Debug")
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -g -fsanitize=address -O2")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g -fsanitize=address -O2")
endif()

set(DDE_DOCK_PATH dde-dock-project-abspath)
message("DDE_DOCK_PATH -> " ${DDE_DOCK_PATH})
set(SRCS 
    ${DDE_DOCK_PATH}/frame/util/themeappicon.h
    ${DDE_DOCK_PATH}/frame/util/themeappicon.cpp
    ${DDE_DOCK_PATH}/frame/util/imageutil.h 
    ${DDE_DOCK_PATH}/frame/util/imageutil.cpp
)

# Find the library
find_package(PkgConfig REQUIRED)
find_package(Qt5Widgets REQUIRED)
find_package(Qt5Concurrent REQUIRED)
find_package(Qt5X11Extras REQUIRED)
find_package(Qt5DBus REQUIRED)
find_package(Qt5Svg REQUIRED)
find_package(DtkWidget REQUIRED)
find_package(DtkCMake REQUIRED)

pkg_check_modules(XCB_EWMH REQUIRED xcb-ewmh x11 xcursor)
pkg_check_modules(DFrameworkDBus REQUIRED dframeworkdbus)
pkg_check_modules(QGSettings REQUIRED gsettings-qt)
pkg_check_modules(DtkGUI REQUIRED dtkgui)

# driver-manager
add_executable(${BIN_NAME} main.cpp ${SRCS})

target_include_directories(${BIN_NAME} PUBLIC
    ${DtkWidget_INCLUDE_DIRS}
    ${XCB_EWMH_INCLUDE_DIRS}
    ${DFrameworkDBus_INCLUDE_DIRS}
    ${Qt5Gui_PRIVATE_INCLUDE_DIRS}
    ${PROJECT_BINARY_DIR}
    ${QGSettings_INCLUDE_DIRS}
    ${DtkGUI_INCLUDE_DIRS}
    ${Qt5Svg_INCLUDE_DIRS}
    ${DDE_DOCK_PATH}/frame/util
)

target_link_libraries(${BIN_NAME} PRIVATE
    ${XCB_EWMH_LIBRARIES}
    ${DFrameworkDBus_LIBRARIES}
    ${DtkWidget_LIBRARIES}
    ${Qt5Widgets_LIBRARIES}
    ${Qt5Gui_LIBRARIES}
    ${Qt5Concurrent_LIBRARIES}
    ${Qt5X11Extras_LIBRARIES}
    ${Qt5DBus_LIBRARIES}
    ${QGSettings_LIBRARIES}
    ${DtkGUI_LIBRARIES}
    ${Qt5Svg_LIBRARIES}
)

if (${CMAKE_SYSTEM_PROCESSOR} STREQUAL "sw_64")
    target_compile_definitions(${BIN_NAME} PUBLIC DISABLE_SHOW_ANIMATION)
endif()

if (${CMAKE_SYSTEM_PROCESSOR} STREQUAL "mips64")
    target_compile_definitions(${BIN_NAME} PUBLIC DISABLE_SHOW_ANIMATION)
endif()

if (${CMAKE_SYSTEM_PROCESSOR} STREQUAL "aarch64")
    target_compile_definitions(${BIN_NAME} PUBLIC DISABLE_SHOW_ANIMATION)
endif()

# bin
install(TARGETS ${BIN_NAME} DESTINATION bin)
"""


def main():
    if len(sys.argv) < 2:
        print("Please enter the path where the dde-dock project is located.")
        return 1
    if len(sys.argv) > 2:
        print("Has extra parameters.")
        return 1
    filedir = os.path.dirname(os.path.abspath(__file__))
    absPath = os.path.abspath(sys.argv[1])
    newfile = cmakeLists.replace("dde-dock-project-abspath", absPath)
    with open(os.path.join(filedir, "CMakeLists.txt"), "w+") as f:
        f.write(newfile)
    return 0


if __name__ == "__main__":
    main()