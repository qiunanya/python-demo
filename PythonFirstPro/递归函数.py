# 递归函数，自己调用自己，不过需要条件才能停下循环，否则地狱循环
# n的阶层算法
def totalSum(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    pass
    return result

print(' n 的阶层为{}'.format(totalSum(10)))

# 用递归实现
def digui(n):
    '''
    递归实现
    :param n阶层数字
    :return:
    '''
    if n == 1:
        return 1
    else:
        return n * digui(n-1)
    pass

print(' 递归实现阶层为{}'.format(totalSum(10)))

