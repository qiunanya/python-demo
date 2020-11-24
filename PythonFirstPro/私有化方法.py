# 私有化方法, 在方法前加两个下划线
class Animal:
    def __eat(self):
        print('吃东西')
        pass
    def running(self):
        self.__eat()
        print('跑起来哈哈哈')
        pass

class Bird(Animal):
    pass

b = Bird()
b.running()