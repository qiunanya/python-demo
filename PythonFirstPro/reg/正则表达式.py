# 爬虫，表达式都需要用到
import re # 导入正则模块
express = "I love python, because it is the best language in the world"
result = re.match('I', express) # 匹配字符串起始位置的一个匹配规则
print(type(result))
print(result.group())