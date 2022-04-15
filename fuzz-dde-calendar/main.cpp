
// #include <QString>
// #include <QDebug>
// #include <QByteArray>
// #include "utils.h"
// #include <QJsonDocument>
// #include <QJsonArray>
// #include "xfuzz.h"

// //自定义转换函数，输入是任意数量的支持的类型（包括其他自定义类型）
// QString to_qstring(std::string &s) {
//     return QString(s.c_str());
// }

// XFUZZ_CUSTOM_CONVERTER(to_qstring);

// void test(QString &s) {
//     qInfo() << s;
//     Utils * ut = new Utils();
//     auto qdt = ut->fromconvertData(s);
//     qInfo() << qdt;
//     auto qs = ut->toconvertData(qdt);
//     qInfo() << qs;
//     auto qdt1 = ut->fromconvertiIGData(s);
//     qInfo() << qdt1;
//     auto qs1 = ut->toconvertData(qdt1);
//     qInfo() << qs;
//     delete ut;
// }

// XFUZZ_TEST_ENTRYPOINT(test);


#include <QCoreApplication>
#include <DLog>
#include <QDBusConnection>
#include <QDBusError>
#include <QTranslator>
#include <QDebug>
#include "calendarscheduler.h"
#include <random>
#include "xfuzz.h"


QString to_qstring(std::string &s) {
    return QString(s.c_str());
}

XFUZZ_CUSTOM_CONVERTER(to_qstring);

qint64 to_qint64(long int x) {
    return static_cast<qint64>(x);
}

XFUZZ_CUSTOM_CONVERTER(to_qint64);

qint32 to_qint32(int x) {
    return static_cast<qint32>(x);
}

XFUZZ_CUSTOM_CONVERTER(to_qint32);


QCoreApplication *app;


void test_init(){
    qputenv("QT_QPA_PLATFORM", "offscreen");
    static char* argv[] = {"./dde-calendar-service-xfuzz", nullptr};
    int argc = 1;
    app = new QCoreApplication(argc,argv);
}

    // QString GetType(qint64 id);
    // QString GetTypes();
    // void DeleteJob(qint64 id);
    // void DeleteType(qint64 id);
    // QString GetJob(qint64 id);
    // qint64 CreateJob(const QString &jobInfo);
    // void UpdateJob(const QString &jobInfo);
    // void UpdateType(const QString &typeInfo);
    // QString GetJobs(const QDateTime &start, const QDateTime &end);
    // QString QueryJobs(const QString &params);
    // QString QueryJobsWithLimit(const QString &params, qint32 maxNum);
    // QString QueryJobsWithRule(const QString &params, const QString &rules);


void testCalendarScheduler(int caseId, qint64 id, QString jobInfo, QString typeInfo, QString startTime, QString endTime, QString params, qint32 maxNum, QString rules){
    CalendarScheduler * cs = new CalendarScheduler;

    // std::random_device r;
    // std::default_random_engine e1(r());
    // std::uniform_int_distribution<int> uniform_dist(0, 13);
    // for (int i = 0; i < 26; i++)
    // {
    //  caseId = uniform_dist(e1);
        if (caseId == 1){
            QString varType = cs->GetType(id);
            qInfo() << "varType: " << varType;
        }
        if (caseId == 2){
            QString varTypes = cs->GetTypes();
            qInfo() << "varTypes: " << varTypes;
        }
        if (caseId == 3){
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
    //}

    delete cs;
}


XFUZZ_TEST_ENTRYPOINT_WITH_INIT(
    testCalendarScheduler, 
    test_init
);





