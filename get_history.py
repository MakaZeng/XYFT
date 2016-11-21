import Network.NetworkManager as NM
import Dao.MysqlDBManager as DBM
import Dao.MysqlDBConfig as CF
import sys
import time
import re
import json
import Calculate.CalculateManager as CCM
import Util.DateUtil as DU
import Calculate.Yuce as Yuce
import demjson

reload(sys)
sys.setdefaultencoding('utf-8')


date = '20161121'

start = 'http://api.caipiaokong.com/lottery/?name=xyft&format=json&uid=640474&token=9bec41b305460ddf056e4251842c7df94bf8d63e&date='+date

if len(start):
    content = NM.maka_simplegetcontent(start)
    dic = json.loads(content)

    for i in dic:
        qishu = str(i)
        idic = dic[i]
        shijian = idic['dateline']
        numbers = idic['number'].split(',')

        n1 = numbers[0]
        n2 = numbers[1]
        n3 = numbers[2]
        n4 = numbers[3]
        n5 = numbers[4]
        n6 = numbers[5]
        n7 = numbers[6]
        n8 = numbers[7]
        n9 = numbers[8]
        n10 = numbers[9]

        sql = "INSERT INTO {1}.{2} ({3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14}) VALUES ('{15}','{16}','{17}','{18}','{19}','{20}','{21}','{22}','{23}','{24}','{25}','{26}');".format(
            '', CF.Database, CF.HISTAB, CF.HISQI, CF.HISTIME, CF.HISN1, CF.HISN2, CF.HISN3, CF.HISN4, CF.HISN5,
            CF.HISN6, CF.HISN7, CF.HISN8, CF.HISN9, CF.HISN10, qishu, shijian, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10)
        DBM.maka_do_sql(sql)
        cm = CCM.CalculateManager()
        cm.calculate()
        json = demjson.encode(cm.results)
        sql = "CREATE TABLE IF NOT EXISTS tongji (`qishu` varchar(100) COLLATE utf8_bin NOT NULL,`result` varchar(100000) DEFAULT NULL,PRIMARY KEY (`qishu`),UNIQUE KEY `qishu_UNIQUE` (`qishu`)) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;"
        DBM.maka_do_sql(sql)
        sql = "INSERT INTO {0}.{1} (qishu,result) VALUES ('{2}','{3}');".format(CF.Database, 'tongji', qishu, json)
        DBM.maka_do_sql(sql)
    time.sleep(1)
    date = str(long(date) -1)

