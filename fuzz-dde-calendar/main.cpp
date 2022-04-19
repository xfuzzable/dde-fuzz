
#include <QString>
#include <QDebug>
#include <QByteArray>
#include "utils.h"
#include <QJsonDocument>
#include <QJsonArray>
#include "xfuzz.h"

//自定义转换函数，输入是任意数量的支持的类型（包括其他自定义类型）
QString to_qstring(std::string &s) {
    return QString(s.c_str());
}

XFUZZ_CUSTOM_CONVERTER(to_qstring);

void test(uint8_t caseId, QString params, qint64 id, QString jobInfo, QString typeInfo, QString startTime, QString endTime, qint32 maxNum, QString rules) {
    CalendarScheduler * cs = new CalendarScheduler;

    caseId = 1 + caseId % 12;

    if (caseId == 1){
        QString varType = cs->GetType(id);
        qInfo() << "varType: " << varType;
    }
    if (caseId == 2){
        QString varTypes = cs->GetTypes();
        qInfo() << "varTypes: " << varTypes;
    }
    if (caseId == 3){
        qInfo() << "QueryJobs: " << params;
        QString varQueryJobs = cs->QueryJobs(params);
        qInfo() << "varQueryJobs: " << varQueryJobs;
    }
    if (caseId == 4){
        cs->DeleteJob(id);
    }
    if (caseId == 5){
        cs->DeleteType(id);
    }
    if (caseId == 6){
        QString varJobId = cs->GetJob(id);
        qInfo() << "varJobId: " << varJobId;
    }
    if (caseId == 7){
        qint64 varCreateJob = cs->CreateJob(jobInfo);
        qInfo() << "varCreateJob: " << varCreateJob;
    }
    if (caseId == 8){
        cs->UpdateJob(jobInfo);
    }
    if (caseId == 9){
        cs->UpdateType(typeInfo);
    }
    if (caseId == 10){
        QDateTime start = QDateTime::fromString(startTime, "yyyy-MM-ddThh:mm:ss");
        QDateTime end = QDateTime::fromString(endTime, "yyyy-MM-ddThh:mm:ss");
        QString varJobs = cs->GetJobs(start, end);
        qInfo() << "varJobs: " << varJobs;
    }
    if (caseId == 11){
        QString varQueryJobsWithLimit = cs->QueryJobsWithLimit(params, maxNum);
        qInfo() << "varQueryJobsWithLimit: " << varQueryJobsWithLimit;
    }
    if (caseId == 12){
        QString varQueryJobsWithRule = cs->QueryJobsWithRule(params, rules);
        qInfo() << "varQueryJobsWithRule: " << varQueryJobsWithRule;
    }
    delete cs;
}

XFUZZ_TEST_ENTRYPOINT(test);




