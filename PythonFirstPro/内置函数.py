# 绝对值
print(abs(-548))
# 近似值
print(round(3.65))
print(round(2.35445, 2))

# pow 求次方
print(3**3)
print(pow(3,3))

# divmod 求商和余数得
print(divmod(7, 3))
print(divmod(9, 3))

# 求最大值和最小值
print(max([1, 25, 26, 22, 4444]))
print(min([1, 25, 26, 22, 4444]))

# 求和
print(sum(range(1, 45)))

# eval 执行字符串表达式, 可以动态执行表达式a
a, b, c = 1, 2, 3
print('动态执行的函数 {}'.format(eval('a+b*c*898')))

def testFun():
    print('被调用了')
    pass
eval('testFun()')

# 类型转换
int()
float()
print(str('45465464'))
print(ord('a'))
print(chr(97))
bool()
#bin()
tuplu = (1, 2, 3, 4)
l = list(tuplu)
l.append('强制转换python')
# 元组转换成列表
print(list(tuplu), type(l))
# 列表转换成元组
print(tuple(l))
tuple()

# 字典的操作
dic = dict(name='qiu', age=15) #创建字典并赋值给字典
print(type(dict), dic, '字典类型')

