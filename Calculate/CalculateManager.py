import Dao.MysqlDBConfig as DBC
import Dao.MysqlDBManager as DBM


class CalculateManager(object):
    leftMostType = 1
    leftTotalCount = 0

    dataList = []
    results = []
    databaseStartNumber = 0

    def __init__(self):
        super(CalculateManager, self).__init__()

    def calculate(self):
        sql = "select * from {0} order by {1} DESC LIMIT 1000".format(DBC.HISTAB,DBC.HISQI)
        self.dataList = DBM.maka_do_sql(sql)
        if len(self.dataList) == 0:
            print 'ERROR database is empty'
        else:
            for i in range(1,10+2):
                targetArray = []
                targetDictionary = {str(i):targetArray}
                self.calculateSourceArray(self.dataList, targetArray, i);
                self.results.append(targetArray)

            numbers = []
            for dic in self.results[self.leftMostType]:
                arr = []
                arr.append(dic.get('number'))
                arr.append(dic.get('left'))
                numbers.append(arr)
            numbers.sort(lambda x, y: cmp(x[1], y[1]))

            rrrrrr = []
            for arr in numbers:
                rrrrrr.insert(0, arr[0])

            numbers = ','.join(rrrrrr)
            road = self.leftMostType + 1
            status = 0
            sql = 'insert into yuce values( {0},\'{1}\',\'{2}\',{3})'.format(int(self.databaseStartNumber + 2),
                                                                             numbers, str(road), status)


def calculateSourceArray(self, dataList, targetArray, type):
    beginNumber = 1
    endNumber = 10
    for i in range(beginNumber, endNumber + 1):
        dic = {}
        targetArray.append(dic)
    count = 0
    index = 1
    for model in dataList:
        number = model[1].replace("\"", '')
        number = number.replace('\'', '')
        numbers = number.split(',')
        if type == 0:
            count = numbers[0]
        elif type == 1:
            count = numbers[1]
        elif type == 2:
            count = numbers[2]
        elif type == 3:
            count = numbers[3]
        elif type == 4:
            count = numbers[4]
        elif type == 5:
            count = numbers[5]
        elif type == 6:
            count = numbers[6]
        elif type == 7:
            count = numbers[7]
        elif type == 8:
            count = numbers[8]
        elif type == 9:
            count = numbers[9]
        else:
            count = 0
        dic = targetArray[int(count) - int(beginNumber)];
        dic['number'] = count
        if not (dic.get('left')):
            dic['left'] = index
        index = index + 1

    leftCount = 0
    for dic in targetArray:
        leftCount = leftCount + dic["left"]
    if type == 0:
        self.leftTotalCount = leftCount
        self.leftMostType = type
    else:
        if leftCount < self.leftTotalCount:
            self.leftMostType = type
            self.leftTotalCount = leftCount
