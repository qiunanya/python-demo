# 文件导入方式
import time
print(time.time(), time.localtime(), time.asctime())

import time as myTime
print(myTime.asctime())

from time import ctime, time, asctime
print(ctime(), time(), asctime())
