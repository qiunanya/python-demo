# 自定义异常
class TooLongMyException(Exception):
    def __init__(self, leng):
        self.len = leng
    pass

    def __str__(self):
        return '您输入的姓名超过长度'+str(self.len)+ '超出长度了'
    pass

def name_test():
    name = input('请输入姓名。。。。')
    try:
        if len(name) > 5:
            raise TooLongMyException(len(name)) # 捕获异常
        else:
            print(name)
            pass
        pass
    except TooLongMyException as result:
        # 处理异常
        print(result)
        pass
    finally:
        # 最后执行
        print('程序执行完毕了')

name_test()