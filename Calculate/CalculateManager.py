import Dao.MysqlDBConfig as DBC
import Dao.MysqlDBManager as DBM
import demjson

class CalculateManager(object):

    dataList = []
    results = []

    pointArray = [200,400,600,800,1000,1200,1400,1600,1800,2000,2200,2400,2600,2800,3000];

    def __init__(self):
        super(CalculateManager, self).__init__()

    def calculate(self):
        sql = "select * from {0} order by {1} DESC LIMIT 3000".format(DBC.HISTAB,DBC.HISQI)
        self.dataList = DBM.maka_do_sql(sql)
        if len(self.dataList) == 0:
            print 'ERROR database is empty'
        else:
            for i in range(1,10+2+1):
                targetArray = []
                targetDictionary = {str(i):targetArray}
                self.calculateSourceArray(self.dataList,targetDictionary, i);
                self.results.append(targetDictionary)
            # init self.results - > [{},{},{}]
            json = demjson.encode(self.results)
            print json

    def calculateSourceArray(self,dataList,targetDictionary,type):

        targetArray = targetDictionary[str(type)]

        inset = 4
        beginNumber = 1
        endNumber = 10+inset

        if type == 11:
            beginNumber = 3
            endNumber = 19+inset

        if type == 12:
            beginNumber =6
            endNumber = 27+inset

        for i in range(beginNumber,endNumber+1):
            ddd = {}
            targetArray.append(ddd)

        # init result -> [{{},{},{}},{{},{},{}},{{},{},{} ... } ...]

        count = 0
        index = 1
        temp = ''
        for model in dataList:
            numbers = []
            temp = int(model[2])
            numbers.append(temp)
            temp = int(model[3])
            numbers.append(temp)
            temp = int(model[4])
            numbers.append(temp)
            temp = int(model[5])
            numbers.append(temp)
            temp = int(model[6])
            numbers.append(temp)
            temp = int(model[7])
            numbers.append(temp)
            temp = int(model[8])
            numbers.append(temp)
            temp = int(model[9])
            numbers.append(temp)
            temp = int(model[10])
            numbers.append(temp)
            temp = int(model[11])
            numbers.append(temp)

            if type == 1:
                count = numbers[0]
            elif type == 2:
                count = numbers[1]
            elif type == 3:
                count = numbers[2]
            elif type == 4:
                count = numbers[3]
            elif type == 5:
                count = numbers[4]
            elif type == 6:
                count = numbers[5]
            elif type == 7:
                count = numbers[6]
            elif type == 8:
                count = numbers[7]
            elif type == 9:
                count = numbers[8]
            elif type == 10:
                count = numbers[9]
            elif type == 11:
                count = numbers[0]+numbers[1]
            elif type == 12:
                count = numbers[0]+numbers[1]+numbers[2]
            else:
                count = 0
            dic = targetArray[int(count) - int(beginNumber) + inset];
            if not (dic.get('title')):
                dic['title'] = count
            if not (dic.get('chance')):
                dic['chance'] = 0.5
            if not (dic.get('left')):
                dic['left'] = index

            if not (dic.get('cishu')):
                dic['cishu'] = 1
            else:
                dic['cishu'] = dic['cishu']+1

            middle = 0.5
            middle = (endNumber - beginNumber - inset)/2 + beginNumber

            if count > middle :
                #da
                da = targetArray[0]
                if not (da.get('title')):
                    da['title'] = 'da'
                if not (da.get('left')):
                    da['left'] = index
                if not (da.get('cishu')):
                    da['cishu'] = 1
                else:
                    da['cishu'] = da['cishu'] + 1
            elif count < middle:
                xiao = targetArray[1]
                if not (xiao.get('title')):
                    xiao['title'] = 'xiao'
                if not (xiao.get('left')):
                    xiao['left'] = index
                if not (xiao.get('cishu')):
                    xiao['cishu'] = 1
                else:
                    xiao['cishu'] = xiao['cishu'] + 1
            if count%2==1:
                # da
                dan = targetArray[2]
                if not (dan.get('title')):
                    dan['title'] = 'dan'
                if not (dan.get('left')):
                    dan['left'] = index
                if not (dan.get('cishu')):
                    dan['cishu'] = 1
                else:
                    dan['cishu'] = dan['cishu'] + 1
            else:
                shuang = targetArray[3]
                if not (shuang.get('title')):
                    shuang['title'] = 'shuang'
                if not (shuang.get('left')):
                    shuang['left'] = index
                if not (shuang.get('cishu')):
                    shuang['cishu'] = 1
                else:
                    shuang['cishu'] = shuang['cishu'] + 1


            if index%100 == 99:
                nnn = 0
                for inner in self.pointArray:
                    if index == inner -1 :
                        nnn = inner
                        break
                if nnn > 0:
                    for indic in targetArray :
                        i = 0
                        if indic.get('cishu'):
                            i = indic['cishu']

                        indic[str(nnn)] = i;

            index = index + 1
