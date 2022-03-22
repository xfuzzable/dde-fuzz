include(projectPath.pri)
message("Project path " $$ABSPATH)
include($$ABSPATH/../common/common.pri)

QT       += core gui svg dbus x11extras concurrent multimedia dbus xml KCodecs network
#private
QT       += gui-private
LIBS	 += -lKF5Codecs -lX11

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

QT += widgets-private

TARGET = dde-file-manager-lib-xfuzz

TEMPLATE = app
CONFIG += create_pc create_prl no_install_prl

DEFINES += QMAKE_TARGET=\\\"$$TARGET\\\" QMAKE_VERSION=\\\"$$VERSION\\\"

# sp3 不稳定的feature，使用宏 UNSTABLE_FEATURE_ENABLE 屏蔽，待稳定后放开
#DEFINES += SP3_UNSTABLE_FEATURE_ENABLE

isEmpty(QMAKE_ORGANIZATION_NAME) {
    DEFINES += QMAKE_ORGANIZATION_NAME=\\\"deepin\\\"
}

isEmpty(PREFIX){
    PREFIX = ./install
}

CONFIG += c++11 link_pkgconfig
PKGCONFIG += libsecret-1 gio-unix-2.0 poppler-cpp dtkwidget dtkgui udisks2-qt5 disomaster gio-qt libcrypto Qt5Xdg dframeworkdbus polkit-agent-1 polkit-qt5-1
#DEFINES += QT_NO_DEBUG_OUTPUT
DEFINES += QT_MESSAGELOGCONTEXT

CONFIG(DISABLE_FFMPEG) | isEqual(BUILD_MINIMUM, YES) {
    DEFINES += DISABLE_FFMEPG
}

# BUILD_MINIMUM for live system
isEqual(BUILD_MINIMUM, YES){
    DEFINES += DFM_MINIMUM
}

CONFIG(DISABLE_ANYTHING) {
    message("Quick search and tag support disabled dut to Anything support disabled.")
    DEFINES += DISABLE_QUICK_SEARCH
    DEFINES += DISABLE_TAG_SUPPORT
}

# 获取标签系统设置
AC_FUNC_ENABLE = true
#AC_FUNC_ENABLE = $$(ENABLE_AC_FUNC)
# 检查集成测试标签
equals( AC_FUNC_ENABLE, true ){
    DEFINES += ENABLE_ACCESSIBILITY
    message("lib-dde-file-manager enabled accessibility function with set: " $$AC_FUNC_ENABLE)
}

include($$ABSPATH/../dialogs/dialogs.pri)
include($$ABSPATH/../utils/utils.pri)
include($$ABSPATH/../chinese2pinyin/chinese2pinyin.pri)
include($$ABSPATH/../fileoperations/fileoperations.pri)
include($$ABSPATH/deviceinfo/deviceinfo.pri)
include($$ABSPATH/devicemanagement/devicemanagement.pri)
include($$ABSPATH/dbusinterface/dbusinterface.pri)
include($$ABSPATH/../usershare/usershare.pri)
include($$ABSPATH/../dde-file-manager-plugins/plugininterfaces/plugininterfaces.pri)
include($$ABSPATH/tag/tag.pri)
include($$ABSPATH/mediainfo/mediainfo.pri)
include($$ABSPATH/vault/vault.pri)
include($$ABSPATH/log/log.pri)

isEqual(ARCH, sw_64){
    DEFINES += SW_LABEL
    include($$ABSPATH/./sw_label/sw_label.pri)
}

include($$ABSPATH/fulltextsearch/fulltextsearch.pri)
DEFINES += FULLTEXTSEARCH_ENABLE
TR_EXCLUDE += /usr/include/boost/ \
          $$ABSPATH/fulltextsearch/*

include($$ABSPATH/io/io.pri)
include($$ABSPATH/interfaces/vfs/vfs.pri)
include($$ABSPATH/interfaces/customization/customization.pri)
include($$ABSPATH/src.pri)

SOURCES += \
        $$ABSPATH/main.cpp

isEqual(ARCH, sw_64) | isEqual(ARCH, mips64) | isEqual(ARCH, mips32) | isEqual(ARCH, aarch64) | isEqual(ARCH, loongarch64) {
    include($$ABSPATH/search/dfsearch.pri)
}

#安全加固
QMAKE_CXXFLAGS += -fstack-protector-all
QMAKE_LFLAGS += -z now -fPIC
isEqual(ARCH, mips64) | isEqual(ARCH, mips32){
    QMAKE_LFLAGS += -z noexecstack -z relro
}

APPSHAREDIR = $$PREFIX/share/$$TARGET
ICONDIR = $$PREFIX/share/icons/hicolor/scalable/apps
DEFINES += APPSHAREDIR=\\\"$$APPSHAREDIR\\\"

isEmpty(LIB_INSTALL_DIR) {
    target.path = $$[QT_INSTALL_LIBS]
} else {
    target.path = $$LIB_INSTALL_DIR
}

isEmpty(INCLUDE_INSTALL_DIR) {
    includes.path = $$PREFIX/include/dde-file-manager
} else {
    includes.path = $$INCLUDE_INSTALL_DIR/dde-file-manager
}

includes.files += $$ABSPATH/interfaces/*.h $$ABSPATH/interfaces/plugins/*.h

includes_private.path = $${includes.path}/private
includes_private.files += $$ABSPATH/interfaces/private/*.h

isEmpty(INCLUDE_INSTALL_DIR) {
    gvfs_includes.path = $$PREFIX/include/dde-file-manager/gvfs
} else {
    gvfs_includes.path = $$INCLUDE_INSTALL_DIR/dde-file-manager/gvfs
}

gvfs_includes.files += $$ABSPATH/gvfs/*.h

isEmpty(INCLUDE_INSTALL_DIR) {
    plugin_includes.path = $$PREFIX/include/dde-file-manager/dde-file-manager-plugins
} else {
    plugin_includes.path = $$INCLUDE_INSTALL_DIR/dde-file-manager/dde-file-manager-plugins
}

plugin_includes.files += $$ABSPATH/../dde-file-manager-plugins/plugininterfaces/menu/*.h
plugin_includes.files += $$ABSPATH/../dde-file-manager-plugins/plugininterfaces/preview/*.h
plugin_includes.files += $$ABSPATH/../dde-file-manager-plugins/plugininterfaces/view/*.h

QMAKE_PKGCONFIG_LIBDIR = $$target.path
QMAKE_PKGCONFIG_VERSION = $$VERSION
QMAKE_PKGCONFIG_DESTDIR = pkgconfig
QMAKE_PKGCONFIG_NAME = dde-file-manager
QMAKE_PKGCONFIG_DESCRIPTION = DDE File Manager Header Files
QMAKE_PKGCONFIG_INCDIR = $$includes.path

templateFiles.path = $$APPSHAREDIR/templates

isEqual(BUILD_MINIMUM, YES){
    templateFiles.files = skin/templates/newTxt.txt
}else{
    templateFiles.files = skin/templates/newDoc.doc \
        skin/templates/newExcel.xls \
        skin/templates/newPowerPoint.ppt \
        skin/templates/newDoc.wps \
        skin/templates/newExcel.et \
        skin/templates/newPowerPoint.dps \
        skin/templates/newTxt.txt
}

mimetypeFiles.path = $$APPSHAREDIR/mimetypes
mimetypeFiles.files += \
    mimetypes/archive.mimetype \
    mimetypes/text.mimetype \
    mimetypes/video.mimetype \
    mimetypes/audio.mimetype \
    mimetypes/image.mimetype \
    mimetypes/executable.mimetype \
    mimetypes/backup.mimetype

mimetypeAssociations.path = $$APPSHAREDIR/mimetypeassociations
mimetypeAssociations.files += \
    $$APPSHAREDIR/mimetypeassociations/mimetypeassociations.json

icon.path = $$ICONDIR
icon.files = $$ABSPATH/skin/images/$${TARGET}.svg

defaultConfig.path = $$APPSHAREDIR/config
defaultConfig.files = $$ABSPATH/configure/default-view-states.json

# readme file for create oem-menuextension directory
readmefile.path = $$PREFIX/share/deepin/$$TARGET/oem-menuextensions
readmefile.files = $$ABSPATH/plugins/.readme

# readme file for create context-menus directory
contextmenusfile.path = /usr/share/applications/context-menus
contextmenusfile.files = $$ABSPATH/plugins/.readme

appentry.path = $$APPSHAREDIR/extensions/appEntry
appentry.files = $$ABSPATH/plugins/.readme

INSTALLS += target templateFiles mimetypeFiles mimetypeAssociations appentry \
 icon includes includes_private gvfs_includes plugin_includes defaultConfig readmefile contextmenusfile policy

DISTFILES += \
    $$ABSPATH/mimetypeassociations/mimetypeassociations.json \
    $$ABSPATH/confirm/deepin-vault-authenticateProxy \
    $$ABSPATH/policy/com.deepin.pkexec.deepin-vault-authenticateProxy.policy

include($$ABSPATH/settings_dialog_json.pri)