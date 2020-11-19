# 匿名函数 lambda 参数1 参数2 参数3：表达式

def computer(x, y):
    return x+y
    pass

m = lambda x, y: x+y
# 通过变量调用匿名函数
print('匿名函数结果：%s' % m(10, 20))
print(computer(1, 3))