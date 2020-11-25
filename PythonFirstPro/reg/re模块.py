# re 正则库模块
import re
express = "Python is the best language in the world"
# result = re.match('i', express, re.I) # 匹配字符串起始位置的一个匹配规则, re.I忽略大小写
result = re.match('(.*) is (.*?) .*', express, re.I|re.M)
if result:
    print('匹配成功')
    print(result)
    print(result.group())
    print(result.group(1))

else:
    print('匹配失败')

