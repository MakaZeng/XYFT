import CalculateManager as CM
import Dao.MysqlDBManager as DBM
import Dao.MysqlDBConfig as DBC
import random

class Yuce(object):
    def __init__(self):
        super(Yuce, self).__init__()

    def startYuce(self):

        sql = "select {0} from {1} order by {2} DESC LIMIT 1".format(DBC.HISQI,DBC.HISTAB, DBC.HISQI)
        top = DBM.maka_do_sql(sql)
        top = top[0][0]

        sql = "CREATE TABLE IF NOT EXISTS yuce (`qishutype` varchar(100) COLLATE utf8_bin NOT NULL,`road` varchar(50) DEFAULT NULL,`beat` varchar(50) DEFAULT NULL,`status` varchar(50) DEFAULT NULL,`numbers` varchar(100) COLLATE utf8_bin DEFAULT NULL,PRIMARY KEY (`qishutype`),UNIQUE KEY `qishutype_UNIQUE` (`qishutype`)) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;"
        DBM.maka_do_sql(sql)

        type1 = self.getRandom()
        insertsql = "INSERT INTO {0}.{1} (qishutype,status,road,numbers,beat) VALUES ('{2}','{3}','{4}','{5}','{6}');".format(DBC.Database,'yuce',str(long(top)+1)+'1','0',type1['road'],type1['numbers'],type1['beat'])
        DBM.maka_do_sql(insertsql)

        type2 = self.getRandom()
        insertsql = "INSERT INTO {0}.{1} (qishutype,status,road,numbers,beat) VALUES ('{2}','{3}','{4}','{5}','{6}');".format(
            DBC.Database, 'yuce', str(long(top)+1)+'2', '0', type2['road'], type2['numbers'], type2['beat'])
        DBM.maka_do_sql(insertsql)

        type3 = self.getRandom()
        insertsql = "INSERT INTO {0}.{1} (qishutype,status,road,numbers,beat) VALUES ('{2}','{3}','{4}','{5}','{6}');".format(
            DBC.Database, 'yuce', str(long(top)+1)+'3', '0', type3['road'], type3['numbers'], type3['beat'])
        DBM.maka_do_sql(insertsql)

        type4 = self.getRandom()
        insertsql = "INSERT INTO {0}.{1} (qishutype,status,road,numbers,beat) VALUES ('{2}','{3}','{4}','{5}','{6}');".format(
            DBC.Database, 'yuce', str(long(top)+1)+'4', '0', type4['road'], type4['numbers'], type4['beat'])
        DBM.maka_do_sql(insertsql)

        type5 = self.getRandom()
        insertsql = "INSERT INTO {0}.{1} (qishutype,status,road,numbers,beat) VALUES ('{2}','{3}','{4}','{5}','{6}');".format(
            DBC.Database, 'yuce', str(long(top)+1)+'5', '0', type5['road'], type5['numbers'], type5['beat'])
        DBM.maka_do_sql(insertsql)

        type6 = self.getRandom()
        insertsql = "INSERT INTO {0}.{1} (qishutype,status,road,numbers,beat) VALUES ('{2}','{3}','{4}','{5}','{6}');".format(
            DBC.Database, 'yuce', str(long(top)+1)+'6', '0', type6['road'], type6['numbers'], type6['beat'])
        DBM.maka_do_sql(insertsql)

        type7 = self.getRandom()
        insertsql = "INSERT INTO {0}.{1} (qishutype,status,road,numbers,beat) VALUES ('{2}','{3}','{4}','{5}','{6}');".format(
            DBC.Database, 'yuce', str(long(top)+1)+'7', '0', type7['road'], type7['numbers'], type7['beat'])
        DBM.maka_do_sql(insertsql)

        type8 = self.getRandom()
        insertsql = "INSERT INTO {0}.{1} (qishutype,status,road,numbers,beat) VALUES ('{2}','{3}','{4}','{5}','{6}');".format(
            DBC.Database, 'yuce', str(long(top)+1)+'8', '0', type8['road'], type8['numbers'], type8['beat'])
        DBM.maka_do_sql(insertsql)

        type9 = self.getRandom()
        insertsql = "INSERT INTO {0}.{1} (qishutype,status,road,numbers,beat) VALUES ('{2}','{3}','{4}','{5}','{6}');".format(
            DBC.Database, 'yuce', str(long(top)+1)+'9', '0', type9['road'], type9['numbers'], type9['beat'])
        DBM.maka_do_sql(insertsql)

        type10 = self.getRandom()
        insertsql = "INSERT INTO {0}.{1} (qishutype,status,road,numbers,beat) VALUES ('{2}','{3}','{4}','{5}','{6}');".format(
            DBC.Database, 'yuce', str(long(top)+1)+'10', '0', type10['road'], type10['numbers'], type10['beat'])
        DBM.maka_do_sql(insertsql)

    def getRandom(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        roads = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        beats = [100, 200, 500, 1000, 2000]
        random.shuffle(numbers)
        random.shuffle(roads)
        random.shuffle(beats)
        return {'numbers':numbers,'road':roads[0],'beat':beats[0]}