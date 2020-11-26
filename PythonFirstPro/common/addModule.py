# 加法模块
def add(x, y):
    """
    加法
    :param x: 参数 x
    :param y: 参数 y
    :return: 返回结果
    """
    return x+y
    pass


# 内部测试
if __name__ == '__main__':
    res = add(1, 2)
    print(res)
    print('模块__name__ 变量=%s' %__name__)