# 重写父类方法
class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        pass

    def bark(self):
        print('狗叫')
        pass
class Cat(Dog):
    def __init__(self, name, color):
        # 调用父类方法
        super().__init__(name, color)
        Dog.__init__(self, name, color)
        pass
    def bark(self):
        print('重写父类方法 bark')
        print(self.name)
        pass

c = Cat('咖啡猫', '灰色')
c.bark()