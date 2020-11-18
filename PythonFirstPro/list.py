# list : python 当中非常重要的数据结构，是一种有序的数据集合
# 特点：支持增删改查

myList = ['彪哥', '马哥', '焦哥', '秋歌', '火锅', 464, True, 4654]
# 在列表尾部增加元素
myList.append('大哥')
# 在列表首部增加元素
myList.insert(0, '大哥大')
# 修改元素
myList[0] = 'perter 修改的'
myList[3] = 65464.4545
myList[6] = 123
# 删除指定的元素
myList.remove('秋歌')
# 删除第一个元素
# del myList[0]
# 批量删除多个
# def myList[1:3]
# 删除最后一个元素
myList.pop()
# 清除所有元素 结果为[]列表
# myList.clear()
# 查找元素
print(myList.__contains__('秋歌'))
# 扩展extend, 在列表尾部增加元素
data = list(range(10))  # 强制转换为list对象
myList.extend(data)
# index 返回下标
print('返回下标 %s' % myList.index('马哥'))
# 从第一个开始到第三个元素
print('从第一个开始到第三个元素: %s' % myList[1:3])
# 倒序输出列表
print('倒序输出列表: %s' % myList[::-1])
print(myList, len(myList), type(myList))