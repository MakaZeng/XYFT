# coding=utf-8
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

        sql = "select {0} from {1} order by {0} limit 1".format(DBC.HISQI,DBC.HISTAB)
        result = DBM.maka_do_sql(sql)
        qishu = result[0][0]

        persons = [100,101,102,103,104,105,106,107,108,109]
        names = ["幸运计划","牛牛计划","彩蛋计划","水果计划","主席计划","山羊计划","盖伦计划","小黑计划","进取计划","勇气计划"]

        for person in persons:
            self.getTouzhuForPerson(person,names[person - 100],qishu)

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
