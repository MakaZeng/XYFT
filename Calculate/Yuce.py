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

        persons = [100,101,102,103,104,105,106,107,108,109]
        names = ["1","2","3","4","5","6","7","8","9","10"]

        for person in persons:
            self.getTouzhuForPerson(person,names[person - 100])
        # sql = "select {0} from {1} order by {2} DESC LIMIT 1".format(DBC.HISQI,DBC.HISTAB, DBC.HISQI)
        # top = DBM.maka_do_sql(sql)
        # top = top[0][0]
        # longTop = long(top)
        # if longTop %180 == 0 :
        #     next = DU.getNextDayZeroQishu(top)
        #     top = next
        #
        # currentTime = long(time.time())
        # currentTime = DU.convertSecondsFrom1970ToDate(currentTime)
        #
        # type = self.getRandom()
        #
        # insertsql = 'INSERT INTO {0}.{1} ({2},{3},{4},{5},{6},{7},{8}) \
        #     VALUES '.format(DBC.Database, DBC.BLTAB, \
        #     DBC.BLQI, DBC.BLTIME, DBC.BLROAD, DBC.BLNUMBER, DBC.BLMONEY,DBC.BLSTATUS, DBC.BLPERSON, )
        #
        # personID = 100
        #
        # numbers = type['numbers']
        # for n in numbers:
        #     insertsql = insertsql + "('{0}','{1}','{2}',{3},{4},{5},{6}),".format( \
        #     str(long(top)+1),currentTime,type['road'],n,long(type['beat']),0,personID)
        #
        # insertsql = insertsql[:-1]
        # print insertsql
        # DBM.maka_do_sql(insertsql)

    def getTouzhuForPerson(self,person,name):
        sql = "select * from {0} where {1} = {2};".format(DBC.PSTAB,DBC.PSID,person)
        result = DBM.maka_do_sql(sql)
        if not result:
            result = USERCONTROLLER.inertPersonWith(person,name,name)
            print result



    def getRandom(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        roads = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        beats = [100, 200, 500, 1000, 2000]
        random.shuffle(numbers)
        random.shuffle(roads)
        random.shuffle(beats)
        random.seed(time.time())
        return {'numbers':numbers[0:random.randint(3,5)],'road':roads[0],'beat':beats[0]}