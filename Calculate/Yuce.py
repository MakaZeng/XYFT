#encoding:utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import CalculateManager as CM
import Dao.MysqlDBManager as DBM
import Dao.MysqlDBConfig as DBC
import random
import time
import Util.DateUtil as DU
import Touzhu.TouzhuController as TZ
import Dao.DatabaseCreator as CREATOR
import User.UserController as USERCONTROLLER

class Yuce(object):
    def __init__(self):
        super(Yuce, self).__init__()

    def startYuce(self):

        CREATOR.CreateTablePersonIfNotEXist()
        CREATOR.CreateTableBeatListIfNotEXist()

        sql = "select {0} from {1} order by {0} DESC limit 1".format(DBC.HISQI,DBC.HISTAB)
        result = DBM.maka_do_sql(sql)
        qishu = result[0][0]

        persons = [100,101,102,103,104,105,106,107,108,109]
        names = ["菜鸟计划","山神计划","盖伦计划","宝贝计划","二狗计划","老马计划","必赢计划","莎莎计划","李仙人计划","白小姐计划"]

        for person in persons:
            self.getTouzhuForPerson(person,names[person - 100],qishu)

    def calculateHistoryYuce(self):
        sql = "select {0},{1},{2},{3},{4},{5} from {6} where {7} == 0;".format(DBC.BLID,DBC.BLROAD,DBC.BLNUMBER,DBC.BLMONEY,DBC.BLPERSON,DBC.BLQI,DBC.BLTAB,DBC.BLSTATUS)
        result = DBM.maka_do_sql(sql)
        for line in result:
            road = line['road']
            numbers = line['numbers']
            beat = line['beat']
            id = line['id']
            person = line['personID']
            qishu = line['qishu']
            sql = "select * from history where qishu = {0};".format(qishu)
            result = DBM.maka_do_sql(sql)
            his = [result[DBC.HISN1],result[DBC.HISN2],result[DBC.HISN3],result[DBC.HISN4],result[DBC.HISN5],result[DBC.HISN6],result[DBC.HISN7],result[DBC.HISN8],result[DBC.HISN9],result[DBC.HISN10]]
            target = his[road-1]
            isIn = 2
            for n in numbers.split(','):
                if n==target:
                    isIn = 1
            sql = "update beatlist set status = {0} where id = {1};".format(isIn,id)
            DBM.maka_do_sql(sql)


    def getTouzhuForPerson(self,person,name,qishu):
        sql = "select * from {0} where {1} = {2};".format(DBC.PSTAB,DBC.PSID,person)
        result = DBM.maka_do_sql(sql)
        if not result:
            result = USERCONTROLLER.inertPersonWith(person,name,name)
            print result
        else:
            tuple = result[0]
            touzhu = self.getRandom()

            currentTime = long(time.time())
            currentTime = DU.convertSecondsFrom1970ToDate(currentTime)

            numbers = touzhu['numbers']
            numbers = ','.join(numbers)

            sql = "insert into {0} ({1},{2},{3},{4},{5},{6},{7}) values ('{8}','{9}','{10}','{11}',{12},{13},{14})" \
            .format(DBC.BLTAB,DBC.BLQI,DBC.BLTIME,DBC.BLROAD,DBC.BLNUMBER,DBC.BLMONEY,DBC.BLSTATUS,DBC.BLPERSON, \
            qishu,currentTime,str(touzhu['road']),numbers,touzhu['beat'],0,person)
            DBM.maka_do_sql(sql)


    def getRandom(self):
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        roads = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        beats = [100, 200, 500, 1000, 2000]
        random.shuffle(numbers)
        random.shuffle(roads)
        random.shuffle(beats)
        random.seed(time.time())
        return {'numbers':numbers[0:random.randint(3,5)],'road':roads[0],'beat':beats[0]}
