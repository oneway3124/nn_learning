import time
import datetime

import os


# '''把时间戳转化为时间: 1479264792 to 2016-11-16 10:53:12'''
def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)


def get_FileCreateTime(filePath):
    filePath = unicode(filePath, 'utf8')
    t = os.path.getctime(filePath)
    return TimeStampToTime(t)


if __name__ == '__main__':
    if (len(os.sys.argv) < 1):
        raise TypeError()
    else:
        print("os.sys.argv[0]: %s" % os.sys.argv[0])  # os.sys.argv[0] is the current file, in this case, file_ctime.py
    f = os.sys.argv[0]
    mtime = time.ctime(os.path.getmtime(f))
    ctime = time.ctime(os.path.getctime(f))
    print("Last modified : %s, last created time: %s" % (mtime, ctime))
    f1 = os.sys.argv[1]
    mtime = time.ctime(os.path.getmtime(f1))
    ctime = time.ctime(os.path.getctime(f1))
    print("create time:%s, modified time %s" % (ctime, mtime))

# ————————————————
# 版权声明：本文为CSDN博主「Hardy-Lee」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/liyuan_669/article/details/25347037
