# 析构方法案例，python 内置函数可以叫做魔法函数
class Animal:
    def __init__(self, name='小花猫'):
        self.name = name
        print('这是构造初始化方法')
    pass

    def __del__(self):
        # 释放对象，一旦始放完毕 对象便不能在使用
        print("%s 这个对象被彻底清除了" % self.name)
        print("这是析构方法")
    pass

cat = Animal()