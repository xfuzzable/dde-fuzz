#include "widgets/basiclistmodel.h"
#include <QString>
#include <QDebug>
#include <QByteArray>
#include "xfuzz.h"
using namespace dcc::widgets;

QString to_qstring(std::string &s) {
    return QString(s.c_str());
}

XFUZZ_CUSTOM_CONVERTER(to_qstring);

void testBasicListModel(QString &s1, QString &s2, int countIndex, int selectedIndex, int hoveredIndex) {
    BasicListModel *obj = new BasicListModel;
    obj->appendOption(s1, s2);
    obj->rowCount(obj->index(countIndex));
    obj->data(obj->index(0), BasicListModel::ItemSizeRole);
    obj->setSelectedIndex(obj->index(selectedIndex));
    obj->setHoveredIndex(obj->index(hoveredIndex));
    obj->clear();
    delete obj;
}

XFUZZ_TEST_ENTRYPOINT(testBasicListModel);
