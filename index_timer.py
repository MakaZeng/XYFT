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

reload(sys)
sys.setdefaultencoding('utf-8')

print 'Crawser_Start ----------------> '
beginURL = 'http://www.cp66607.com/api/xyft?act=index'

content = NM.maka_simplegetcontent(beginURL)

if len(content):
    s = json.loads(content)
    first = s[0]

    qishu = first["xissue"]
    shijian = float(first["xkjtime"]) + 60*60
    shijian = DU.convertSecondsFrom1970ToDate(shijian)

    n1 = first["xn1"]
    n2 = first["xn2"]
    n3 = first["xn3"]
    n4 = first["xn4"]
    n5 = first["xn5"]
    n6 = first["xn6"]
    n7 = first["xn7"]
    n8 = first["xn8"]
    n9 = first["xn9"]
    n10 = first["xn10"]

    sql = "INSERT INTO {1}.{2} ({3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14}) VALUES ('{15}','{16}','{17}','{18}','{19}','{20}','{21}','{22}','{23}','{24}','{25}','{26}');".format('',CF.Database,CF.HISTAB,CF.HISQI,CF.HISTIME,CF.HISN1,CF.HISN2,CF.HISN3,CF.HISN4,CF.HISN5,CF.HISN6,CF.HISN7,CF.HISN8,CF.HISN9,CF.HISN10,qishu,shijian,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10)
    DBM.maka_do_sql(sql)
    cm = CCM.CalculateManager()
    cm.calculate()
    time.sleep(1)
    yc = Yuce.Yuce()
    yc.startYuce()
