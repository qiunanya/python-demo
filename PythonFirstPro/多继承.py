# 多继承
class Immortal:
    def flying(self):
        print('神仙会飞')
    pass

class Monkey:
    def jump(self):
        print('猴子会跳动')
    pass

class Children(Immortal, Monkey):
    pass

class D(object):
    def eat(self):
        print('D.eat')
    pass
class C(D):
    def eat(self):
        print('C.eat')
        pass
    pass
class B(D):
    pass

class A(B, C):
    pass

a = A()
a.eat()
print(A.__mro__)

d = Children()
d.jump()
d.flying()