import time


def convertSecondsFrom1970ToDate(seconds):
    seconds = float(seconds)
    x = time.localtime(seconds)
    x = time.strftime('%Y-%m-%d %H:%M:%S', x)
    print  x
    return x