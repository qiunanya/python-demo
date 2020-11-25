# python 类定义

class Person:
    """
    对应特征
    """
    name = '邱南亚'
    age = 254

    def __init__(self):
        # 给对象增加属性
        self.height = 1235

    def eat(self):
        print(self.name + "吃饭了哈"+str(self.height))
        pass

    def running(self):
        print(self.name + "跑起来了")
        pass


# 创建对象
qiu = Person()
qiu.name = '诸葛亮'
qiu.eat()
qiu.running()
