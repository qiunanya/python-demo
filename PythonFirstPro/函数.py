# 无参函数定义
def printInfo():
    # 函数体
    print('函数被调用了')
    pass

# 调用无参函数
printInfo()

# 有参函数定义，必选参数
def __paramsInfo__(name, height, age):
    print('%s 的身高 %s' % (name, height))
    print('%s 的年龄 %d' % (name, age))
    pass

# 调用有参函数
__paramsInfo__('赵四', 1.87, 25)
__paramsInfo__('诸葛亮', 1.88, 30)

# 参数分类
# 必选参数，默认参数[缺省参数]，可选参数，关键字参数
def sum(a=20, b=12):
    print('缺省参数使用=%d' % (a+b))
    pass

# 调用缺省参数
sum(1)

# 可变参数函数（当参数的个数不确定时使用）
def getComputer(*args):
    print(args)
    result = 0
    for i in args:
        result += i
        pass
    print('result = %d ' %result)
    pass
# 调用可变参数函数
getComputer(1, 2, 14, 54)

# 函数返回值
def returnParams(a, b):
    sums = a+b
    return sums
    pass

rs = returnParams(10, 20)
print(type(rs))
print('返回值：%d ' % rs)