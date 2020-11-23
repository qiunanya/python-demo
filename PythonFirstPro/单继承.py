# python 面向对象的三大特征：封装(拥有父类属性和行为)，继承，多态
class Animal:

    def eat(self):
        print('父类吃的方法')
        pass

    def drink(self):
        print("父类喝的方法")
        pass
    pass

# dog 继承Animal 父类
class Dog(Animal):
    def dance(self):
        print("小狗跳舞")
        pass
    pass
# cat 继承Animal 父类
class Cat(Animal):
    def miao(self):
        print("小猫喵喵叫")
        pass
    pass

d = Dog()
d.eat()
c = Cat()
c.drink()