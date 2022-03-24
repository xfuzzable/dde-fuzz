#!/usr/bin/python
import os 
import sys 

cmakeLists = """
cmake_minimum_required(VERSION 3.7)
project(dde-calendar-xfuzz)

find_package(PkgConfig REQUIRED)
find_package(Qt5 COMPONENTS
    Core
    DBus
REQUIRED)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_AUTOMOC ON)

#安全编译参数
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fstack-protector-strong -D_FORTITY_SOURCE=1 -z noexecstack -pie -fPIC -z lazy")
set(PROJECT_PATH dde-calendar-abspath)
include_directories(${PROJECT_PATH}/calendar-basicstruct/src)
file(GLOB_RECURSE BASESTRUCT_SRCS ${PROJECT_PATH}/calendar-basicstruct/src/*.cpp)

add_executable(${PROJECT_NAME} main.cpp ${BASESTRUCT_SRCS})

target_include_directories(${PROJECT_NAME} PUBLIC
    ${PROJECT_PATH}/calendar-basicstruct/src
    ${DtkWidget_INCLUDE_DIRS}
    ${XCB_EWMH_INCLUDE_DIRS}
    ${DFrameworkDBus_INCLUDE_DIRS}
    ${Qt5Gui_PRIVATE_INCLUDE_DIRS}
    ${PROJECT_BINARY_DIR}
    ${QGSettings_INCLUDE_DIRS}
    ${Gio-2.0_INCLUDE_DIRS}
    ${Qt5X11Extras_INCLUDE_DIRS}
)
target_link_libraries(${PROJECT_NAME} PRIVATE
    ${XCB_EWMH_LIBRARIES}
    ${DFrameworkDBus_LIBRARIES}
    ${DtkWidget_LIBRARIES}
    ${Qt5Widgets_LIBRARIES}
    ${Qt5Concurrent_LIBRARIES}
    ${Qt5X11Extras_LIBRARIES}
    ${Qt5DBus_LIBRARIES}
    ${Qt5Multimedia_LIBRARIES}
    ${QGSettings_LIBRARIES}
    ${Qt5Svg_LIBRARIES}
    ${DEEPIN_PW_CHECK}
    ${SHMN_VIDEO}
    ${LIBS}
)
"""


def main():
    if len(sys.argv) < 2:
        print("Please enter the path where the dde-calendar project is located.")
        return 1
    if len(sys.argv) > 2:
        print("Has extra parameters.")
        return 1
    filedir = os.path.dirname(os.path.abspath(__file__))
    absPath = os.path.abspath(sys.argv[1])
    newfile = cmakeLists.replace("dde-calendar-abspath", absPath)
    with open(os.path.join(filedir, "CMakeLists.txt"), "w+") as f:
        f.write(newfile)
    return 0


if __name__ == "__main__":
    main()