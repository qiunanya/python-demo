# 字典是由键值对组成的集合，没有下标概念，是一个无序的键值集合，是内置的高级数据类型

dictA = {"pro":'计算机'}
dictA['name'] = '周杰伦'
dictA['age'] = '32'
dictA['arr'] = '歌手'
# 修改
print("修改前name：%s" % dictA['name'])
dictA['name'] = '司马懿'
dictA.update({'age': 544})

# 增加
dictA.update({'height': 187})

# 删除
del dictA['age']

# 删除最后一个元素
dictA.pop('height')

print(dictA, len(dictA), type(dictA), property(dictA))

for i in dictA:
    print(i, end=' ')
    pass

# 字典和js的对象很相似啊
# 获取键值
print('获取所有键 %s \n' % dictA.keys())
print('获取所有值 %s \n' % dictA.values())

# 获取键值
print('获取所有的键值 %s' % dictA.items())

# 循环遍历 获取每对键值
for i in dictA.items():
    print(i, len(i))
    pass

# 获取键和值
for key, value in dictA.items():
    print('%s == %s' % (key, value))
    pass

# 对字典进行排序, 按key排序和按值排序
# sorted() 按key排序
print(sorted(dictA.items(), key=lambda d:d[0]))
# 按value排序
print(sorted(dictA.items(), key=lambda d:d[1]))

