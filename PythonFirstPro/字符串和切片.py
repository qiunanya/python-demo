test = '邱南亚'
name = ' py th  on  '
print('获取第一个 %s' %test[0])
for i in test:
    print(i, end='')
    pass

# 首字母变成大写 函数：capitalize
print('首字母大写 %s' % name.capitalize())

# 去掉左右两边空格
b = name.strip()
# 去掉所以空格
c = name.replace(' ', '')
l = name.lstrip()
rr = name.lstrip()
print('去掉左右空格'+b)
print('去掉所有空格'+c)
print('去掉左边空格'+l)
print('去掉右边空格'+rr)
print('name的内存地址 %d' % id(name))

# 字符串查找 find函数可以查找目标对象在序列对象中的值，如果没有找到就返回-1
# index 如果没有找到对象的数据 便会异常，而find函数不会，找不到返回 -1
# __contains__:是否包含，包含返回true，否则返回false
dataStr = 'I Love Python'
print(dataStr.find('M'))
print(dataStr.find('L'))
print(dataStr.index('o'))
print(dataStr.__contains__('L'))
print(dataStr.startswith('I'))
print(dataStr.endswith('n'))
# 设置查找范围
print(dataStr.startswith('P', 2, 10))
print(dataStr.upper())          # 把所有字符中的小写字母转换成大写字母
print(dataStr.lower())          # 把所有字符中的大写字母转换成小写字母
print(dataStr.capitalize())     # 把第一个字母转化为大写字母，其余小写
print(dataStr.title())          # 把每个单词的第一个字母转化为大写，其余小写

# *** 切片功能测试 ,其他语言没有
strs = 'hello world'
# slice [start:end:step] 左闭右开 start <= value < end
print(strs)
print(strs[0])
print(strs[2:5])    # 2-5下标之间的数据
print(strs[2:])     # 2：取剩下的部分字符串
print('倒序输出：'+strs[::-1])  # 倒序输出, 负号表示方向, 从右边向左遍历