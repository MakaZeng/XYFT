import time


def convertSecondsFrom1970ToDate(seconds):
    seconds = float(seconds)
    x = time.localtime(seconds)
    x = time.strftime('%Y-%m-%d %H:%M:%S', x)
    return x

def getNextDayZeroQishu(str):
    date = str[0:8]
    seconds = time.mktime(time.strptime(date, '%Y%m%d'))
    seconds = float(seconds)
    seconds = seconds + 25*60*60
    x = time.localtime(seconds)
    x = time.strftime('%Y%m%d', x)
    x = x + '000'
    return x