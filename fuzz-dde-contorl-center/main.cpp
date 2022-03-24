#include "widgets/basiclistmodel.h"
#include <QString>
#include <QDebug>
#include <QByteArray>

using namespace dcc::widgets;


extern "C" void xfuzz_test_one(char *Data, size_t DataSize) {
    if (DataSize == 0){
        return;
    }else{
        const QByteArray databuf = QByteArray(Data, DataSize);
        QString s(databuf);
        BasicListModel *obj = new BasicListModel;
        obj->appendOption(s, s);
        obj->rowCount(obj->index(0));
        obj->data(obj->index(0), BasicListModel::ItemSizeRole);
        obj->setSelectedIndex(obj->index(0));
        obj->setHoveredIndex(obj->index(0));
        obj->clear();
        delete obj;
    }
}
