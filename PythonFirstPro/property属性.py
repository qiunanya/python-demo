# property 属性
class Person:
    def __init__(self):
        self.__age = 15
        pass

    # def get_age(self):
    #     return self.__age
    #     pass
    #
    # def set_age(self, age):
    #     # print('年龄不能小于0') if self.__age < 0 else self.__age = age
    #     if age < 0:
    #         print('年龄不能小于 0 ')
    #     else:
    #         self.__age = age
    #         pass
    #     pass
    # age = property(get_age, set_age)
    @property # 使用装饰器对age进行装饰，提供一个getter方法
    def age(self):
        return self.__age
    pass
    @age.setter # 使用装饰器进行修饰，提供一个setter方法
    def age(self, age):
        if age < 0:
            print('年龄不能小于 0 ')
        else:
            self.__age = age
            pass

p = Person()
p.age = 30
print(p.age)
