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
dataStr = 'I Love Python'
print(dataStr.find('M'))
print(dataStr.find('L'))
print(dataStr.index('o'))

