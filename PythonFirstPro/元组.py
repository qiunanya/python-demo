#  tuple 元组的创建
tupleA = ()  # 空元组
tupleA = ('abjc', 89, 93.23, 11, 11, 11, '到底', [11, 22, 33])
print(type(tupleA), tupleA)

# 元组的查询
for i in tupleA:
    print(i, end='  ')

print(tupleA[2])
# 切片获取元组值, 含首不含尾
print(tupleA[2:4])

# 倒序
print(tupleA[::-1])

# count函数 统计元素出现的次数
print(tupleA.count(11))
# 当元组中只有一个元素的时候，必须要在数据项的后边加上逗号，否则不是元组
# ss = ('a',)
# print(type(ss))