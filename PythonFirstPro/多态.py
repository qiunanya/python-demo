class Animal:
    def say(self):
        print('我是一个动物')
        pass
    pass

class Duck(Animal):
    def say(self):
        print('小鸭')
        pass
    pass

class Dog(Animal):
    def say(self):
        print('小狗')
        pass
    pass

class Cat(Animal):
    def say(self):
        print('小猫')
        pass
    pass

# 公共方法
def common(obj):
    obj.say()
    pass

d = Duck()
d.say()
# 多态体现，循环调用
itemList = [Dog(), Cat(), Duck()]
for item in itemList:
    common(item)
    pass
